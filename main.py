from helpers.get_bearer_token import retrieve_bearer_token 
from helpers.get_environment_id import get_environment_id
from helpers.get_instance_id import get_instance_id
from helpers.get_thread_dump import get_thread_dump
import argparse
from dotenv import load_dotenv
import os
from datetime import datetime

# Load variables from .env file
load_dotenv()

def setup_arg_parser():
    parser = argparse.ArgumentParser(description="Request Thread Dump for Application")
    parser.add_argument("--application_name", required=True, help="Name of the application")
    parser.add_argument("--environment", required=True, help="Environment name")
    return parser

def main():
    # Create the parser and parse arguments
    parser = setup_arg_parser()
    args = parser.parse_args()

    # Access the arguments
    application_name = args.application_name
    environment = args.environment

    # Retrieve the bearer token
    bearer_token = retrieve_bearer_token()

    try:
        environment_id = get_environment_id(bearer_token, environment)
        instance_id = get_instance_id(bearer_token, environment_id, application_name)
        thread_dump = get_thread_dump(application_name, environment_id, instance_id)

        # Define the directory to save the thread dump
        dump_dir = f"thread_dumps/{environment}"
        os.makedirs(dump_dir, exist_ok=True)

        # Create a unique filename for the thread dump
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{dump_dir}/{application_name}_{timestamp}.txt"

        # Write the thread dump to the file
        with open(filename, 'w') as file:
            file.write(thread_dump)
        print(f"Thread dump saved to {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
