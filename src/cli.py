# Handles command-line interface and user input

# The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to

import time

print("This is a task tracker, You can perform all these tasks::: \n")

available_actions = ['Add-Task', 'Update-Task', 'Delete-Task', 'List-all', 'Delete-all']

for available_action in available_actions:
    print(f"* {available_action}")

def accept_user_actions():
    user_action = input("\nwhat action do you want to perform ? ")
    return user_action


current_action = accept_user_actions()
print(current_action)