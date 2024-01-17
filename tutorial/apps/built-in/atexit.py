# atexit_functions.py
import atexit

def goodbye():
    """
    Print a goodbye message.
    """
    print("Goodbye, the program is ending!")

def cleanup_action():
    """
    Perform a cleanup action, e.g., close files or release resources.
    """
    print("Cleaning up resources...")

def log_exit_time():
    """
    Log the time at which the program exits.
    """
    from datetime import datetime
    print(f"Program exited at: {datetime.now()}")

def save_program_state():
    """
    Save the program's state or data at exit.
    """
    # Placeholder for saving state
    print("Saving program state...")

def complex_cleanup():
    """
    Perform a complex cleanup task.
    """
    # Placeholder for complex cleanup actions
    print("Performing complex cleanup tasks...")

def register_functions():
    """
    Register functions to be called upon normal program termination.
    """
    atexit.register(goodbye)
    atexit.register(cleanup_action)
    atexit.register(log_exit_time)
    atexit.register(save_program_state)
    atexit.register(complex_cleanup)

# Register functions for atexit
register_functions()
