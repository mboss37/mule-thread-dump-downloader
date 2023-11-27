from helpers.get_bearer_token import retrieve_bearer_token 
from helpers.get_environment_id import get_environment_id
from helpers.get_instance_id import get_instance_id
from helpers.get_thread_dump import get_thread_dump
from helpers.get_log_file import get_log_file
from dotenv import load_dotenv
import os
from datetime import datetime

# Load variables from .env file
load_dotenv()

def download_thread_dump():
    # Get the application name and environment from the user
    application_name = input("Enter the application name: ")
    environment = input("Enter the environment (DEV, INT, EDU or PROD): ")

    # Retrieve the bearer token
    bearer_token = retrieve_bearer_token()

    try:
        environment_id = get_environment_id(bearer_token, environment)
        instance_id = get_instance_id(bearer_token, environment_id, application_name)
        
        # Retrieve the thread dump
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

def download_log_file():
    # Get the application name and environment from the user
    application_name = input("Enter the application name: ")
    environment = input("Enter the environment (DEV, INT, EDU or PROD): ")

    # Retrieve the bearer token
    bearer_token = retrieve_bearer_token()

    try:
        environment_id = get_environment_id(bearer_token, environment)
        instance_id = get_instance_id(bearer_token, environment_id, application_name)
        
        # Retrieve the log file
        log_file = get_log_file(application_name, environment_id, instance_id)

        # Define the directory to save the log file
        log_dir = f"log_files/{environment}"
        os.makedirs(log_dir, exist_ok=True)

        # Create a unique filename for the log file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{log_dir}/{application_name}_{timestamp}.txt"

        # Write the log to the file
        with open(filename, 'w') as file:
            file.write(log_file)
        print(f"Thread dump saved to {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    print("Select the feature you want to use:")
    print("1: Download Thread Dump")
    print("2: Download Log File")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        download_thread_dump()
    elif choice == '2':
        download_log_file()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()