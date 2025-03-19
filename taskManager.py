'''
What I'll Need To Do: 
1. 7 Options (Functions)
2. a way to keep the program running (while loop) and a way to get out of the loop (exit option/break)
3. deleting, nesting, and adding dictionaries and their values (Have the steps be the tasks value, but set the value as a dictionary?)
4. make it so the tasks are displayed
5. be able to display the number of tasks
6. be able to mark a task's step as completed. (probably could just change the steps' value? unsure)
'''

tasks = {}

def add_task():
    task_name = input("Enter the task name: ")
    print(f"Task '{task_name}' added successfully.")
    
    tasks[task_name] = {}

    '''
    task_name = "Brush Teeth"
    { Bob: {step1: blah, step2: blah, step3: blah},  Brush Teeth: {step1: blah, step2: blah, step3: blah},}
    '''

def add_step():
    
    steps = input("")

def mark_completed():
    print("temporarily here")

def view_tasks():
    print(f"{tasks}")

def remove_task():
    task_del = input("Please enter the task would you like to remove: ")
    del (task_del) # COME BACK TO THIS!!!

def display_num_of_tasks():
    print()

def main():

    while True:
        print("\n--- Task Manager ---\n")
        print("1. Add a Task")
        print("2. Add a Step to a Task")
        print("3. Mark Step as Completed")
        print("4. View All Tasks")
        print("5. Remove a Task")
        print("6. Display Total Number of Tasks")
        print("7. Quit")

        try: 
            choice = int(input("Choose an option (1-7): "))
            if choice == 7:
                print("Exiting the system. Goodbye!\n")
                break
            elif choice == 1:
                add_task()
        except: 
            print("Error You have entered an incorrect value, please try again.")

if __name__ == "__main__":
    main()