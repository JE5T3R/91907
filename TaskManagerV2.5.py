from tkinter import *
from datetime import date
import json
import os 
from datetime import datetime

#Scrollbar, delete tasks and window position when opening the program has been added.

root = Tk()

# Responsive window positioning
window_width = 340
window_height = 700

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width - window_width) / 2)
y = int((screen_height - window_height) / 3)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
radio_var = StringVar()
root.title = "Task Manager"

style = "Arial 15"
health = 100
today = date.today()
entered_date = None

def show_frame(frame):
    frame.tkraise()

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

# -------- Main container frame ----------
container = Frame(root)
container.pack(fill="both", expand=True)

# -------- Frame 1: Main Menu ----------
frame_main = Frame(container)
frame_main.place(relwidth=1, relheight=1)

label1 = Label(frame_main, text="Task manager", bg="lightblue", borderwidth=1, relief="solid", font="ARIAL 20")
label1.pack()

my_frame = Frame(frame_main, borderwidth=2, relief="solid", padx=10, pady=10)
my_frame.pack(pady=20)

label2 = Label(frame_main, text="Task Name", bg="lightblue", borderwidth=1, relief="solid", font="ARIAL 12")
label2.pack(pady=(10, 5))
taskname = Entry(frame_main, bg="lightblue", borderwidth=1, relief="solid", font="ARIAL 18", width=20)
taskname.pack()

date_label = Label(frame_main, text=today, font="Arial 15")
date_label.pack(pady=(20,5))

btn_cent = Button(frame_main, text="Enter date", bg="lightgrey", font=style, command=lambda: show_frame(frame_cent))
btn_cent.pack(pady=(5,20))

taskframe_btn = Button(frame_main, text="See tasks", bg="lightgrey", font=style, command=lambda: show_frame(taskframe))
taskframe_btn.pack(pady=(5,20))

label3 = Label(frame_main, text="Task Discription", bg="lightblue", borderwidth=1, relief="solid", font="ARIAL 12")
label3.pack(pady=(0, 5))
discription = Text(frame_main, bg="lightblue", borderwidth=1, relief="solid", font="ARIAL 18", width=20, height=5)
discription.pack()

# -------- Frame 2: Date Entry --------
frame_cent = Frame(container)
frame_cent.place(relwidth=1, relheight=1)

Label(frame_cent, text="Year:", font="Arial 30").pack()
year_entry = Entry(frame_cent, font="Arial 22", bg="lightblue")
year_entry.pack()

Label(frame_cent, text="Month:", font="Arial 30").pack()
month_entry = Entry(frame_cent, font="Arial 22", bg="lightblue")
month_entry.pack()

Label(frame_cent, text="Day:", font="Arial 30").pack()
day_entry = Entry(frame_cent, font="Arial 22", bg="lightblue")
day_entry.pack()

submit_button = Button(frame_cent, text="Submit", command=get_future_date, font="Arial 25", bg="lightgrey")
submit_button.pack()

result_label = Label(frame_cent, text="")
result_label.pack()
Button(frame_cent, text="Back", command=lambda: show_frame(frame_main)).pack()

# -------- Load or Initialize Task Data --------
if os.path.exists("TaskManagerV1.json"):
    with open("TaskManagerV1.json") as f:
        data = json.load(f)
else:
    data = {}

# -------- Task Display Frame --------
taskframe = Frame(container)
taskframe.place(relwidth=1, relheight=1)

# Static header
Button(taskframe, text="Back", command=lambda: show_frame(frame_main), font="Arial 20").pack(pady=10)

# Scrollable task content area
canvas = Canvas(taskframe, bg="white")
scrollbar = Scrollbar(taskframe, orient="vertical", command=canvas.yview)
task_content = Frame(canvas, bg="white")

task_content.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=task_content, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

def _on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", _on_mousewheel))
canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))

def delete_task(task_key):
    if task_key in data:
        del data[task_key]
        with open("TaskManagerV1.json", "w") as f:
            json.dump(data, f, indent=2)
        refresh_taskframe()

def refresh_taskframe():
    for widget in task_content.winfo_children():
        widget.destroy()

    for key, value in data.items():
        c = value["taskname"]
        a = value["discription"]
        b = value["Duedate"]

        task_block = Frame(task_content, bg="lightblue", bd=2, relief="solid")
        task_block.pack(pady=10, fill="x", padx=5)

        Label(task_block, text="Task Name", bg="lightblue", font="Arial").pack(anchor="w", fill="x", expand=True)
        name_label = Label(task_block, text=c, bg="lightblue", font="Arial", wraplength=300, justify="left")
        name_label.pack(anchor="w", fill="x")

        Label(task_block, text="Discription", bg="lightblue", font="Arial").pack(anchor="w", fill="x", expand=True)
        desc_label = Label(task_block, text=a, bg="lightblue", font="Arial", wraplength=300, justify="left")
        desc_label.pack(anchor="w", fill="x", expand=True)

        Label(task_block, text="Due Date", bg="lightblue", font="Arial").pack(anchor="w", fill="x", expand=True)
        date_label = Label(task_block, text="Due by " + b, bg="lightblue", font="Arial", wraplength=300, justify="left")
        date_label.pack(anchor="w", fill="x", expand=True)

        Button(task_block, text="Delete Task", bg="red", fg="white", font="Arial 12",
               command=lambda k=key: delete_task(k)).pack(pady=5)

refresh_taskframe()

# -------- Save Data Function --------
def save_data():
    global entered_date
    if entered_date is None:
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

    c_key = "Task" + str(num+1)
    data[c_key] = new

    with open("TaskManagerV1.json", "w") as f:
        json.dump(data, f, indent=2)

    result_label.config(text="Task saved successfully!")
    refresh_taskframe()

save_button = Button(frame_main, text="Save Data", command=save_data)
save_button.pack()

show_frame(frame_main)
root.mainloop()