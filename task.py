import json
from json import JSONEncoder

class Task():

    def __init__(self):
      self.tasks = []
      self.task = {}
      self.filename = 'tasks.json'

    def show_tasks(self):
        with open(self.filename) as f_obj:
            self.tasks = json.load(f_obj)
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}- {task['name'].title()} {task['status']}")
        return self.tasks

    def show_task(self):
        with open(self.filename) as f_obj:
            self.tasks_list = json.load(f_obj)
            self.task_number = (int(input("What's the index of the task you want to check? ")))
            print(f"{self.task_number}- {self.tasks_list[self.task_number - 1]['name'].title()} {self.tasks_list[self.task_number - 1]['status']}")


    def add_task(self):
        self.task = {}
        if self.tasks == []:
            self.task['name'] = input('Enter your first task: ')
            # self.task['description'] = input('Describe briefly your first task: ')
            self.task['status'] = '[ ]'
            self.tasks.append(self.task)
        else:
            self.task['name'] = input('Please enter a new task: ')
            self.task['status'] = ' [ ]'
            self.tasks.append(self.task)
        return self.tasks

    def save_task(self):
        with open(self.filename, 'w') as f_obj:
            json.dump(self.tasks, f_obj)

    def edit_task(self):
        self.show_tasks()
        self.task_number = (int(input("What's the index of the task you want to edit? ")))
        self.new_task = input("Please enter the new task that will replace the one you picked: ")
        self.tasks[self.task_number - 1]['name'] = self.new_task

    def mark_task(self):
        self.show_tasks()
        self.task_number = (int(input("What's the index of the task you want to mark as completed? ")))
        self.tasks[self.task_number - 1]['status']=  " [X]"
