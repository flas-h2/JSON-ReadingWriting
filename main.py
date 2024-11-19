import json
import time


def load_tasks():
    """Function to load the JSON file with all tasks inside."""
    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)
            return data
    except IOError:
        data = {}
        return data
    

def new_id():
    """Function to create a new ID for every new task to identify what it is and to search by."""
    with open("id.json", "r") as file:
        data = json.load(file)
        id = data[0]
        id += 1 
    with open("id.json", "w") as file:
        json.dump([id], file)
    return id


def view_completed_tasks(tasks):
    """Function to view the completed tasks listed in the JSON file."""
    for task in tasks:
        if task["status"] == "Complete":
            print(f"\nName of task: {task["task"]}")
            print(f"ID of task: {task["id"]}")
            print(f"Status of task: {task["status"]}")
            time.sleep(2)
            

def view_incompleted_tasks(tasks):
    """Function to view the incompleted tasks listed in the JSON file."""
    for task in tasks:
        if task["status"] == "Incomplete":
            print(f"\nName of task: {task["task"]}")
            print(f"ID of task: {task["id"]}")
            print(f"Status of task: {task["status"]}")
            time.sleep(2)
            

def view_all_tasks(tasks):
    """Function to view all tasks listed in the JSON file."""
    for task in tasks: 
        print(f"\nTask: {task["task"]}")
        print(f"ID: {task["id"]}")
        print(f"Status: {task["status"]}")
        time.sleep(2)


def mark_task_complete(tasks):
    """Prompts the user to enter the id for the task they would like to mark as complete and then uses another function to update the json"""
    while True:
        while True:
            try:
                userin = int(input("What is the id for the task you would like to mark as completed? "))
                break
            except Exception:
                print("Not a valid input, please input a number.")
        task_counter = 0
        for task in tasks:
            if task["id"] == userin and task["status"] == "Complete":
                print("This task is already completed")
            elif task["id"] == userin:
                task["status"] = "Complete"
                task_counter += 1
        if task_counter == 0:
            print("No task found with that id. Please try again.")
        else:
            update_json(tasks)
            return tasks
        

def update_json(tasks):
    """Function to update the JSON file after changing it."""
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def add_new_task(tasks):
    """Function to add new tasks to the JSON file."""
    task_name_inp = input("Please enter new task name: ")
    task_id = new_id()
    tasks.append({"task": task_name_inp, "id": task_id, "status": "Incomplete"})
    print(f"Your task is now listed under ID {task_id}")
            

def main():
    """Main function that runs the code."""
    data = load_tasks()
    while True:
        inp = input("""Please choose an option: \n1. View completed tasks \n2. View incomplete tasks \n3. View all tasks \n4. Mark a task as complete \n5. Add a new task \n6. Exit \n""")
        if inp == "1":
            time.sleep(1)
            view_completed_tasks(data)
        elif inp == "2":
            time.sleep(1)
            view_incompleted_tasks(data)
        elif inp == "3":
            time.sleep(1)
            view_all_tasks(data)
        elif inp == "4":
            time.sleep(1)
            mark_task_complete(data)
        elif inp == "5":
            time.sleep(1)
            add_new_task(data)
        elif inp == "6":
            quit()
        else:
            print("Please input a valid response listed above.")
    

if __name__ == "__main__":
    main()