"""
config.py — Your OpsRamp credentials and token management.
"""

import requests

BASE_URL = "*"
TENANT_ID = "*"
CLIENT_ID = "*"
CLIENT_SECRET = "*"

_cached_token = None


def get_bearer_token():
    """Fetch and cache the bearer token using OAuth2 client credentials."""
    global _cached_token

    if _cached_token:
        return _cached_token

    token_url = f"{BASE_URL}/tenancy/auth/oauth/token"

    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    response = requests.post(token_url, data=payload)
    response.raise_for_status()

    _cached_token = response.json().get("access_token")
    return _cached_token


def get_auth_headers():
    """Return headers with Bearer token for API requests."""
    return {
        "Authorization": f"Bearer {get_bearer_token()}",
        "Content-Type": "application/json"
    }
