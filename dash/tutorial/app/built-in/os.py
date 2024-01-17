# os_functions.py
import os

def list_dir(path='.'):
    """
    List the contents of a directory.

    :param path: Path to the directory. Defaults to the current directory.
    :return: List of directory contents.
    """
    return os.listdir(path)

def change_dir(new_path):
    """
    Change the current working directory to a specified path.

    :param new_path: The path to change the current directory to.
    """
    try:
        os.chdir(new_path)
        print(f"Changed current directory to: {new_path}")
    except FileNotFoundError:
        print(f"The directory {new_path} does not exist")

def recursive_search(directory, extension):
    """
    Recursively search for files with a specific extension in a directory.

    :param directory: The directory to search in.
    :param extension: File extension to search for.
    :return: List of paths to files matching the extension.
    """
    matches = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                matches.append(os.path.join(root, file))
    return matches

def create_directory(path):
    """
    Create a new directory at the specified path.

    :param path: The path where the new directory will be created.
    """
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Directory {path} created successfully.")
    except OSError as error:
        print(f"Creation of the directory {path} failed: {error}")

def remove_directory(path):
    """
    Remove a directory at the specified path.

    :param path: The path of the directory to be removed.
    """
    try:
        os.rmdir(path)
        print(f"Directory {path} removed successfully.")
    except OSError as error:
        print(f"Removal of the directory {path} failed: {error}")

def get_current_working_directory():
    """
    Return the current working directory.
    """
    return os.getcwd()

def rename_file_or_directory(src, dest):
    """
    Rename a file or directory from src to dest.

    :param src: The current name of the file or directory.
    :param dest: The new name of the file or directory.
    """
    try:
        os.rename(src, dest)
        print(f"Renamed {src} to {dest}.")
    except OSError as error:
        print(f"Renaming {src} to {dest} failed: {error}")
