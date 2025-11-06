import msal
from config.settings import CLIENT_ID, CLIENT_SECRET, AUTHORITY, SCOPE


def get_access_token():
    """
    Authenticate with MSAL using client 
    credentials and return access token.
    """

    app = msal.ConfidentialClientApplication(
        client_id=CLIENT_ID,
        client_credential=CLIENT_SECRET,
        authority=AUTHORITY
    )

    # Try silent token first (cached)
    result = app.acquire_token_silent(SCOPE, account=None)

    if not result:
        result = app.acquire_token_for_client(scopes=SCOPE)

    if "access_token" in result:
        print(" Access Token acquired successfully!\n")
        # print(result)
        return result["access_token"]
    
    raise Exception(f"Token acquisition failed:\n{result.get('error_description', 'Unknown error')}")
