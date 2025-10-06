from todo import TodoList

def main():
    todo = TodoList()

    while True:
        print("\nOptions: add, list, done, delete, exit")
        choice = input("Enter choice: ").strip().lower()

        if choice == "add":
            task = input("Enter new task: ").strip()
            if task:
                todo.add_task(task)
            else:
                print("Task cannot be empty!")
        elif choice == "list":
            todo.list_tasks()
        elif choice == "done":
            try:
                number = int(input("Enter task number to mark as done: "))
                todo.mark_done(number)
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "delete":
            try:
                number = int(input("Enter task number to delete: "))
                todo.delete_task(number)
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "exit":
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()