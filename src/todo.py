from colorama import Fore, Style

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        print(Fore.GREEN + "Task added successfully!" + Style.RESET_ALL)

    def list_tasks(self):
        if not self.tasks:
            print(Fore.YELLOW + "No tasks found." + Style.RESET_ALL)
            return
        print("\nYour Tasks:")
        for idx, t in enumerate(self.tasks, start=1):
            status = Fore.GREEN + "✅ Done" + Style.RESET_ALL if t["done"] else Fore.RED + "❌ Pending" + Style.RESET_ALL
            print(f"{idx}. {t['task']} - {status}")

    def mark_done(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number-1]["done"] = True
            print(Fore.CYAN + f"Task {task_number} marked as done!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid task number!" + Style.RESET_ALL)

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            deleted = self.tasks.pop(task_number-1)
            print(Fore.MAGENTA + f"Deleted task: {deleted['task']}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid task number!" + Style.RESET_ALL)