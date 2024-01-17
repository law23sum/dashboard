import json
from pathlib import Path

path = Path('responses.json')
contents = path.read_text()
responses = json.loads(contents)

num_responses = len(responses)
print(f"Found {num_responses:,} responses.")

# Find the unique responses.
unique_responses = []
for response in responses:
    if response not in unique_responses:
        unique_responses.append(response)

num_unique = len(unique_responses)
print(f"Found {num_unique} unique responses.")
print(unique_responses)
