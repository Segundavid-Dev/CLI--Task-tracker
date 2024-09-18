# Core logic for managing tasks (add, Delete, update, list, etc.)
import time
from cli import accept_user_actions
from cli import current_action

task1 = 'Add-Task'
task2 = 'Update-Task'
task3 = 'Delete-Task'
task4 = 'List-all'
task5 = 'Delete-all'

# validate user action
list_tasks = [task1, task2, task3, task4, task5]
dict_tasks = {}
more_dict_tasks = {}

def add_task():
    if current_action == task1:
        print("Executing add Task functionality...")
        time.sleep(1)
        # Adding initial task
        add_task1 = input("Input your task: ")

        dict_tasks[0] = add_task1
        print(dict_tasks)
        time.sleep(0.5)

        print("Task added successfully...")
        time.sleep(0.5)

        counter = len(dict_tasks) #starts from the current length of the task dictionary
        verifying_adding_tasks = input("Do you want to add more task? (Y for yes, N for no): ")

        if verifying_adding_tasks.upper() == 'Y':
            amount_of_task = int(input("Enter number of task to be added: "))

            for _ in range(amount_of_task):
                more_task_input = input("Enter more task: ")
                dict_tasks[counter] = more_task_input
                counter += 1

        print("Updated tasks", dict_tasks)


def invalid_action():
    if current_action not in list_tasks:
        print("invalid action, not listed among available options!")
        print("Rerun program to perform another Task")
        
       
        

add_task1 = add_task()
invalid_action()