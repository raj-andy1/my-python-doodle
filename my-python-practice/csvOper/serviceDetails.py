import pandas as pd


servicesList = ["hot-escalation",
"bxp-deploy-bot",
"dcp-spike-mesh-expansion",
"ci-analyzer",
"admin-api-token-management",
"cronman",
"security_issue_metrics",
"caas-explorations",
"app-host-functions",
"reka-public",
"atlas-backfill-refresh-ui",
"atlassian-directory-elasticsearch",
"faiss-docker",
"dcp-spike-mesh-expansion",
"dt-usage-tracker",
"jira-migration-target",
"jira-np-ingestion",
"jira-np-ingestion",
"jrebel-license-server",
"martech-uploadhub",
"open-summit",
"pf-site-admin-ui",
"seta-shard-event-listener",
"seta-gsac-anodot-forwarder",
"shpxlvi2",
"status-page-infra-pgbouncer",
"status-page-infra-varnish",
"statuspage-edge",
"viceroy-e2e-test",
"voltron-dqi",
"xpsearch-content",
"bbc-varnish",
"bbc-datarainbow",
"bbc-gev2"]

csvFile = "ServiceInsights.csv"
try:
    df = pd.read_csv(csvFile, low_memory=False)
    filtered_result = df[df['Service ID'].isin(servicesList)].reset_index(drop=True)
    filtered_result.to_csv('ServiceInsightsFiltered.csv', index=False)
except Exception as e:
    print(f"Error: {e}")


