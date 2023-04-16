from task import Task

active = True
task = Task()

while active:
    user_action = input("Will you add a task? edit a task? See your list?")
    match user_action:
        case 'Add':
            # task = Task()
            task.add_task()
        case 'Edit':
            task.edit_task()
        case 'See':
            task.show_tasks()
        case 'Quit':
            active = False


# print(tasks)
