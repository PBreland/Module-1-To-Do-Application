menu_items = ['1. Add a task',
            '2. View all tasks', 
            '3. Delete a task', 
            '4. Quit'
]
task_list = [

]
def main_menu():
    print("Welcome to the To-Do List Application!")
    print("\n")
    print('Menu:', *menu_items, sep='\n ')
def add_task():
            action = input("Enter task or exit to return to Main Menu: ")
            if action.lower() != 'exit':
                task_list.append(action)
                print("\nTask added!")
                multiple_task_add()
            elif action == 'exit':
                print("\nReturning to menu")
def view_task():
    if task_list:
        print('\n''Current Tasks:', *task_list, sep='\n -')
    else:
        print("\nNo tasks available.")
def remove_task():
    view_task()
    action = input("Enter a task to remove or exit to return to main menu: ")
    if action == 'exit':
        print("\nReturning to menu")
        return
    for i, task in enumerate(task_list):
         if task.startswith(action):
            task_list.remove(task)
            print("\nTask removed!")
            multiple_task_remove()
            break
    else:
        print("\nNot a valid task. Please try again.")
def multiple_task_add():
        while True:
            action = input("Add another task or exit: ")
            if action == 'exit':
                print("\nReturning to main menu.")
                break
            else:
                task_list.append(action)
                print("\nTask added!")
def multiple_task_remove():
    while True:
        view_task()
        action = input("Remove another task or exit: ")
        if action == 'exit':
                print("\nReturning to the main menu.")
                break
        for i, task in enumerate(task_list):
            if task.startswith(action):
                task_list.remove(task)
                print("\nTask has been removed.")
        else:
            print("\nThis is not a valid task. Please try again.")
while True:
    main_menu()
    try:
        user_action = int(input("Please select a menu item number: ")) #must be an integer
        if user_action == 1:
            add_task()
        if user_action == 2:
            view_task()
        if user_action == 3:
            remove_task()
        if user_action == 4:
            print(f"\nThank you for using my app! Cheers!")
            break
    except ValueError:
        print("\n")
        print("That is not a valid selection. Please try again.")