# json_template_generator.py

import json


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

# Get user input for filename
filename = input("Please enter a filename for the output JSON file: ")

# Append .json if not already included in filename
if not filename.endswith(".json"):
    filename += ".json"

# Write the root object to a JSON file
with open(filename, 'w') as json_file:
    json.dump(root_object, json_file, indent=4)

print(f"JSON output has been written to {filename}")
