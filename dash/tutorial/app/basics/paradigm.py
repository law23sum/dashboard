# This is a module-level docstring that describes the purpose and usage of the entire file or module.
"""This module provides generic functionality for demonstration purposes."""

# These are import statements where you can include other modules or libraries that your code depends on.
# Import statements

# Constants are variables whose values are not meant to change. They are usually written in uppercase.
CONSTANT_VALUE = "Hello, World!"

# Global variables are accessible throughout the module, outside and inside of functions or classes.
global_variable = []

# Definition of a function. Functions are reusable blocks of code that perform a specific task.
def generic_function(parameter1, parameter2):
    """Performs a generic operation and returns the result.

    Args:
        parameter1 (str): Description of parameter1.
        parameter2 (int): Description of parameter2.

    Returns:
        str: A formatted string combining parameter1 and parameter2.
    """
    # The function returns a formatted string combining the parameters.
    return f"{parameter1} has a value of {parameter2}"


# Definition of a class. Classes are blueprints for creating objects (a particular data structure).
class GenericClass:
    """A demonstration of a generic class in Python."""

    # Class variables are shared across all instances of the class.
    class_variable = "Class Variable Value"

    # The __init__ method is a special method called a constructor, used to initialize new objects.
    def __init__(self, instance_variable):
        # Instance variables are specific to each instance of the class.
        self.instance_variable = instance_variable

    # An instance method. It can access and modify object instance data.
    def instance_method(self):
        """A simple instance method."""
        return f"Value: {self.instance_variable}"

    # A class method. It's bound to the class rather than the object instance.
    @classmethod
    def class_method(cls):
        """A simple class method."""
        # 'cls' refers to the class itself and not an instance of the class.
        return cls.class_variable

    # A static method. It does not have access to 'self' or 'cls'. It behaves like a regular function.
    @staticmethod
    def static_method(parameter):
        """A simple static method."""
        return f"Static method called with {parameter}"


# This conditional statement checks if the file is being run as the main program.
if __name__ == "__main__":
    # If true, it executes the following block of code.
    print(generic_function("Age", 30))
    obj = GenericClass("Instance Value")
    print(obj.instance_method())
    print(GenericClass.class_method())
    print(GenericClass.static_method("Parameter Value"))