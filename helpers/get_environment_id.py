# helpers/get_environment_id.py
import requests
import os
import json

def get_environment_id(bearer_token, environment):

    organization_id = os.getenv("ORGANIZATION_ID")
    
    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Content-Type': 'application/json'
    }
    url = f"https://eu1.anypoint.mulesoft.com/accounts/api/organizations/{organization_id}/environments"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        environments = response.json()['data']

        # Find the DEV environment and print its ID
        for env in environments:
            if env['name'] == environment:
                dev_env_id = env['id']
                print(f"DEV Environment ID: {dev_env_id}")
                return dev_env_id

    else:
        raise Exception("Error fetching environment ID")
