# helpers/get_log_file.py
import requests
import os
from requests.auth import HTTPBasicAuth

def get_log_file(application_name, environment_id, instance_id):
    """
    Retrieves the log file of a specified application instance.

    Returns:
    str: The log file of the application instance.

    Raises:
    Exception: If there is an error in fetching the log file.
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

    # Construct the URL for the API request to get the log file
    url = f"https://eu1.anypoint.mulesoft.com/cloudhub/api/v2/applications/{application_name}/instances/{instance_id}/log-file"

    # Print the request URL
    print(f'Requesting log file for application: {application_name}, instance: {instance_id}')

          
    # Make the GET request to the API using Basic Authentication
    response = requests.get(url, auth=HTTPBasicAuth(username, password), headers=headers)

    # Check if the response is successful (HTTP status code 200)
    if response.status_code == 200:
        # Return the log file text
        return response.text
    else:
        # Raise an exception if the response status code is not 200
        raise Exception(f"Error fetching log file: {response.status_code} - {response.text}")