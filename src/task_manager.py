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

def add_task():
    if current_action == task1:
        print("Executing add Task functionality...")
        time.sleep(1)
        add_task1 = input("Input your task: ")

        dict_tasks[i] = add_task1
        print(dict_tasks)
        time.sleep(0.5)

        print("Task added successfully...")
        time.sleep(0.5)

    verify_adding_tasks = input("Do you want to add more Tasks ?:: ")
    try:
        if verify_adding_tasks.lower() == 'yes':
            amount_of_tasks = int(input("Enter amount of tasks to add in Integer:: "))

            for i in range(amount_of_tasks):
                more_tasks = input("Enter tasks:: ")
                dict_tasks[i] = more_tasks
                print(dict_tasks)



            # print(f"\nSystem ready to add {amount_of_tasks} TO-DO's")
    except ValueError as e:
        print(e)
 
        # return add_task1
    
        
    




def invalid_action():
    if current_action not in list_tasks:
        print("invalid action, not listed among available options!")
        print("Rerun program to perform another Task")
        
       
        


add_task1 = add_task()
invalid_action()