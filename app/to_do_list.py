from task import Task

# active = True
task = Task()

while task.active:
    user_action = input("\nWill you add a task? edit a task? Mark a task as completed? See your list? Check a specific task? Delete a task? Destroy your list?\n")
    match user_action.title():
        case 'Add':
            task.add_task()
        case 'Edit':
            task.edit_task()
        case 'Mark':
            task.mark_task()
        case 'See':
            task.show_tasks()
        case 'Check':
            task.show_task()
        case 'Delete':
            task.delete_task()
        case 'Destroy':
            task.destroy_list()
        case 'Quit':
            # active = False
            task.quit()
