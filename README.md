md
# SharePoint-Integrations

## Overview

This repository contains Python scripts for interacting with Microsoft SharePoint using the Microsoft Graph API. It provides functionalities to authenticate, fetch site information, list drives, retrieve documents, and more. This integration allows for programmatic access and management of SharePoint resources.

## Key Features & Benefits

*   **Authentication:** Securely authenticates with SharePoint using MSAL (Microsoft Authentication Library).
*   **Site Information Retrieval:** Fetches SharePoint site ID using the site URL.
*   **Drive Listing:** Lists all drives (document libraries) within a specified SharePoint site.
*   **Document Retrieval:** Retrieves documents from specific drives.
*   **Configurable:** Utilizes environment variables for easy configuration of credentials and settings.

## Prerequisites & Dependencies

Before you begin, ensure you have the following installed:

*   **Python:** Version 3.6 or higher
*   **pip:** Python package installer
*   **pdm:** Package manager ([https://pdm.fming.dev/](https://pdm.fming.dev/))
*   **Microsoft Azure Account:**  Required for creating an App Registration and obtaining necessary credentials.

The project depends on the following Python packages:

*   `msal`
*   `python-dotenv`
*   `requests`

These dependencies are managed by `pdm`.

## Installation & Setup Instructions

1.  **Clone the Repository:**

    ```bash
    git clone git@github.com:muhammadumairshaikh/SharePoint-Integrations.git
    cd SharePoint-Integrations
    ```

2.  **Install PDM:**

    If you don't have PDM installed, install it using pip:

    ```bash
    pip install pdm
    ```

3.  **Initialize PDM:**

    Navigate to the project directory in your terminal and initialize PDM:

    ```bash
    pdm init
    ```

    Choose the appropriate options, ensuring that you create a virtual environment.

4.  **Install Dependencies:**

    Install the project dependencies using PDM:

    ```bash
    pdm install
    ```

5.  **Configure Environment Variables:**

    Create a `.env` file in the project's root directory and populate it with the following variables:

    ```
    CLIENT_ID=<YOUR_CLIENT_ID>
    CLIENT_SECRET=<YOUR_CLIENT_SECRET>
    TENANT_ID=<YOUR_TENANT_ID>
    HOSTNAME=<YOUR_SHAREPOINT_HOSTNAME>
    SITENAME=<YOUR_SHAREPOINT_SITENAME>
    ```

    Replace the placeholders with your actual Azure App Registration details and SharePoint information.  Obtain these from your Azure portal.  Specifically:
    * **CLIENT_ID:** The Application (client) ID from your App Registration.
    * **CLIENT_SECRET:**  The Client Secret you created for your App Registration.  Store securely.
    * **TENANT_ID:** The Directory (tenant) ID from your Azure Active Directory.
    * **HOSTNAME:**  The hostname of your SharePoint site (e.g., `yourtenant.sharepoint.com`).
    * **SITENAME:** The name of the site within your SharePoint host (e.g., `yoursite`).

6.  **Azure App Registration Permissions:**

    Ensure your Azure App Registration has the necessary Microsoft Graph API permissions. The application needs the following **Application permissions**:

    *   `Sites.Read.All`
    *   `Files.Read.All`

    Grant admin consent to these permissions after adding them to your App Registration.

## Usage Examples

Here's how to use the main script to fetch information:

```python
from auth.msal_auth import get_access_token
from config.settings import HOSTNAME, SITENAME
from services.site_id import get_sharepoint_site_id
from services.fetch_specific_drive import fetch_drive_documents


def main():
    token = get_access_token()
    site_id = get_sharepoint_site_id(HOSTNAME, SITENAME, token)
    if site_id:
        print(f"Site ID: {site_id}")
        # Example: Fetch documents from a specific drive
        fetch_drive_documents(token, site_id)
    else:
        print("Failed to retrieve site ID.")


if __name__ == "__main__":
    main()
```

This script first obtains an access token, then retrieves the site ID, and then can be modified to call other services to interact with SharePoint.  Ensure you have set the environment variables as specified in the Installation section.

## Configuration Options

The project utilizes environment variables defined in the `.env` file to configure various settings:

| Variable      | Description                                                     |
|---------------|-----------------------------------------------------------------|
| `CLIENT_ID`   | The Client ID of the Azure App Registration.                 |
| `CLIENT_SECRET`| The Client Secret of the Azure App Registration.              |
| `TENANT_ID`   | The Tenant ID of your Azure Active Directory.                |
| `HOSTNAME`    | The hostname of your SharePoint site.                         |
| `SITENAME`    | The name of the specific site within your SharePoint host.   |

## Contributing Guidelines

Contributions are welcome! To contribute to this project, follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Implement your changes.
4.  Submit a pull request with a clear description of your changes.

## License Information

This project does not currently have a specified license.  All rights are reserved by the owner.

## Acknowledgments

*   This project leverages the `msal` library for authentication with Microsoft Azure.
*   Uses `python-dotenv` to handle configuration through environment variables.