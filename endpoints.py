"""
endpoints.py — ALL OpsRamp API endpoints (v2 + v3), GET and POST-for-query.

Sources (verified against actual docs):
  https://develop.opsramp.com/v2
  https://develop.opsramp.com/v3

Each endpoint dict:
  name        — unique identifier (also used as output filename)
  path        — URL path template (placeholders: {tenantId}, {clientId}, {tenant_id})
  description — what it returns
  method      — "GET" (default) or "POST"
  body        — required body for POST endpoints (minimal)
  params      — extra query-string parameters the API requires
  msp_only    — True if endpoint requires MSP/SERVICEPROVIDER access (skipped)

To add a new endpoint, just copy-paste a dict and change the values.
"""

ENDPOINTS = [

    # ╔══════════════════════════════════════════════════════════╗
    # ║                   V2 — RESOURCE MANAGEMENT              ║
    # ╚══════════════════════════════════════════════════════════╝

    {
        "name": "v2_resources_search",
        "path": "/api/v2/tenants/{tenantId}/resources/search",
        "description": "Search all managed resources",
    },
    {
        "name": "v2_resources_minimal",
        "path": "/api/v2/tenants/{clientId}/resources/minimal",
        "description": "Minimal resource list (lightweight)",
    },
    {
        "name": "v2_resources_antivirus",
        "path": "/api/v2/tenants/{clientId}/resources/antivirus/search",
        "description": "Get latest antivirus definitions (500 if no AV data)",
    },
    {
        "name": "v2_audit_recordings",
        "path": "/api/v2/tenants/{tenantId}/resources/auditRecordings/search",
        "description": "Console audit recording details",
    },
    {
        "name": "v2_decommissioned_resources",
        "path": "/api/v2/tenants/{clientId}/history/resources",
        "description": "Search decommissioned resources",
    },
    {
        "name": "v2_device_groups_minimal",
        "path": "/api/v2/tenants/{clientId}/deviceGroups/minimal",
        "description": "Minimal details of device groups",
    },
    {
        "name": "v2_device_groups_search",
        "path": "/api/v2/tenants/{clientId}/deviceGroups/search",
        "description": "Root level device groups",
    },
    {
        "name": "v2_service_groups_search",
        "path": "/api/v2/tenants/{clientId}/serviceGroups/search",
        "description": "Root-level service groups",
    },
    {
        "name": "v2_service_groups_minimal",
        "path": "/api/v2/tenants/{clientId}/serviceGroups/minimal",
        "description": "Minimal details of service groups",
    },
    {
        "name": "v2_sites_search",
        "path": "/api/v2/tenants/{tenantId}/sites/search",
        "description": "Search sites",
    },
    {
        "name": "v2_sites_minimal",
        "path": "/api/v2/tenants/{clientId}/sites/minimal",
        "description": "Minimal site details",
    },
    # v2_device_mgmt_policy_search removed - requires non-empty policy name
    # Use v2_device_mgmt_policy_list below instead
    {
        "name": "v2_device_mgmt_policy_list",
        "path": "/api/v2/tenants/{clientId}/policies/management",
        "description": "List device management policies",
    },
    {
        "name": "v2_resource_type_minimal",
        "path": "/api/v2/tenants/{clientId}/resourceType/minimal",
        "description": "Minimal resource type details",
    },
    {
        "name": "v2_device_warranties",
        "path": "/api/v2/tenants/{clientId}/deviceWarranties",
        "description": "Get device warranties (500 if none configured)",
    },
    {
        "name": "v2_synthetics_public_locations",
        "path": "/api/v2/cfg/synthetics/locations",
        "description": "Public locations for synthetics",
    },
    {
        "name": "v2_synthetics_private_locations",
        "path": "/api/v2/tenants/{clientId}/synthetics/checkpoints",
        "description": "Private locations for synthetics",
    },

    # ╔══════════════════════════════════════════════════════════╗
    # ║                   V2 — ALERTS                           ║
    # ╚══════════════════════════════════════════════════════════╝

    {
        "name": "v2_alerts_search",
        "path": "/api/v2/tenants/{tenantId}/alerts/search",
        "description": "Search alerts across the tenant",
    },
    {
        "name": "v2_alert_types",
        "path": "/api/v2/alertTypes",
        "description": "Get supported alert types",
    },
    {
        "name": "v2_escalations_search",
        "path": "/api/v2/tenants/{tenantId}/escalations/search",
        "description": "Search alert escalation policies",
    },
    {
        "name": "v2_rosters_search",
        "path": "/api/v2/tenants/{tenantId}/rosters/search",
        "description": "Search rosters",
    },
    {
        "name": "v2_alert_correlation_policies",
        "path": "/api/v2/tenants/{tenantId}/policies/alertCorrelation",
        "description": "Get alert correlation policies",
    },
    {
        "name": "v2_alert_prediction_policies",
        "path": "/api/v2/tenants/{tenantId}/policies/alertprediction",
        "description": "Get alert prediction policies",
    },
    {
        "name": "v2_first_response_policies",
        "path": "/api/v2/tenants/{tenantId}/policies/firstResponse",
        "description": "Get first response policy details",
    },
    {
        "name": "v2_scheduled_maintenance_search",
        "path": "/api/v2/tenants/{clientId}/scheduleMaintenances/search",
        "description": "Search scheduled maintenance windows",
    },

    # ╔══════════════════════════════════════════════════════════╗
    # ║                   V2 — METRICS                          ║
    # ╚══════════════════════════════════════════════════════════╝

    {
        "name": "v2_metrics",
        "path": "/api/v2/tenants/{tenantId}/metrics",
        "description": "Search metrics within tenant",
    },

    # ╔══════════════════════════════════════════════════════════╗
    # ║                   V2 — TICKETS                          ║
    # ╚══════════════════════════════════════════════════════════╝

    {
        "name": "v2_incidents_search",
        "path": "/api/v2/tenants/{tenantId}/incidents/search",
        "description": "Search incidents",
    },
    {
        "name": "v2_servicerequests_search",
        "path": "/api/v2/tenants/{tenantId}/serviceRequests/search",
        "description": "Search service requests",
    },
    {
        "name": "v2_problems_search",
        "path": "/api/v2/tenants/{tenantId}/problems/search",
        "description": "Search problems",
    },
    {
        "name": "v2_tasks_search",
        "path": "/api/v2/tenants/{tenantId}/tasks/search",
        "description": "Search tasks",
    },
    {
        "name": "v2_incident_business_impacts",
        "path": "/api/v2/tenants/{clientId}/incidents/businessImpacts",
        "description": "Get incident business impact values",
    },
    {
        "name": "v2_incident_urgencies",
        "path": "/api/v2/tenants/{clientId}/incidents/urgencies",
        "description": "Get incident urgency values",
    },
    {
        "name": "v2_incident_forward_mapping",
        "path": "/api/v2/tenants/{tenantId}/incidents/forwardMapping",
        "description": "Get incident forward mapping",
    },
    {
        "name": "v2_incident_reverse_mapping",
        "path": "/api/v2/tenants/{tenantId}/incidents/reverseMapping",
        "description": "Get incident reverse mapping",
    },
    {
        "name": "v2_incident_status_reasons",
        "path": "/api/v2/tenants/{tenantId}/incidents/statusReasons",
        "description": "Get ticket status change reasons (incidents)",
    },
    {
        "name": "v2_incident_custom_form",
        "path": "/api/v2/tenants/{tenantId}/incidents/customForm",
        "description": "Get custom form details for incidents",
    },
    {
        "name": "v2_custom_fields",
        "path": "/api/v2/tenants/{tenantId}/customFields/INCIDENT",
        "description": "Get ticket custom fields for incidents",
    },
    {
        "name": "v2_sla_policies_search",
        "path": "/api/v2/tenants/{tenantId}/incidents/slaPolicies/search",
        "description": "Search SLA policies for incidents",
    },

    # ╔══════════════════════════════════════════════════════════╗
    # ║                   V2 — MONITORING                       ║
    # ╚══════════════════════════════════════════════════════════╝

    {
        "name": "v2_monitoring_templates_search",
        "path": "/api/v2/tenants/{tenantId}/monitoring/templates/search",
        "description": "Search monitoring templates",
    },
    {
        "name": "v2_syslog_rules",
        "path": "/api/v2/tenants/{tenantId}/monitoring/syslog/rules",
        "description": "Get syslog rules",
    },
    {
        "name": "v2_syslog_profiles",
        "path": "/api/v2/tenants/{tenantId}/monitoring/syslog/profiles",
        "description": "Get syslog profiles",
    },

    # ╔══════════════════════════════════════════════════════════╗
    # ║                   V2 — INTEGRATIONS                     ║
    # ╚══════════════════════════════════════════════════════════╝

    {
        "name": "v2_integrations_available",
        "path": "/api/v2/tenants/{tenantId}/integrations/available/search",
        "description": "Search available integrations/apps",
    },
    {
        "name": "v2_integrations_installed",
        "path": "/api/v2/tenants/{tenantId}/integrations/installed/search",
        "description": "Search installed integrations",
    },
    # v2_discovery_profiles_search removed - requires non-empty profile name
    {
        "name": "v2_integration_activity",
        "path": "/api/v2/tenants/{tenantId}/integrations/activity",
        "description": "Get integration activity log",
    },

    # ╔══════════════════════════════════════════════════════════╗
    # ║                   V2 — AUTOMATION                       ║
    # ╚══════════════════════════════════════════════════════════╝

    {
        "name": "v2_jobs_search",
        "path": "/api/v2/tenants/{tenantId}/jobs/search",
        "description": "Get tenant jobs list",
    },
    {
        "name": "v2_job_types",
        "path": "/api/v2/tenants/{tenantId}/jobs/types",
        "description": "Get job types",
    },
    {
        "name": "v2_rba_categories",
        "path": "/api/v2/tenants/{tenantId}/rba/categories",
        "description": "Get RBA script categories",
    },
    {
        "name": "v2_process_workflows_search",
        "path": "/api/v2/tenants/{tenant_id}/metadata/processes/search",
        "description": "Search process workflows",
    },
    {
        "name": "v2_process_instances_search",
        "path": "/api/v2/tenants/{tenant_id}/metadata/processes/processInstances/search",
        "description": "Search process instances",
    },

    # ╔══════════════════════════════════════════════════════════╗
    # ║                   V2 — KNOWLEDGE BASE                   ║
    # ╚══════════════════════════════════════════════════════════╝

    {
        "name": "v2_kb_categories",
        "path": "/api/v2/tenants/{tenantId}/kb/categorylist",
        "description": "Get KB category lists",
    },
    {
        "name": "v2_kb_articles",
        "path": "/api/v2/tenants/{tenantId}/kb/articlesList",
        "description": "Get list of KB articles",
    },
    {
        "name": "v2_kb_articles_search",
        "path": "/api/v2/tenants/{tenantId}/kb/articles/search",
        "description": "Search KB articles",
    },
    {
        "name": "v2_kb_templates",
        "path": "/api/v2/tenants/{tenantId}/kb/templatesList",
        "description": "Get KB templates list",
    },

    # ╔══════════════════════════════════════════════════════════╗
    # ║                   V2 — TENANCY / ACCESS CONTROLS        ║
    # ╚══════════════════════════════════════════════════════════╝

    {
        "name": "v2_clients_search",
        "path": "/api/v2/tenants/{partnerId}/clients/search",
        "description": "Search clients (MSP-only)",
        "msp_only": True,
    },
    {
        "name": "v2_clients_minimal",
        "path": "/api/v2/tenants/{partnerId}/clients/minimal",
        "description": "Minimal details of clients (MSP-only)",
        "msp_only": True,
    },
    {
        "name": "v2_users_search",
        "path": "/api/v2/tenants/{tenantId}/users/search",
        "description": "Search tenant users",
    },
    {
        "name": "v2_users_minimal",
        "path": "/api/v2/tenants/{tenantId}/users/minimal",
        "description": "Minimal details of users",
    },
    {
        "name": "v2_users_login_history",
        "path": "/api/v2/tenants/{tenantId}/users/loginHistory/search",
        "description": "Get user login history",
    },
    {
        "name": "v2_user_groups",
        "path": "/api/v2/tenants/{tenantId}/userGroups",
        "description": "Get user groups",
    },
    {
        "name": "v2_roles_search",
        "path": "/api/v2/tenants/{tenantId}/roles/search",
        "description": "Search roles",
    },
    {
        "name": "v2_permission_sets",
        "path": "/api/v2/tenants/{tenantId}/permissionSets",
        "description": "Get permission sets",
    },
    {
        "name": "v2_credential_sets_minimal",
        "path": "/api/v2/tenants/{clientId}/credentialSets/minimal",
        "description": "Minimal details of client credential sets",
    },
    {
        "name": "v2_client_notes_search",
        "path": "/api/v2/tenants/{tenantId}/notes/search",
        "description": "Search client notes (MSP-only)",
        "msp_only": True,
    },
    {
        "name": "v2_custom_branding",
        "path": "/api/v2/tenants/{tenantId}/customBranding",
        "description": "Get tenant custom branding",
    },

    # ╔══════════════════════════════════════════════════════════╗
    # ║                   V2 — CONFIG / REFERENCE DATA          ║
    # ╚══════════════════════════════════════════════════════════╝

    {
        "name": "v2_countries",
        "path": "/api/v2/cfg/countries",
        "description": "Get countries list",
    },
    {
        "name": "v2_timezones",
        "path": "/api/v2/cfg/timezones",
        "description": "Get timezones list",
    },
    {
        "name": "v2_nocs",
        "path": "/api/v2/cfg/tenants/nocs",
        "description": "Get tenant NOCs",
    },
    {
        "name": "v2_channels",
        "path": "/api/v2/cfg/tenants/channels",
        "description": "Get channels",
    },

    # ╔══════════════════════════════════════════════════════════╗
    # ║                   V2 — CLOUD RESOURCE TYPES             ║
    # ╚══════════════════════════════════════════════════════════╝

    {
        "name": "v2_resource_types_arm",
        "path": "/api/v2/tenants/{tenantId}/resourceTypes/ARM",
        "description": "Get ARM (Azure) cloud resource types",
    },
    {
        "name": "v2_resource_types_aws",
        "path": "/api/v2/tenants/{tenantId}/resourceTypes/AWS",
        "description": "Get AWS cloud resource types",
    },
    {
        "name": "v2_resource_types_google",
        "path": "/api/v2/tenants/{tenantId}/resourceTypes/GOOGLE",
        "description": "Get Google cloud resource types",
    },

    # ╔══════════════════════════════════════════════════════════╗
    # ║                   V2 — PATCHING                         ║
    # ╚══════════════════════════════════════════════════════════╝

    {
        "name": "v2_patches_search",
        "path": "/api/v2/tenants/{tenantId}/patches",
        "description": "Search patches",
    },
    {
        "name": "v2_patch_baselines",
        "path": "/api/v2/tenants/{tenantId}/patches/baselines",
        "description": "Get patch baselines",
    },
    {
        "name": "v2_patch_compliance",
        "path": "/api/v2/tenants/{tenantId}/patches/compliance",
        "description": "Get compliance checks",
    },
    {
        "name": "v2_patch_config_search",
        "path": "/api/v2/tenants/{tenantId}/patches/configurations/search",
        "description": "Search patch configurations",
    },
    {
        "name": "v2_resources_patches",
        "path": "/api/v2/tenants/{tenantId}/resources/patches",
        "description": "Get patches on resources",
    },

    # ╔══════════════════════════════════════════════════════════╗
    # ║                   V2 — REPORTING                        ║
    # ╚══════════════════════════════════════════════════════════╝

    {
        "name": "v2_reporting_apps",
        "path": "/api/v2/tenants/{tenantId}/reporting-apps/available/search",
        "description": "Search available reporting apps",
    },

    # ╔══════════════════════════════════════════════════════════╗
    # ║                   V2 — MANAGEMENT PROFILES              ║
    # ╚══════════════════════════════════════════════════════════╝

    {
        "name": "v2_mgmt_profiles_search",
        "path": "/api/v2/tenants/{tenantId}/managementProfiles/search",
        "description": "Search for management profiles",
    },

    # ╔══════════════════════════════════════════════════════════╗
    # ║                  V3 — RESOURCE MANAGEMENT               ║
    # ╚══════════════════════════════════════════════════════════╝

    # v3_topology_client removed - requires dynamic {resourceId} parameter
    {
        "name": "v3_topology_map_nodes",
        "path": "/graph/api/v3/tenants/{tenantId}/topology/map/nodes",
        "description": "Get all client level topology nodes",
    },
    {
        "name": "v3_topology_map_links",
        "path": "/graph/api/v3/tenants/{tenantId}/topology/map/links",
        "description": "Get all client level topology links",
    },
    {
        "name": "v3_topology_map_relationships",
        "path": "/graph/api/v3/tenants/{clientId}/topology/map/relationships",
        "description": "Get topology relationship data",
    },
    {
        "name": "v3_authz_tags",
        "path": "/api/v3/tenants/{clientId}/authzTags",
        "description": "Get authorization tags",
    },
    {
        "name": "v3_device_mgmt_policy_search",
        "path": "/api/v3/tenants/{tenantId}/resources/policies/search",
        "description": "Search device management policies (v3)",
    },
    # v3_service_maps POST removed - it's a CREATE endpoint, not a search

    # ╔══════════════════════════════════════════════════════════╗
    # ║                  V3 — METRICSQL                         ║
    # ╚══════════════════════════════════════════════════════════╝

    {
        "name": "v3_metricsql_metrics",
        "path": "/metricsql/api/v3/tenants/{tenantId}/metrics",
        "description": "Get metrics (MetricsQL — needs query param)",
        "params": {"query": "up"},
    },
    {
        "name": "v3_metricsql_labels",
        "path": "/metricsql/api/v3/tenants/{tenantId}/metrics/labels",
        "description": "Get metric labels",
    },
    # v3_metricsql_data POST removed - it's a WRITE endpoint (save timeseries), not a query

    # ╔══════════════════════════════════════════════════════════╗
    # ║                  V3 — LOG MANAGEMENT                    ║
    # ╚══════════════════════════════════════════════════════════╝

    {
        "name": "v3_logs_queries",
        "path": "/api/v3/tenants/{tenantId}/logs/queries",
        "description": "Query logs (POST required)",
        "method": "POST",
        "body": {
            "query": "{source = \"kubernetes\", k8s.namespace.name = \"dynamo-workload\"}",
            "fields": [],
            "limit": 1000,
            "start": 1770022800000000000,
            "end": 1770109200000000000
        }
    },

    # ╔══════════════════════════════════════════════════════════╗
    # ║                  V3 — ALERT DEFINITIONS                 ║
    # ╚══════════════════════════════════════════════════════════╝

    {
        "name": "v3_metric_alerts_queries",
        "path": "/alertdefinitions/api/v3/tenants/{tenantId}/metric-alerts/queries",
        "description": "Query metric alert definitions",
        "method": "POST",
        "body": {}
    },
    {
        "name": "v3_trace_alerts_queries",
        "path": "/alertdefinitions/api/v3/tenants/{tenantId}/trace-alerts/queries",
        "description": "Query trace alert definitions",
        "method": "POST",
        "body": {}
    },
    {
        "name": "v3_log_alerts_queries",
        "path": "/alertdefinitions/api/v3/tenants/{tenantId}/log-alerts/queries",
        "description": "Query log alert definitions",
        "method": "POST",
        "body": {}
    },

    # ╔══════════════════════════════════════════════════════════╗
    # ║                  V3 — OPSQL                             ║
    # ╚══════════════════════════════════════════════════════════╝

    {
        "name": "v3_opsql_queries",
        "path": "/opsql/api/v3/tenants/{tenantId}/queries",
        "description": "Run OpsQL query",
        "method": "POST",
        "body": {
            "objectType": "resource",
            "fields": ["id", "name", "type"],
            "pageNo": 1,
            "pageSize": 10
        }
    },

    # ╔══════════════════════════════════════════════════════════╗
    # ║                  V3 — MONITORING MANAGEMENT             ║
    # ╚══════════════════════════════════════════════════════════╝

    {
        "name": "v3_snmp_traps_search",
        "path": "/monitoring/api/v3/tenants/{tenantId}/snmp-traps/search",
        "description": "Search SNMP trap rules (MSP-only)",
        "msp_only": True,
    },

    # ╔══════════════════════════════════════════════════════════╗
    # ║                  V3 — DASHBOARDS                        ║
    # ╚══════════════════════════════════════════════════════════╝

    {
        "name": "v3_dashboard_collections",
        "path": "/dashboards/api/v3/collections",
        "description": "Get dashboard collections",
    },

]
