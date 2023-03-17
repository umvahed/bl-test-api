import requests
import json

base_url = "https://<your.blackduck.hub.instance>/api/"

# Authenticate with the Blackduck Hub API
auth = ("api_token", "<your_api_token_here>")

# Make a GET request to the API endpoint for components in the knowledge base
kb_url = base_url + "components?inKnowledgeBase=true&limit=1000"

# Send the GET request with authentication headers
response = requests.get(kb_url, auth=auth)

# Check if the response was successful
if response.status_code == 200:
    # Parse the JSON data from the response
    data = json.loads(response.content)

    # Loop through the components in the knowledge base and print their names
    for component in data['items']:
        print(component['name'])
else:
    # Print an error message if the request was unsuccessful
    print("Failed to retrieve components from knowledge base: ", response.status_code)
