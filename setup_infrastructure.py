import os
import subprocess

# Define the users and their respective groups
users = {
    "Andrew": "System_Administrator",
    "Julius": "Legal",
    "Chizi": "Human_Resource_Manager",
    "Jeniffer": "Sales_Manager",
    "Adeola": "Business_Strategist",
    "Bach": "CEO",
    "Gozie": "IT_intern",
    "Ogochukwu": "Finance_Manager"
}

# Define the directories to be created
directories = [
    "Finance Budgets",
    "Contract Documents",
    "Business Projections",
    "Business Models",
    "Employee Data",
    "Company Vision and Mission Statement",
    "Server Configuration Script"
]

# Base path where directories will be created
base_path = os.path.expanduser("~/assignment/pTask_4")

def create_group(group):
    """
    Create a group if it doesn't already exist.
    """
    try:
        subprocess.run(["sudo", "groupadd", group], check=True, stderr=subprocess.DEVNULL)
        print(f"Group '{group}' created.")
    except subprocess.CalledProcessError as e:
        if e.returncode == 9:  # Group already exists
            print(f"Group '{group}' already exists.")
        else:
            print(f"Error creating group '{group}': {e}")

def create_user(username, group):
    """
    Create a user and assign them to a group.
    """
    try:
        create_group(group)
        subprocess.run(["sudo", "useradd", "-m", "-G", group, username], check=True)
        print(f"User '{username}' created and added to group '{group}'.")
    except subprocess.CalledProcessError as e:
        if e.returncode == 9:  # User already exists
            print(f"User '{username}' already exists.")
        else:
            print(f"Error creating user '{username}' or group '{group}': {e}")

def create_directories(base_path, dir_list):
    """
    Create directories from the given list under the base path.
    """
    for directory in dir_list:
        path = os.path.join(base_path, directory)
        try:
            os.makedirs(path, exist_ok=True)
            if os.path.exists(path):
                print(f"Directory '{path}' already exists.")
            else:
                print(f"Directory '{path}' created.")
        except OSError as e:
            print(f"Error creating directory '{path}': {e}")

def create_file_in_directory(base_path, dir_list):
    """
    Take user input to create a file in the specified directory.
    """
    file_name = input("Enter the name of the file to create: ")
    directory = input("Enter the directory to create the file in: ")

    if directory in dir_list:
        file_path = os.path.join(base_path, directory, file_name)
        try:
            with open(file_path, 'w') as file:
                file.write("")  # Create an empty file
            print(f"File '{file_path}' created.")
        except OSError as e:
            print(f"Error creating file '{file_path}': {e}")
    else:
        print(f"Directory '{directory}' does not exist. File not created.")

if __name__ == "__main__":
    # Create users and assign them to groups
    for user, group in users.items():
        create_user(user, group)

    # Create company directories
    create_directories(base_path, directories)

    # Create a file in the specified directory based on user input
    create_file_in_directory(base_path, directories)


