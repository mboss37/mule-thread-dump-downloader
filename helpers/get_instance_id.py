# helpers/get_environment_id.py
import requests
import json

# helpers/get_environment_id.py
import requests

def get_instance_id(bearer_token, environment_id, application_name):
    """
    Retrieves the instance ID of a specified application within a given environment.

    Args:
    bearer_token (str): The bearer token for authentication.
    environment_id (str): The ID of the environment.
    application_name (str): The name of the application.

    Returns:
    str: The instance ID of the running application instance.

    Raises:
    Exception: If no running instances are found or if there is an error in fetching the instance ID.
    """

    # Prepare the request headers with authorization and content type
    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Content-Type': 'application/json',
        'X-ANYPNT-ENV-ID': environment_id
    }

    # Construct the URL for the API request
    url = f"https://eu1.anypoint.mulesoft.com/cloudhub/api/v2/applications/{application_name}/deployments?orderByDate=DESC"

    # Make the GET request to the API
    response = requests.get(url, headers=headers)

    # Check if the response is successful (HTTP status code 200)
    if response.status_code == 200:
        deployments = response.json()['data']

        # Iterate through deployments
        for deployment in deployments:
            # Check if 'instances' key exists and is not empty
            if 'instances' in deployment and deployment['instances']:
                for instance in deployment['instances']:
                    # Check if the instance status is 'STARTED'
                    if instance['status'] == 'STARTED':
                        instance_id = instance['instanceId']
                        # Print instance ID
                        print("Instance ID: ", instance_id)
                        return instance_id

        raise Exception("No running instances found")
    else:
        raise Exception("Error fetching instance ID")