import requests
from config.settings import GRAPH_BASE_URL, TIMEOUT


def get_sharepoint_site_id(access_token: str, hostname: str, sitename: str) -> str:
    """Fetch the SharePoint Site ID using hostname and sitename."""
    url = f"{GRAPH_BASE_URL}/sites/{hostname}:/sites/{sitename}"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(url, headers=headers, timeout=TIMEOUT)
    response.raise_for_status()

    site_data = response.json()
    site_id = site_data.get("id")

    print(f" Site ID fetched successfully: {site_id}\n")
    return site_id
