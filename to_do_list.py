from task import Task

active = True
task = Task()

while active:
    user_action = input("Will you add a task? edit a task? Mark a task as completed? See your list? Check a specific task? ")
    match user_action:
        case 'Add':
            task.add_task()
            task.save_task()
        case 'Edit':
            task.edit_task()
            task.save_task()
        case 'Mark':
            task.mark_task()
            task.save_task()
        case 'See':
            task.show_tasks()
        case 'Check':
            task.show_task()
        case 'Quit':
            active = False


# print(tasks)
