class Task():

    def __init__(self):
      self.tasks = []

    def show_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}- {task.title()}")

    def add_task(self):
        if self.tasks == []:
            self.task = input('enter a to do: ')
            self.tasks.append(self.task)
        else:
            self.task = input('Please enter a new task: ')
            self.tasks.append(self.task)
        return self.tasks

    def edit_task(self):
        self.show_tasks()
        self.task_number = (int(input("What's the index of the task you want to edit?"))) - 1
        # task_number -= 1
        self.new_task = input("Please enter the new task that will replace the one you picked: ")
        self.tasks[self.task_number] = self.new_task
