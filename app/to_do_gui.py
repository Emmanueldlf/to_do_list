from task_gui import TaskGui
import PySimpleGUI as psg
# import matplotlib
# matplotlib.use('Agg')

label = psg.Text("Enter a task you would like to add to your To Do List")
input_box = psg.InputText(tooltip="Enter a task", key='task')
task = TaskGui()
add_button = psg.Button("Add")
# if hasattr(task, 'show_tasks'):
#     list_box = psg.Listbox(values=task.show_tasks(), key="tasks",
#                             enable_events=True, size=[45, 10])
# else:
#     list_box = psg.Listbox(values=task.tasks, key="tasks",
#                             enable_events=True, size=[45, 10])
# list_box = psg.Listbox(values=task.show_tasks(), key="tasks",
#                        enable_events=True, size=[45, 10])
list_box = psg.Listbox(values=task.show_tasks(), key="tasks",
                       enable_events=True, size=[45, 10])
edit_button = psg.Button("Edit")
quit_button = psg.Button("Quit")

window = psg.Window('To Do List',
                    layout=[[label], [input_box, add_button], [list_box, edit_button], [quit_button]],
                    font=('Helvetica', 20))
# task = Task()
while task.active:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['tasks'])
    # user_action = input("\nWill you add a task? edit a task? Mark a task as completed? See your list? Check a specific task? Delete a task? Destroy your list?\n")
    match event:
        case 'Add':
            # task.add_task()
            task.add_task(values['task'])
            # task.add_task(values['task'], values['tasks'])
        case 'Edit':
            # task.edit_task(values['tasks'][0], task.tasks, values['task'])
            task.edit_task(values['tasks'][0], values['task'])
            window['tasks'].update(values=task.show_tasks())
        # case 'Mark':
        #     task.mark_task()
        case 'See':
            window['task'].update(value=values['tasks'][0]['name'])
            # task.show_tasks()
        # case 'Check':
        #     task.show_task()
        # case 'Delete':
        #     task.delete_task()
        # case 'Destroy':
        #     task.destroy_list()
        # case 'Quit':
        case 'Quit':
            # active = False
            # task.quit()
            psg.WIN_CLOSED
            break

window.close()
