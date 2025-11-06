import json
import requests
from datetime import datetime
from config.settings import GRAPH_BASE_URL
from services.list_drives import list_all_drives


def list_drive_items(access_token: str, site_id: str, drive_id: str):
    """
    List all items (files/folders) inside a specific drive.
    """
    url = f"{GRAPH_BASE_URL}/sites/{site_id}/drives/{drive_id}/root/children"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    return response.json().get("value", [])


def fetch_documents(access_token: str, site_id: str, output_file: str = "drive_documents.json"):
    """
    Fetch documents from all drives in a SharePoint site and save results to a JSON file.
    """
    drives = list_all_drives(access_token, site_id)

    if not drives:
        print(" No drives found in this site.")
        return

    data = {
        "site_id": site_id,
        "total_drives": len(drives),
        "drives": [],
        "fetched_at": datetime.utcnow().isoformat() + "Z"
    }

    for drive in drives:
        drive_name = drive.get("name")
        drive_id = drive.get("id")

        drive_info = {
            "drive_name": drive_name,
            "drive_id": drive_id,
            "documents": []
        }

        try:
            items = list_drive_items(access_token, site_id, drive_id)
        except requests.HTTPError as e:
            print(f" Failed to fetch items for drive '{drive_name}': {e}")
            continue

        for item in items:
            document = {
                "name": item.get("name"),
                "type": "folder" if "folder" in item else "file",
                "webUrl": item.get("webUrl"),
                "lastModifiedDateTime": item.get("lastModifiedDateTime")
            }
            drive_info["documents"].append(document)

        data["drives"].append(drive_info)

    # Save all results to JSON file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f" Drive document details saved successfully to '{output_file}'.")
