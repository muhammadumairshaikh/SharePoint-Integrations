from dotenv import dotenv_values

config = dotenv_values(".env")

CLIENT_ID = config["CLIENT_ID"]
CLIENT_SECRET = config["CLIENT_SECRET"]
TENANT_ID = config["TENANT_ID"]

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"

# Microsoft Graph scope
SCOPE = ["https://graph.microsoft.com/.default"]


HOSTNAME = config.get("HOSTNAME")
SITENAME = config.get("SITENAME")
# DRIVE_NAME = config["DRIVE_NAME"]

GRAPH_BASE_URL = "https://graph.microsoft.com/v1.0"

TIMEOUT = 15