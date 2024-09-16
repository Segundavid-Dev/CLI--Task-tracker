# Handles file operations (reading/writing from/to the tasks file)
import json
import cli as cli
cli.accept_user_actions()


#filepath
filename1 = 'tasks\Task.json'

#Read from the JSON file to validate task amount
def validate_taskJson(filename1):
    with open(filename1, 'r') as file:
        json_validate = json.load(file)
    return json_validate


data = validate_taskJson(filename1)
print(data)

# Write task to JSON