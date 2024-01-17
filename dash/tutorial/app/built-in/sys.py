# sys_functions.py
import sys
from io import StringIO

def print_python_version():
    """
    Print the currently running Python version.
    """
    print("Python version")
    print(sys.version)
    print("Version info.")
    print(sys.version_info)

def add_to_python_path(new_path):
    """
    Add a new path to the Python path at runtime.

    :param new_path: The path to add to the Python path.
    """
    if new_path not in sys.path:
        sys.path.append(new_path)
        print(f"Added {new_path} to PYTHONPATH")
    else:
        print(f"{new_path} is already in PYTHONPATH")

def capture_stdout(code_block):
    """
    Capture and return the standard output of a block of code.

    :param code_block: A string containing the code to execute.
    :return: Captured standard output as a string.
    """
    old_stdout = sys.stdout
    sys.stdout = buffer = StringIO()
    try:
        exec(code_block)
    finally:
        sys.stdout = old_stdout
    return buffer.getvalue()

def exit_program(status=0):
    """
    Exit the program with a given status code.

    :param status: Exit status code. Default is 0 (zero).
    """
    sys.exit(status)

def get_platform_info():
    """
    Return the name of the operating system dependent module imported.

    :return: The name of the platform.
    """
    return sys.platform

def get_python_executable_path():
    """
    Return the path to the Python executable.

    :return: Path to the Python executable.
    """
    return sys.executable

def get_command_line_arguments():
    """
    Return the list of command line arguments passed to a Python script.

    :return: List of command line arguments.
    """
    return sys.argv[1:]  # Excluding the script name itself
