"""
main.py — Simple OpsRamp API collector. Fetches page 1 from each endpoint.
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


def fetch_page1(endpoint: dict) -> dict | None:
    """Fetch page 1 from an endpoint. Returns JSON response or None."""
    url = BASE_URL + resolve_path(endpoint["path"])
    method = endpoint.get("method", "GET").upper()
    params = {"pageNo": 1, "pageSize": 100}

    print(f"\n{'─'*50}")
    print(f"  {endpoint['name']}  —  {endpoint['description']}")
    print(f"  {method} {url}")

    try:
        if method == "POST":
            body = endpoint.get("body", {})
            resp = requests.post(url, headers=get_auth_headers(), json=body, params=params, timeout=30)
        else:
            resp = requests.get(url, headers=get_auth_headers(), params=params, timeout=30)
        print(f"  Status: {resp.status_code}")

        if resp.status_code == 200:
            data = resp.json()
            if isinstance(data, dict):
                total = data.get("totalResults", "N/A")
                print(f"  totalResults: {total}")
            else:
                print(f"  Results: {len(data)} items")
            return data
        else:
            print(f"  Error: {resp.text[:300]}")
            return None

    except Exception as e:
        print(f"  Exception: {e}")
        return None


def save(name: str, data: dict):
    """Save JSON to output folder."""
    path = os.path.join(OUTPUT_DIR, f"{name}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, default=str)
    print(f"  Saved → {path}")


def main():
    print("=" * 50)
    print("  OpsRamp API Collector — Page 1 Fetch")
    print("=" * 50)

    for ep in ENDPOINTS:
        data = fetch_page1(ep)
        if data:
            save(ep["name"], data)

    print(f"\n{'='*50}")
    print(f"  Done! Check the '{OUTPUT_DIR}/' folder.")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    main()
