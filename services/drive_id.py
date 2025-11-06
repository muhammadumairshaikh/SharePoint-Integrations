# import requests
# from config.settings import GRAPH_BASE_URL, DRIVE_NAME


# def get_drive_id_by_name(access_token: str, site_id: str) -> str:
#     """Fetch drive ID for a given site by drive (document library) name."""
#     url = f"{GRAPH_BASE_URL}/sites/{site_id}/drives"
#     headers = {"Authorization": f"Bearer {access_token}"}

#     response = requests.get(url, headers=headers)
#     response.raise_for_status()

#     drives = response.json().get("value", [])
#     if not drives:
#         raise Exception("No drives found for this site!")

#     for drive in drives:
#         if drive.get("name") == DRIVE_NAME:
#             drive_id = drive.get("id")
#             # print(f" Drive '{DRIVE_NAME}' found with ID: {drive_id}\n")
#             return drive_id

#     raise Exception(f"Drive named '{DRIVE_NAME}' not found in site {site_id}")
