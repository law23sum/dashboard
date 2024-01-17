# list_files.py

import os


# Get the current working directory
current_directory = os.getcwd()

# Get a list of all files and directories in the current directory
files_and_directories = os.listdir(current_directory)

# Print all files and directories
for item in files_and_directories:
    print(item)
