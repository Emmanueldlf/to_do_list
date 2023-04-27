from task import Task
import PySimpleGUI as psg
# import matplotlib
# matplotlib.use('Agg')

label = psg.Text("Enter a task you would like to add to your To Do List")
input_box = psg.InputText(tooltip="Enter a task", key='task')
task = Task()
add_button = psg.Button("Add")
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
           task.add_task(values['task'])
        case 'Edit':
            task.edit_task(values['tasks'][0]['name'], task.tasks, values['task'])
            window['tasks'].update(values=task.tasks)
        # case 'Mark':
        #     task.mark_task()
        case 'See':
            window['task'].update(value=values['tasks'][0])
            task.show_tasks()
        # case 'Check':
        #     task.show_task()
        # case 'Delete':
        #     task.delete_task()
        # case 'Destroy':
        #     task.destroy_list()
        case psg.WIN_CLOSED:
            # active = False
            # task.quit()
            break

window.close()
