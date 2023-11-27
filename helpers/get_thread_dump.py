# helpers/get_thread_dump.py
import requests
import os
from requests.auth import HTTPBasicAuth

def get_thread_dump(application_name, environment_id, instance_id):
    """
    Retrieves the thread dump of a specified application instance.

    Args:
    application_name (str): The name of the application.
    environment_id (str): The ID of the environment.
    instance_id (str): The ID of the application instance.

    Returns:
    str: The thread dump of the application instance.

    Raises:
    Exception: If there is an error in fetching the thread dump.
    """
    
    # Retrieve username and password from environment variables
    username = os.getenv("CLOUDHUB_USERNAME")
    password = os.getenv("CLOUDHUB_PASSWORD")

    # Check if username and password are available
    if not username or not password:
        raise Exception("Username or password not set in environment variables")

    # Prepare the request headers
    headers = {
        'X-ANYPNT-ENV-ID': environment_id
    }

    # Construct the URL for the API request to get the thread dump
    url = f"https://eu1.anypoint.mulesoft.com/cloudhub/api/v2/applications/{application_name}/instances/{instance_id}/diagnostics"

    # Print the request URL
    print(f'Requesting Thread Dump for application: {application_name}, instance: {instance_id}')

          
    # Make the GET request to the API using Basic Authentication
    response = requests.get(url, auth=HTTPBasicAuth(username, password), headers=headers)

    # Check if the response is successful (HTTP status code 200)
    if response.status_code == 200:
        # Return the thread dump text
        return response.text
    else:
        # Raise an exception if the response status code is not 200
        raise Exception(f"Error fetching thread dump: {response.status_code} - {response.text}")