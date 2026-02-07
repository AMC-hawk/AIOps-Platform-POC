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
        "path": "/api/v2/tenants/{tenantId}/resources/minimal",
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
    {
        "name": "logs_queries",
        "path": "/api/v3/tenants/{tenantId}/logs/queries",
        "description": "Logs queries",
        "method": "POST",
        "body": {
            "query": "{source = \"kubernetes\", k8s.namespace.name = \"dynamo-workload\"}",
            "fields": [],
            "limit": 1000,
            "start": 1770022800000000000,
            "end": 1770109200000000000
        }
    },
    # ── Add more endpoints below ──────────────────────
    # {
    #     "name": "my_new_api",
    #     "path": "/api/v2/tenants/{tenantId}/something/search",
    #     "description": "What it does",
    # },
]
