import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
inputBox = sg.InputText(tooltip="Enter a todo")
add_button = sg.Button("Add todo")
del_button = sg.Button("Delete todo")


window = sg.Window("My Todo App", layout=[[label],[inputBox],[add_button, del_button]])

window.read()
window.close()
