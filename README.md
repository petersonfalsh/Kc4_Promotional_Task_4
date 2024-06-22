# Kc4_Promotional_Task_4

# Infrastructure Setup Script

This project contains a Python script to automate the creation of users and directories for a small business. 

## Features

- Creates specified users and assigns them to appropriate groups.
- Creates specified directories within a base path.
- Includes functionality to create a file based on user input in specified directories.
- Ensures directories are only created if they do not already exist.


## Prerequisites

- Unix-like operating system (Linux or macOS)
- Python 3
- `sudo` privileges to create users and groups

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Ensure the script has executable permissions:**

    ```bash
    chmod +x setup_infrastructure.py
    ```

## Usage

1. **Run the script:**

    ```bash
    sudo python3 setup_infrastructure.py
    ```

2. **Follow the prompts to create a file:**

    - Enter the name of the file to create.
    - Enter the directory to create the file in (must be one of the predefined directories).

## Script Details

### Users and Groups

The following users will be created and assigned to their respective groups:

- **Andrew**: System_Administrator
- **Julius**: Legal
- **Chizi**: Human_Resource_Manager
- **Jeniffer**: Sales_Manager
- **Adeola**: Business_Strategist
- **Bach**: CEO
- **Gozie**: IT_intern
- **Ogochukwu**: Finance_Manager

### Directories

The following directories will be created under the specified base path (`~/assignment/pTask_4`):

- Finance Budgets
- Contract Documents
- Business Projections
- Business Models
- Employee Data
- Company Vision and Mission Statement
- Server Configuration Script

### File Creation

The script includes a feature to take user input to create a file. The file will only be created if the directory name is one of the predefined company directories.

