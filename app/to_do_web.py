from task import Task
import streamlit as st

# active = True
task = Task()

st.title('Tasks Management')
st.subheader('This is a Tasks Management app')
st.write('This app is to help keep track of your tasks')

task.show_tasks()
for task in task.tasks:
    st.checkbox(task['name'] )

st.text_input(label="", placeholder="Add a new task...")





# while task.active:
#     user_action = input("\nWill you add a task? edit a task? Mark a task as completed? See your list? Check a specific task? Delete a task? Destroy your list?\n")
#     match user_action.title():
#         case 'Add':
#             task.add_task()
#         case 'Edit':
#             task.edit_task()
#         case 'Mark':
#             task.mark_task()
#         case 'See':
#             task.show_tasks()
#         case 'Check':
#             task.show_task()
#         case 'Delete':
#             task.delete_task()
#         case 'Destroy':
#             task.destroy_list()
#         case 'Quit':
#             # active = False
#             task.quit()
