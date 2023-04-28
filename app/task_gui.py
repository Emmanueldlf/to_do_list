import datetime
import calendar
import json
from json import JSONEncoder
# import PySimpleGUI as psg


class TaskGui():
    def __init__(self):
        self.tasks = []
        self.task = {}
        self.filename = 'app/tasks.json'
        self.active = True
        # self.label = psg.Text("Enter a task you would like to add to your To Do List")
        # self.input_box = psg.InputText(tooltip="Enter a task", key='task')
        # self.add_button = psg.Button("Add")
        # if hasattr(self.task, 'show_tasks'):
        #     self.list_box = psg.Listbox(values=self.task.show_tasks(), key="tasks",
        #                                 enable_events=True, size=[45, 10])
        # else:
        #     self.list_box = psg.Listbox(values=self.tasks, key="tasks",
        #                                 enable_events=True, size=[45, 10])

        # self.edit_button = psg.Button("Edit")
        # self.quit_button = psg.Button("Quit")
        # self.window = psg.Window('To Do List',
        #                             layout=[[self.label], [self.input_box, self.add_button], [self.list_box, self.edit_button], [self.quit_button]],
        #                             font=('Helvetica', 20))
        # self.event, self.values = self.window.read()
        # self.values['tasks'] = []
        # self.tasks = self.values['tasks']
        # print(1, self.event)
        # print(2, self.values)
        # print(3, self.values['tasks'])

    def _read_file(self):
        if self.filename:
            with open(self.filename) as f_obj:
                self.tasks = json.load(f_obj)
        elif not self.filename:
            with open(self.filename, 'c') as f_obj:
                self.tasks = json.dump(self.tasks, f_obj)
            with open(self.filename) as f_obj:
                self.tasks = json.load(f_obj)
        return self.tasks

    def _save_task(self):
    # def _save_task(self, tasks):
        with open(self.filename, 'w') as f_obj:
            json.dump(self.tasks, f_obj)
            # json.dump(tasks, f_obj)

    def show_tasks(self):
        try:
            self._read_file()
            if self.tasks == [] or self.tasks == None:
                self.message = print("\nYour list is currently empty.")
                return self.message
            else:
                for index, task in enumerate(self.tasks):
                    # self.tasks[index] = (f"{index + 1}- {task['name'].title()}, added on {task['creation_date']}, {task['status']}")
                    (f"{index + 1}- {task['name'].title()}, added on {task['creation_date']}, {task['status']}")
                return self.tasks
        except ValueError:
            self.message = print("\nYou did not create any task yet so your tasks list is currently empty, please add a task to create a list, or type 'quit'")
            # self.tasks = self.message
            # self.window['task'].update(value=self.values['tasks'][0])
            return self.message
        # return self.tasks

    def show_task(self):
        # with open(self.filename) as f_obj:
        #     self.tasks_list = json.load(f_obj)
        self._read_file()
        self.task_number = (int(input("\nWhat's the index of the task you want to check? ")))
        print(f"{self.task_number}- {self.tasks[self.task_number - 1]['name'].title()}, added on {self.tasks[self.task_number - 1]['creation_date']}, {self.tasks[self.task_number - 1]['status']}\n")

    # def add_task(self, value, tasks):
    def add_task(self, value):
        # self.task = {}
        # self._read_file()
        try:
            self._read_file()
            # with open(self.filename) as f_obj:
                # self.tasks = json.load(f_obj)
            if self.tasks == None:
                # self.task['name'] = self.values['task']
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
                # self.tasks = []
                # self.tasks = self.values['tasks']
            else:
                # self.task['name'] = self.values['task']
                self.task['name'] = value
                # self.task['name'] = input('\nPlease enter a new task: ')
                creation_time = datetime.datetime.now()
                self.task['creation_date'] = creation_time.strftime("%d-%m-%Y")
                self.task['status'] = ' [ ]'
        except ValueError:
            # self.task['name'] = self.values['task']
            self.task['name'] = value
            # self.task['name'] = input('\nEnter your first task: ')
            # self.task['description'] = input('Describe briefly your first task: ')
            creation_time = datetime.datetime.now()
            self.task['creation_date'] = str(creation_time.strftime("%d-%m-%Y"))
            self.task['status'] = '[ ]'
            # self.tasks = []
            # self.tasks = self.values['tasks']
        except AttributeError:
            # self.task['name'] = self.values['task']
            self.task['name'] = value
            # self.task['name'] = input('\nEnter your first task: ')
            # self.task['description'] = input('Describe briefly your first task: ')
            creation_time = datetime.datetime.now()
            self.task['creation_date'] = str(creation_time.strftime("%d-%m-%Y"))
            self.task['status'] = '[ ]'
            # self.tasks = []
            # self.tasks = self.values['tasks']
        # if self.tasks == None:
        #     self.tasks = []
        self.tasks.append(self.task)
        self._save_task()
        # tasks.append(self.task)
        # self._save_task(tasks)
        return self.tasks
        # return tasks


    def edit_task(self, some_task, value):
        # self.show_tasks()
        self._read_file()
        # print(self.tasks)
        if hasattr(TaskGui, 'message') :
            print("As a next step, please add a task or type 'quit'")
        else:
            task_to_edit = some_task
            index = self.tasks.index(task_to_edit)
            self.tasks[index]['name'] =  value
            # tasks[index]['name'] =  value
            # self.task_number = (int(input("What's the index of the task you want to edit? ")))
            # self.new_task = input("Please enter the new task that will replace the one you picked: ")
            # self.tasks[self.task_number - 1]['name'] = self.new_task
            self._save_task()
            # self.window['tasks'].update(values=self.task.tasks)


    def mark_task(self):
        self.show_tasks()
        # self._read_file()
        if hasattr(TaskGui, 'message') :
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
        # psg.WIN_CLOSED
