# Import the os module to access operating system interface functions,
# specifically used here to retrieve environment variables
import os
from dotenv import load_dotenv
import requests


load_dotenv()
access_token = os.getenv('ACCESS_TOKEN')


url = f"https://api.extremecloudiq.com/locations/tree"
headers = {'Authorization': f'Bearer {access_token}'}
params = {'expandChildren': 'true'}

# parentId: {{loc_id}} (disabled)

response = requests.get(url, headers=headers, params=params)

print("Status Code:", response.status_code)

content_type = response.headers.get('Content-Type')
if content_type and 'application/json' in content_type:
    try:
        print("Response Body:", response.json())
        # write the response to a file
        with open('data/location-tree.json', 'w') as f:
            import json
            json.dump(response.json(), f, indent=2)
        print("Response written to data/location-tree.json")
    except ValueError:
        print("Response is not valid JSON")
else:
    print("Content-Type is not application/json")
    print(response.text)