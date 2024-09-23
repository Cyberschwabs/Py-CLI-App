import json
import typer, logging, os, requests
import msal
from alive_progress import alive_bar
from dotenv import load_dotenv
from typing_extensions import Annotated

def login_to_azure():
    load_dotenv(".env")

    client_id = os.getenv('AZURE_CLIENT_ID')
    client_secret = os.getenv('AZURE_CLIENT_SECRET')
    tenant_id = os.getenv('AZURE_TENANT_ID')
    authority = f"https://login.microsoftonline.com/{tenant_id}"
    scope = ['https://graph.microsoft.com/.default']

    cliapp = msal.ConfidentialClientApplication(
        client_id=client_id,
        client_credential=client_secret,
        authority=authority
    )

    token_result = cliapp.acquire_token_silent(scopes=scope, account=None)
    if not token_result:
        logging.info("No suitable token exists in cache. Let's get a new one from Azure AD.")
        token_result = cliapp.acquire_token_for_client(scopes=scope)

    global token
    token = token_result.get("access_token")

app = typer.Typer()

# Get Azure AD User by UPN
@app.command()
def getuserdetails(upn: Annotated[str, typer.Option(prompt=True)]):
    with alive_bar(120000) as bar:
        print('Getting user: ' + f'{upn}')

        base_url = 'https://graph.microsoft.com/v1.0/'
        endpoint = f'users/{upn}'
        access_token = token
        headers = {
        'Authorization': access_token
        }

        graph_result = requests.get(url=f"{base_url + endpoint}", headers=headers)
        result = json.dumps(graph_result.json(), indent=4)
        print(result)
        bar()


@app.command()


@app.command()


@app.command()


# Create New Folder Directory
@app.command()
def createfolder(parent_dir: Annotated[str, typer.Option(prompt=True)],
                        directory: Annotated[str, typer.Option(prompt=True)]):
    print(f'{parent_dir}' + ' ' + f'{directory}' + ' Will be created!')
    newdirectory = os.path.join(parent_dir, directory)
    os.mkdir(newdirectory)


if __name__ == "__main__":
    login_to_azure()
    app()