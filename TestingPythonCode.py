'''from tkinter import *
from tkinter import PhotoImage
from datetime import date
import json
import os 
from datetime import datetime


root = Tk()
root.geometry("340x700")
radio_var = StringVar()
root.title = "Task Manager"

style = "Arial 15"
health = 100
today = date.today()



taskame = Entry(root, bg="lightblue", borderwidth=1, relief="solid", font="ARIAL 18", width=20)
taskame.pack()


discrption = Text(root, bg="lightblue", borderwidth=1, relief="solid", font="ARIAL 18", width=20, height=5)
discrption.pack()




with open ("TaskManagerV1json") as f:
    data = json.load(f)

#Adding new tasts to the json file


def save_task():

    num = len(data)  # check how many questions are already in the quiz 
    new = dict()
    new = {"input_text": taskame} #This will be replaced with an entry box
    new = {"discription": discrption} # this will be replaced with an entry box

    c_key = "Task" + str(num+1)
    data[c_key] = new
    with open("TaskManagerV1json", "w") as f:
        json.dump(data, f, indent=2)

submit_button = Button(root, text="Creat task", command=save_task, font="Arial 25", bg="lightgrey")
submit_button.pack()

root.mainloop()'''

import tkinter as tk
import json

with open("TaskManagerV1json", 'r') as f:
    data = json.load(f)

def save_data():
    name = name_entry.get()
    age = age_entry.get()

    num = len(data)  # check how many questions are already in the quiz 
    new = dict()
    new = {"taskname": name} #This will be replaced with an entry box
    new = {"discription": age} # this will be replaced with an entry box
    
    
    c_key = "Task" + str(num+1)
    data[c_key] = new

    with open("TaskManagerV1json", "w") as f:
        json.dump(data, f, indent=2)

# Create the main window
root = tk.Tk()
root.title("User Data Entry")

# Create Entry widgets
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

age_label = tk.Label(root, text="Age:")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

# Create a Save button
save_button = tk.Button(root, text="Save Data", command=save_data)
save_button.pack()

root.mainloop()