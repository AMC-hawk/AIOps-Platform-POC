"""
endpoints.py — List of GET endpoints to hit. Just add more dicts to try new APIs.
"""

ENDPOINTS = [
    {
        "name": "resources_search",
        "path": "/api/v2/tenants/{tenantId}/resources/search",
        "description": "Search all managed resources",
    },
    {
        "name": "resources_minimal",
        "path": "/api/v2/tenants/{clientId}/resources/minimal",
        "description": "Minimal resource list",
    },
    {
        "name": "metrics_search",
        "path": "/api/v2/tenants/{tenantId}/metrics",
        "description": "Search metrics",
    },
    {
        "name": "alerts_search",
        "path": "/api/v2/tenants/{tenantId}/alerts/search",
        "description": "Search alerts",
    },
    # ── Add more endpoints below ──────────────────────
    # {
    #     "name": "my_new_api",
    #     "path": "/api/v2/tenants/{tenantId}/something/search",
    #     "description": "What it does",
    # },
]
