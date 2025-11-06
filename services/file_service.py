# import requests
# from config.settings import GRAPH_BASE_URL, TIMEOUT


# def list_drive_items(access_token: str, site_id: str, drive_id: str):
#     """List all items (files/folders) in the root of the drive."""
#     url = f"{GRAPH_BASE_URL}/sites/{site_id}/drives/{drive_id}/root/children"
#     headers = {"Authorization": f"Bearer {access_token}"}

#     response = requests.get(url, headers=headers, timeout= TIMEOUT)
#     response.raise_for_status()

#     items = response.json().get("value", [])

#     if not items:
#         print("⚠️ No items found in this drive.")
#         return []

#     print("📄 Documents and folders in this drive:\n")
#     for item in items:
#         name = item.get("name")
#         item_type = "📁 Folder" if "folder" in item else "📄 File"
#         web_url = item.get("webUrl")
#         print(f"{item_type} | {name} | {web_url}")

#     return items

import os
import requests
import webbrowser
from config.settings import GRAPH_BASE_URL, TIMEOUT
from services.list_drives import list_all_drives


def get_drive_id_by_name(access_token: str, site_id: str, drive_name: str) -> str:
    """Get the ID of a specific drive by its name."""
    drives = list_all_drives(access_token, site_id)

    for drive in drives:
        if drive.get("name").lower() == drive_name.lower():
            return drive.get("id")

    raise Exception(f"❌ Drive named '{drive_name}' not found in site {site_id}")


def list_items_in_drive(access_token: str, site_id: str, drive_id: str):
    """List all items (files/folders) inside a specific drive."""
    url = f"{GRAPH_BASE_URL}/sites/{site_id}/drives/{drive_id}/root/children"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(url, headers=headers, timeout=TIMEOUT)
    response.raise_for_status()

    return response.json().get("value", [])


def download_file(access_token: str, site_id: str, drive_id: str, item_id: str, file_name: str):
    """Download a file from a drive using its item ID."""
    url = f"{GRAPH_BASE_URL}/sites/{site_id}/drives/{drive_id}/items/{item_id}/content"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(url, headers=headers, timeout=TIMEOUT)
    response.raise_for_status()

    os.makedirs("downloads", exist_ok=True)
    file_path = os.path.join("downloads", file_name)

    with open(file_path, "wb") as f:
        f.write(response.content)

    print(f"📥 File downloaded successfully: {file_path}")
    return file_path


def fetch_drive_documents(access_token: str, site_id: str, drive_name: str, target_file: str = None):
    """
    Fetch documents from a specific drive in a SharePoint site.
    If target_file is given, fetch that file's metadata and download it.
    """
    drive_id = get_drive_id_by_name(access_token, site_id, drive_name)
    print(f"\n📁 Drive found: '{drive_name}' (ID: {drive_id})")

    items = list_items_in_drive(access_token, site_id, drive_id)

    if not items:
        print("⚠️ No documents found in this drive.")
        return

    if target_file:
        print(f"\n🔍 Searching for file: '{target_file}' ...")
        found = next((item for item in items if item.get("name").lower() == target_file.lower()), None)

        if found:
            print("\n✅ File found!\n")
            print(f" Name: {found.get('name')}")
            print(f" Type: {'Folder' if 'folder' in found else 'File'}")
            print(f" Web URL: {found.get('webUrl')}")
            print(f" Last Modified: {found.get('lastModifiedDateTime')}")

            # ✅ Open file in browser
            web_url = found.get("webUrl")
            if web_url:
                print("\n🌐 Opening file in browser...")
                webbrowser.open(web_url)

            # ✅ Download file to local system
            if "file" in found:  # only download if it's a file, not folder
                download_file(
                    access_token,
                    site_id,
                    drive_id,
                    found.get("id"),
                    found.get("name")
                )
            else:
                print("⚠️ The selected item is a folder, not a file.")
        else:
            print(f"❌ File '{target_file}' not found in drive '{drive_name}'.")
        return

    # If no specific file requested, print all documents
    print(f"\n📄 Documents in '{drive_name}':\n")
    for item in items:
        item_type = "📁 Folder" if "folder" in item else "📄 File"
        print(f"{item_type}  {item.get('name')}  →  {item.get('webUrl')}")
