from task import Task
import PySimpleGUI as psg
# import matplotlib
# matplotlib.use('Agg')

label = psg.Text("Enter a task you would like to add to your To Do List")
input_box = psg.InputText(tooltip="Enter a task")
add_button = psg.Button("Add")


window = psg.Window('To Do List', layout=[[label], [input_box, add_button]])
window.read()
print("Welcome to our Tasks app")
window.close()
