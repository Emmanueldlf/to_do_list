import json
from json import JSONEncoder

class Task():

    def __init__(self):
      self.tasks = []
      self.task = {}
      self.filename = 'app/tasks.json'
      self.active = True

    def _read_file_(self):
       with open(self.filename) as f_obj:
            self.tasks = json.load(f_obj)

    def show_tasks(self):
        try:
            self._read_file_()
            if self.tasks == [] or self.tasks == None:
                self.message = print("Your list is currently empty.")
                return self.message
            else:
                for index, task in enumerate(self.tasks):
                    print(f"{index + 1}- {task['name'].title()} {task['status']}")
                return self.tasks
        except ValueError:
            self.message = print("You did not create any task yet so your tasks list is currently empty, please add a task to create a list, or type 'quit'")
            # self.tasks = self.message
            return self.message
        # return self.tasks

    def show_task(self):
        # with open(self.filename) as f_obj:
        #     self.tasks_list = json.load(f_obj)
            self.task_number = (int(input("What's the index of the task you want to check? ")))
            print(f"{self.task_number}- {self.tasks_list[self.task_number - 1]['name'].title()} {self.tasks_list[self.task_number - 1]['status']}\n")

    def add_task(self):
        # self.task = {}
        self._read_file_()
        try:
            # self._read_file_()
            # with open(self.filename) as f_obj:
                # self.tasks = json.load(f_obj)
            self.task['name'] = input('Please enter a new task: ')
            self.task['status'] = ' [ ]'
        except ValueError:
            self.task['name'] = input('Enter your first task: ')
            # self.task['description'] = input('Describe briefly your first task: ')
            self.task['status'] = '[ ]'
            self.tasks = []
        except AttributeError:
            self.task['name'] = input('Enter your first task: ')
            # self.task['description'] = input('Describe briefly your first task: ')
            self.task['status'] = '[ ]'
            self.tasks = []
        if self.tasks == None:
            self.tasks = []
        self.tasks.append(self.task)
        self._save_task_()
        return self.tasks

        # if self.tasks == []:
        #     self.task['name'] = input('Enter your first task: ')
        #     # self.task['description'] = input('Describe briefly your first task: ')
        #     self.task['status'] = '[ ]'
        # else:
        #     with open(self.filename) as f_obj:
        #         self.tasks = json.load(f_obj)
        #     self.task['name'] = input('Please enter a new task: ')
        #     self.task['status'] = ' [ ]'
        # self.tasks.append(self.task)
        # self.save_task()
        # return self.tasks

    def _save_task_(self):
        with open(self.filename, 'w') as f_obj:
            json.dump(self.tasks, f_obj)

    def edit_task(self):
        self.show_tasks()
        if hasattr(Task, 'message') :
            print("As a next step, please add a task or type 'quit'")
        else:
            self.task_number = (int(input("What's the index of the task you want to edit? ")))
            self.new_task = input("Please enter the new task that will replace the one you picked: ")
            self.tasks[self.task_number - 1]['name'] = self.new_task
            self._save_task_()

    def mark_task(self):
        self.show_tasks()
        if hasattr(Task, 'message') :
            print("As a next step, please add a task or type 'quit'")
        else:
            self.task_number = (int(input("What's the index of the task you want to mark as completed? ")))
            self.tasks[self.task_number - 1]['status']=  " [X]"
            self._save_task_()

    def delete_task(self):
        self.show_tasks()
        if self.tasks == None or self.tasks == []:
            print("As a next step, please add a task or type 'quit'")
        else:
            self.task_number = (int(input("What's the index of the task you want to delete? ")))
            self.tasks.remove(self.tasks[self.task_number - 1])
            self._save_task_()

    def destroy_list(self):
        #Not working
        self._read_file_()
        self.confirmation = input("Are you sure you want to completely delete this list? ")
        if self.confirmation.title == 'Yes':
            # with open(self.filename) as f_obj:
                # self.tasks = json.load(f_obj)
            del(self.tasks)
            self.tasks = None
        else:
            'You will be redirected to the menu and be able to pick another action.'
        # self.tasks = None
        self._save_task_()

    def quit(self):
        self.active = False
