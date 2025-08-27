from tkinter import *
from datetime import date
import json
import os 
from datetime import datetime


root = Tk()

#---
# Responsive window positioning - will walways open window in the center of the screen -
window_width = 340
window_height = 700

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width - window_width) / 2)
y = int((screen_height - window_height) / 3)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
#---


radio_var = StringVar()
root.title = "Task Manager"

style = "Arial 15"
today = date.today() #Gives the program the curent date
entered_date = None #User will enter a date so this will change

#---
# function to raise frames 
def show_frame(frame): 
    frame.tkraise()
#---

#---
#Function to ensure the user inputs a future date
def get_future_date(): 
    try:
        year = int(year_entry.get())
        month = int(month_entry.get())
        day = int(day_entry.get())

        global entered_date
        entered_date = date(year, month, day)
        today = date.today()

        if entered_date > today:
            result_label.config(text=f"Entered Future Date: {entered_date}")
        else:
            result_label.config(text=" enter a date in the future.")
    except ValueError:
        result_label.config(text="Invalid date. Please enter numbers for year, month, and day.")
    except Exception as e:
        result_label.config(text=f"Error: {e}")
#---

# -------- Main container frame ----------
container = Frame(root)
container.pack(fill="both", expand=True)

# -------- Frame 1: Main Menu ----------
frame_main = Frame(container, bg="#CEECFF")
frame_main.place(relwidth=1, relheight=1)

label1 = Label(frame_main, text="Task manager", bg="#A6B1FF", borderwidth=1, relief="solid", font="ARIAL 20")
label1.pack()

my_frame = Frame(frame_main, borderwidth=2, relief="solid", padx=10, pady=10)
my_frame.pack(pady=20)

label2 = Label(frame_main, text="Task Name", bg="#A6B1FF", borderwidth=1, relief="solid", font="ARIAL 12")
label2.pack(pady=(10, 5))
taskname = Entry(frame_main, bg="#A6B1FF", borderwidth=1, relief="solid", font="ARIAL 18", width=20)
taskname.pack()

date_label = Label(frame_main, text=today, font="Arial 15", bg="#CEECFF")
date_label.pack(pady=(20,5))

btn_cent = Button(frame_main, text="Enter date", bg="#A6DDFF", font=style, command=lambda: show_frame(frame2))
btn_cent.pack(pady=(5,20))

taskframe_btn = Button(frame_main, text="See tasks", bg="#A6DDFF", font=style, command=lambda: show_frame(taskframe))
taskframe_btn.pack(pady=(5,20))

label3 = Label(frame_main, text="Task Discription", bg="#A6B1FF", borderwidth=1, relief="solid", font="ARIAL 12")
label3.pack(pady=(0, 5))
discription = Text(frame_main, bg="#A6B1FF", borderwidth=1, relief="solid", font="ARIAL 18", width=20, height=5)
discription.pack()

# -------- Frame 2: Date Entry --------
frame2 = Frame(container, bg="#CEECFF")
frame2.place(relwidth=1, relheight=1)
#---

#---
#Frame 2 contents
Label(frame2, text="Year:", font="Arial 30", bg="#CEECFF").pack()
year_entry = Entry(frame2, font="Arial 22", bg="#A6B1FF")
year_entry.pack()

Label(frame2, text="Month:", font="Arial 30", bg="#CEECFF").pack()
month_entry = Entry(frame2, font="Arial 22", bg="#A6B1FF")
month_entry.pack()

Label(frame2, text="Day:", font="Arial 30", bg="#CEECFF").pack()
day_entry = Entry(frame2, font="Arial 22", bg="#A6B1FF")
day_entry.pack()

submit_button = Button(frame2, text="Submit", command=get_future_date, font="Arial 25", bg="#A6DDFF")
submit_button.pack(pady=20)

result_label = Label(frame2, text="", bg="#CEECFF", font="Arial 8")
result_label.pack()

Button(frame2, text="Back", command=lambda: show_frame(frame_main), width=11, height=2, bg="#CEECFF", font=style).pack(pady=20)
#---


# -------- Load / Initialize Task Data --------
'''Decided to use OS.path in my newer versions because 
one of the people sitting next to me was talking about
how it ensures the file is found corectly. i didnt find
any issue with the file before but added this just incase
I was overlooking something'''
if os.path.exists("TaskManagerV1.json"):
    with open("TaskManagerV1.json") as f: #Opes the Json file as a readable file
        data = json.load(f)
