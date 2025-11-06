from auth.msal_auth import get_access_token
from config.settings import HOSTNAME, SITENAME
from services.site_id import get_sharepoint_site_id
# from services.list_drives import list_all_drives
# from services.drive_id import get_drive_id_by_name
# from services.file_service import list_drive_items
# from services.fetch_drive_docs import fetch_documents
from services.fetch_specific_drive import fetch_drive_documents


def main():
    token = get_access_token()
    site_id = get_sharepoint_site_id(token, HOSTNAME, SITENAME)
    # list_all_drives(token, site_id)
    # drive_id = get_drive_id_by_name(token, site_id)
    # list_drive_items(token, site_id, drive_id)
    # fetch_documents(token, site_id)
    fetch_drive_documents(token, site_id, drive_name="Documents", target_file="- Master Services Agreement.docx")


if __name__ == "__main__":
    main()
