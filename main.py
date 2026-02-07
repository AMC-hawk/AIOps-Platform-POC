"""
main.py — OpsRamp API collector. Fetches page 1 from each endpoint,
saves each result to its own file under output/.
"""

import json
import os
import requests

from config import BASE_URL, TENANT_ID, CLIENT_ID, get_auth_headers
from endpoints import ENDPOINTS

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def resolve_path(path: str) -> str:
    """Replace {tenantId} and {clientId} placeholders."""
    return path.replace("{tenantId}", TENANT_ID).replace("{clientId}", CLIENT_ID)


def fetch_page1(endpoint: dict) -> dict | list | None:
    """Fetch page 1 from an endpoint. Returns JSON response or None."""
    url = BASE_URL + resolve_path(endpoint["path"])
    method = endpoint.get("method", "GET").upper()
    params = {"pageNo": 1, "pageSize": 100}

    print(f"\n{'─'*60}")
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
            print(f"  Error: {resp.text[:500]}")
            return None

    except Exception as e:
        print(f"  Exception: {e}")
        return None


def save(name: str, data):
    """Save JSON to output folder."""
    path = os.path.join(OUTPUT_DIR, f"{name}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, default=str)
    print(f"  Saved → {path}")


def main():
    total = len(ENDPOINTS)
    print("=" * 60)
    print(f"  OpsRamp API Collector — {total} endpoints")
    print("=" * 60)

    success = 0
    failed = 0

    for i, ep in enumerate(ENDPOINTS, 1):
        print(f"\n  [{i}/{total}]", end="")
        data = fetch_page1(ep)
        if data is not None:
            save(ep["name"], data)
            success += 1
        else:
            failed += 1

    print(f"\n{'='*60}")
    print(f"  Done!  ✅ {success} ok  /  ❌ {failed} failed")
    print(f"  Output: {OUTPUT_DIR}/")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