else:
    data = {} #if there is nothing in the json file it will create a dictionary
#---
    

#---
# -------- Task Display Frame --------
taskframe = Frame(container)
taskframe.place(relwidth=1, relheight=1)
#---


#---
# Scrollable task frame area
canvas = Canvas(taskframe, bg="#CEECFF")
scrollbar = Scrollbar(taskframe, orient="vertical", command=canvas.yview)
task_content = Frame(canvas, bg="#CEECFF")

task_content.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=task_content, anchor="center")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

def _on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", _on_mousewheel))
canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))
#---


#---
#Function to delete a task
def delete_task(task_key):
    if task_key in data:
        del data[task_key]
        with open("TaskManagerV1.json", "w") as f:
            json.dump(data, f, indent=2)
        refresh_taskframe()
#---
        
#---
#Refreshes the frame to update the tasks whithout needing to close and open the program
#Diff function to display the tasks in a organsised mannar byt creating a frame and then for every task another frame which will hold the tasks information.
def refresh_taskframe():
    for widget in task_content.winfo_children():
        widget.destroy()

    for key, value in data.items(): #Saves the task data found in the json file as variables. after it does so for task 1 it will restart and do it for task 2 and so on
        c = value["taskname"]
        a = value["discription"]
        b = value["Duedate"]

        task_block = Frame(task_content, bg="#A6B1FF", bd=2, relief="solid") #Creates the second frame which will hold the task detaisl
        task_block.pack(pady=10, fill="x", padx=5, expand=True)

        Label(task_block, text="Task Name", bg="#A6B1FF", font="Arial, 20").pack(anchor="center", fill="x", expand=True)
        name_label = Label(task_block, text=c, bg="#A6B1FF", font="Arial, 15", wraplength=300, justify="left").pack(anchor="center", fill="x")

        Label(task_block, text="Discription", bg="#A6B1FF", font="Arial, 20").pack(anchor="w", fill="x", expand=True)
        desc_label = Label(task_block, text=a, bg="#A6B1FF", font="Arial, 15", wraplength=300, justify="center").pack(anchor="w", fill="x", expand=True)

        Label(task_block, text="Due Date", bg="#A6B1FF", font="Arial, 20").pack(anchor="w", fill="x", expand=True)
        date_label = Label(task_block, text="Due by " + b, bg="#A6B1FF", font="Arial, 15", wraplength=300, justify="left").pack(anchor="w", fill="x", expand=True)

        Button(task_block, text="Delete Task", bg="red", fg="white", font="Arial 12",command=lambda k=key: delete_task(k)).pack(pady=5) #Deletes a task by calling on the delete task function

refresh_taskframe() #recals the def to refresh to update the displayed tasks in real time

Button(task_content, text="Beck", command=lambda: show_frame(frame_main), font="Arial 20", bg="#A6DDFF").pack(pady=10)#Takes the user back to the main frame / window from the view tasks frame

#---
#Function to save the user inputs and insert them into the json file
def save_data():
    global entered_date
    if entered_date is None: #if the user leaves the entered date section empty, tells the user to enter a due date before creating the task
        result_label.config(text="Please enter a due date before saving.")
        return

    tskname = taskname.get()
    taskdesc = discription.get("1.0", END).strip()
    strtaskdate = str(entered_date)
    taskdate = strtaskdate

    num = len(data)
    new = dict()
    new["taskname"] = tskname
    new["discription"] = taskdesc
    new["Duedate"] = taskdate

    c_key = "Task" + str(num+1) #When creating another task, in the json file, it needs a key to access the nested dictionary. The key will be the task followed by a number so task1.
    data[c_key] = new

    with open("TaskManagerV1.json", "w") as f: #Adds the user inputs into the json file
        json.dump(data, f, indent=2) 

    result_label.config(text="Task saved successfully!")
    refresh_taskframe() #Updates the view tasks frame / window

save_button = Button(frame_main, text="Create Task", command=save_data, width=20, height=2, bg="#A6DDFF", font=style) #Saves the user inputs by recaling the save data function
save_button.pack(pady=20)

show_frame(frame_main) #When starting the program, The frame_main frame will be displayed instead of anything else.
root.mainloop()