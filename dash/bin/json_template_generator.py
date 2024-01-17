# json_template_generator.py

import json
import os


# Prompt the user for the number of objects and properties
num_objects = int(input("Enter the number of objects: "))
num_properties = int(input("Enter the number of properties per object: "))

# Initialize the root object and the array of objects
root_object = {}
array_of_objects = []

# Generate the objects
for i in range(num_objects):
    obj = {}
    for j in range(num_properties):
        # Using generic names and values for properties
        obj[f"property{j + 1}"] = f"value{i + 1}-{j + 1}"
    array_of_objects.append(obj)

# Add the array of objects to the root object
root_object["array_of_objects"] = array_of_objects

# Get user input for output directory
directory_path = input(
    "Please enter the directory path for the output JSON file: "
    )

# Check if the directory exists, if not create it
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

# Get user input for filename
filename = input("Please enter a filename for the output JSON file: ")

# Append .json if not already included in filename
if not filename.endswith(".json"):
    filename += ".json"

# Join the directory path and filename
full_path = os.path.join(directory_path, filename)

# Write the root object to a JSON file
with open(full_path, 'w') as json_file:
    json.dump(root_object, json_file, indent=4)

print(f"JSON output has been written to {full_path}")
