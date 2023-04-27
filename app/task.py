import datetime
import calendar
import json
from json import JSONEncoder

class Task():

    def __init__(self):
      self.tasks = []
      self.task = {}
      self.filename = 'app/tasks.json'
      self.active = True

    def _read_file(self):
        with open(self.filename) as f_obj:
            self.tasks = json.load(f_obj)
        return self.tasks

    def _save_task(self):
        with open(self.filename, 'w') as f_obj:
            json.dump(self.tasks, f_obj)

    def show_tasks(self):
        try:
            self._read_file()
            if self.tasks == [] or self.tasks == None:
                self.message = print("\nYour list is currently empty.")
                return self.message
            else:
                for index, task in enumerate(self.tasks):
                    print(f"{index + 1}- {task['name'].title()}, added on {task['creation_date']}, {task['status']}")
                return self.tasks
        except ValueError:
            self.message = print("\nYou did not create any task yet so your tasks list is currently empty, please add a task to create a list, or type 'quit'")
            # self.tasks = self.message
            return self.message
        # return self.tasks

    def show_task(self):
        # with open(self.filename) as f_obj:
        #     self.tasks_list = json.load(f_obj)
            self._read_file()
            self.task_number = (int(input("\nWhat's the index of the task you want to check? ")))
            print(f"{self.task_number}- {self.tasks[self.task_number - 1]['name'].title()}, added on {self.tasks[self.task_number - 1]['creation_date']}, {self.tasks[self.task_number - 1]['status']}\n")

    def add_task(self, value):
        # self.task = {}
        # self._read_file()
        try:
            self._read_file()
            # with open(self.filename) as f_obj:
                # self.tasks = json.load(f_obj)
            if self.tasks == None:
                self.task['name'] = value
                # self.task['name'] = input('\nEnter your first task: ')
                creation_time = datetime.datetime.now()
                # time_stamp = creation_time.timestamp(creation_time)
                # date_time = datetime.fromtimestamp(time_stamp)
                self.task['creation_date'] = str(creation_time.strftime("%d-%m-%Y"))
                # print(self.task['creation_date'])
                # self.due_date = input('Please enter the date when this task should be completed?')
                # self.task['due_date'] = self.due_date.strftime('%x')
                self.task['status'] = ' [ ]'
                self.tasks = []
            else:
                self.task['name'] = value
                # self.task['name'] = input('\nPlease enter a new task: ')
                creation_time = datetime.datetime.now()
                self.task['creation_date'] = creation_time.strftime("%d-%m-%Y")
                self.task['status'] = ' [ ]'
        except ValueError:
            self.task['name'] = value
            # self.task['name'] = input('\nEnter your first task: ')
            # self.task['description'] = input('Describe briefly your first task: ')
            creation_time = datetime.datetime.now()
            self.task['creation_date'] = str(creation_time.strftime("%d-%m-%Y"))
            self.task['status'] = '[ ]'
            self.tasks = []
        except AttributeError:
            self.task['name'] = value
            # self.task['name'] = input('\nEnter your first task: ')
            # self.task['description'] = input('Describe briefly your first task: ')
            creation_time = datetime.datetime.now()
            self.task['creation_date'] = str(creation_time.strftime("%d-%m-%Y"))
            self.task['status'] = '[ ]'
            self.tasks = []
        # if self.tasks == None:
        #     self.tasks = []
        self.tasks.append(self.task)
        self._save_task()
        return self.tasks

    def edit_task(self, some_task, tasks, value):
        self.show_tasks()
        if hasattr(Task, 'message') :
            print("As a next step, please add a task or type 'quit'")
        else:
            task_to_edit = some_task
            # print(tasks)
            index = tasks.index(task_to_edit)
            tasks[index]['name'] =  value
            # self.task_number = (int(input("What's the index of the task you want to edit? ")))
            # self.new_task = input("Please enter the new task that will replace the one you picked: ")
            # self.tasks[self.task_number - 1]['name'] = self.new_task
            self._save_task()

    def mark_task(self):
        self.show_tasks()
        # self._read_file()
        if hasattr(Task, 'message') :
            print("\nAs a next step, please add a task or type 'quit'")
        else:
            self.task_number = (int(input("\nWhat's the index of the task you want to mark as completed? ")))
            self.tasks[self.task_number - 1]['status']=  " [X]"
            self._save_task()

    def delete_task(self):
        self.show_tasks()
        if self.tasks == None or self.tasks == []:
            print("\nAs a next step, please add a task or type 'quit'")
        else:
            self.task_number = (int(input("\nWhat's the index of the task you want to delete? ")))
            self.tasks.remove(self.tasks[self.task_number - 1])
            self._save_task()

    def destroy_list(self):
        self.confirmation = input("\nAre you sure you want to completely delete this list? ")
        if self.confirmation == 'Yes' or self.confirmation == 'yes':
            self._read_file()
            del(self.tasks)
            self.tasks = None
            self._save_task()
        else:
           print('\nYou will be redirected to the menu and be able to pick another action.')
        return self.tasks

    def quit(self):
        self.active = False
