import requests
import json

base_url = "https://<your blackduck hub url>/api"

username = "<your username>"
password = "<your password>"

# Create an authentication token for the API
auth_token = requests.post(base_url + "/tokens/authenticate",
    auth=(username, password)).json().get('bearerToken')

# Set headers for all requests
headers = {
    'Authorization': 'Bearer ' + auth_token,
    'Accept': 'application/json'
}

# Get all knowledge base components
components_url = base_url + "/components?limit=1000&q=kbComponent:true&sort=-createdAt"
response = requests.get(components_url, headers=headers)

# Print component name and version
if response.status_code == 200:
    components = json.loads(response.content)
    for component in components.get('items', []):
        print(component.get('name', 'Unknown Name'))
else:
    print("Failed to retrieve components, status code: ", response.status_code)

This script authenticates the user with their username and password, retrieves an authentication token, and uses that token in subsequent requests. It then retrieves all knowledge base components by making a GET request to the /components endpoint with a query parameter q=kbComponent:true to filter out non-knowledge base components. Finally, it prints the name of each knowledge base component to the console.

Note that the limit parameter in the request URL is set to 1000, which limits the number of results returned to 1000. If there are more than 1000 knowledge base components, you may need to modify this parameter or add pagination logic to retrieve all components.