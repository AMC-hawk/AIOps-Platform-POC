"""
main.py - OpsRamp API collector. Fetches page 1 from each endpoint,
saves each result to its own file under output/.
"""

import json
import os
import requests

from config import BASE_URL, TENANT_ID, get_auth_headers
from endpoints import ENDPOINTS

OUTPUT_DIR = "output"
ERRORS_DIR = os.path.join(OUTPUT_DIR, "_errors")
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(ERRORS_DIR, exist_ok=True)


def resolve_path(path: str) -> str:
    """Replace all tenant/client placeholder variants.

    NOTE: In OpsRamp API paths, {clientId} means the client *organization* UUID,
    NOT the OAuth client_id used for authentication. For client-level tenants
    both {tenantId} and {clientId} resolve to the same org UUID (TENANT_ID).
    Some automation endpoints use {tenant_id} (with underscore).
    {partnerId} also maps to TENANT_ID (only relevant for MSP accounts).
    """
    return (path
            .replace("{tenantId}", TENANT_ID)
            .replace("{clientId}", TENANT_ID)
            .replace("{tenant_id}", TENANT_ID)
            .replace("{partnerId}", TENANT_ID)
            .replace("{mspId}", TENANT_ID))


def fetch_page1(endpoint: dict) -> dict | list | None:
    """Fetch page 1 from an endpoint. Returns JSON response or None."""
    url = BASE_URL + resolve_path(endpoint["path"])
    method = endpoint.get("method", "GET").upper()

    # Build query params: defaults + any endpoint-specific extras
    params = {"pageNo": 1, "pageSize": 100}
    if "params" in endpoint:
        params.update(endpoint["params"])

    print(f"\n{'-'*60}")
    print(f"  {endpoint['name']}")
    print(f"  {endpoint['description']}")
    print(f"  {method} {url}")

    try:
        if method == "POST":
            body = endpoint.get("body", {})
            resp = requests.post(url, headers=get_auth_headers(), json=body, timeout=30)
        else:
            resp = requests.get(url, headers=get_auth_headers(), params=params, timeout=30)

        print(f"  Status: {resp.status_code}")

        if resp.status_code == 200:
            data = resp.json()
            if isinstance(data, dict):
                total = data.get("totalResults", "N/A")
                print(f"  totalResults: {total}")
            elif isinstance(data, list):
                print(f"  Results: {len(data)} items")
            return data
        else:
            error_text = resp.text[:500]
            print(f"  Error: {error_text}")
            # Save error for debugging
            save_error(endpoint["name"], resp.status_code, error_text)
            return None

    except Exception as e:
        print(f"  Exception: {e}")
        save_error(endpoint["name"], 0, str(e))
        return None


def save(name: str, data):
    """Save JSON to output folder."""
    path = os.path.join(OUTPUT_DIR, f"{name}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, default=str)
    print(f"  Saved -> {path}")


def save_error(name: str, status: int, text: str):
    """Save error info for debugging."""
    path = os.path.join(ERRORS_DIR, f"{name}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"Status: {status}\n\n{text}")


def main():
    total = len(ENDPOINTS)
    active = [ep for ep in ENDPOINTS if not ep.get("msp_only")]
    skipped_msp = [ep for ep in ENDPOINTS if ep.get("msp_only")]

    print("=" * 60)
    print(f"  OpsRamp API Collector -- {total} endpoints")
    print(f"  Active: {len(active)}  |  MSP-only (skipped): {len(skipped_msp)}")
    print("=" * 60)

    if skipped_msp:
        print(f"\n  [!] Skipping MSP-only endpoints:")
        for ep in skipped_msp:
            print(f"    - {ep['name']}")

    success = 0
    failed = 0

    for i, ep in enumerate(active, 1):
        print(f"\n  [{i}/{len(active)}]", end="")
        data = fetch_page1(ep)
        if data is not None:
            save(ep["name"], data)
            success += 1
        else:
            failed += 1

    print(f"\n{'='*60}")
    print(f"  Done!  OK: {success}  /  FAILED: {failed}  /  MSP-ONLY: {len(skipped_msp)}")
    print(f"  Output: {OUTPUT_DIR}/")
    if failed:
        print(f"  Errors: {ERRORS_DIR}/")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
