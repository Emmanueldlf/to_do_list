from task import *
from PySimpleGUI import *

label = PySimpleGUI.Text("Enter a task you would like to add to your To Do List")


window = PySimpleGUI.Window('To Do List', layout=[""])
window.read()
window.close()
