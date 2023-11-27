# helpers/get_bearer_token.py
import requests
import os

def retrieve_bearer_token():
    username = os.getenv("CLOUDHUB_USERNAME")
    password = os.getenv("CLOUDHUB_PASSWORD")

    data = {'username': username, 'password': password}
    headers = {'Content-Type': 'application/json'}

    response = requests.post("https://eu1.anypoint.mulesoft.com/accounts/login", json=data, headers=headers)

    if response.status_code == 200:
        bearer_token = response.json().get('access_token')
        if bearer_token:
            # Print the bearer token to the console
            print("Bearer Token: " ,bearer_token)
            
            # Return the bearer token
            return bearer_token
        else:
            raise Exception("Bearer token not found in the response.")
    else:
        raise Exception(f"Failed to retrieve bearer token, status code: {response.status_code}")
