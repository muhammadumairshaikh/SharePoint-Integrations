import requests
from config.settings import GRAPH_BASE_URL, TIMEOUT
from services.site_id import get_sharepoint_site_id


def list_all_drives(access_token: str, site_id: str):
    """
    List all document libraries (drives) for the given SharePoint site.

    Parameters:
        access_token (str): Valid Microsoft Graph access token
        site_id (str): ID of the SharePoint site

    Returns:
        list: A list of drives (each as dict with name, id, etc.)
    """
    url = f"{GRAPH_BASE_URL}/sites/{site_id}/drives"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(url, headers=headers, timeout=TIMEOUT)
    response.raise_for_status()

    drives = response.json().get("value", [])

    if not drives:
        print(f"No drives found for this site: {site_id}")
        return []

    print(f"\nFound {len(drives)} available document libraries in site: {site_id}\n")
    # print("🧾 Available drives:\n")

    # for d in drives:
    #     print(f"   • Name: {d.get('name')}")
    #     print(f"     ID:   {d.get('id')}\n")

    return drives
