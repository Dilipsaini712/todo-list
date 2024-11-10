task = []
print("*******Welcome In To-Do-List*******")

while True:
    print("1. Add Task")
    print("2. Show Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit.\n")

    choice=input("Enter the your choice: ")

    if choice == '1':
        n_task=int(input("How many task you want to add in list: "))
        for i in range(1,n_task+1):
            add=input(f"Enter your task {i} = ")
            task.append(add)
            print(f"{task} task has been added successfully.\n")
    
    elif choice == '2':
        if len(task) == 0:
            print("No task available in list.\n")
        else:
            print("*******Your Task List*******")
            for i in range(len(task)):
                print(f"{i+1}. {task[i]}")
            print("\n")
    
    elif choice == '3':
        if len(task) == 0:
            print("No task available in list.\n")
        else:
            update_task=int(input("Enter the task number you want to update: "))
            if update_task < 1 or update_task > len(task):
                print("Invalid task number. Please try again.\n")
            else:
                task[update_task-1] = input("Enter the new task: ")
                print(f"Task {update_task} has been updated successfully.\n")

    elif choice == '4':
        if len(task) == 0:
            print("No task available in list.\n")
        else:
            delete_task=int(input("Enter the task number you want to delete: "))
            if delete_task < 1 or delete_task > len(task):
                print("Invalid task number. Please try again.\n")
            else:
                del task[delete_task - 1]
                print(f"Task {delete_task} has been deleted successfully.\n")
    
    elif choice == '5':
        print("Thank you for using To-Do-List. Good Bye!\n")
        break
    
    else:
        print("Please enter right choice 1-5!\n please try again.\n")