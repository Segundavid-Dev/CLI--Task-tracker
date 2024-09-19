# Handles file operations (reading/writing from/to the tasks file)
import json
import cli 
import task_manager



#filepath
filename1 = 'tasks\Task.json'

# Write task to JSON
def write_task_to_json():
    with open(filename1, 'w') as file:
        json.dump(task_manager.dict_tasks, file, indent=4)


write_json = write_task_to_json()


#read task from JSON
# def read_from_json():
#     with open(filename1, 'r') as file:
#         file.read()