from tkinter import *
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

# Function to raise a frame
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

# --------- Frame 1: Main Menu ----------
frame_main = Frame(container)
frame_main.place(relwidth=1, relheight=1)



# Button row (L and R side-by-side)
button_frame = Frame(frame_main)
button_frame.pack()




#---creat task window---
label1 = Label(button_frame, text="Task manager", bg="lightblue", borderwidth=1, relief="solid", font="ARIAL 20")
label1.pack()

my_frame = Frame(root, borderwidth=2, relief="solid", padx=10, pady=10)
my_frame.pack(pady=20) # Use pack to position the frame in the root window

label2 = Label(button_frame, text="Task Name", bg="lightblue", borderwidth=1, relief="solid", font="ARIAL 12")
label2.pack(pady=(10, 5))

taskname = Entry(button_frame, bg="lightblue", borderwidth=1, relief="solid", font="ARIAL 18", width=20)
taskname.pack()




date_label = Label(button_frame, text=today, font="Arial 15")
date_label.pack(pady=(20,5))

#Takes you to the second frame
btn_cent = Button(button_frame, text="Enter date", bg="lightgrey", font=style, command=lambda: show_frame(frame_cent))
btn_cent.pack(pady=(5,20))

taskframe_btn = Button(button_frame, text="See tasks", bg="lightgrey", font=style, command=lambda: show_frame(taskframe))
taskframe_btn.pack(pady=(5,20))


label3 = Label(button_frame, text="Task Discription", bg="lightblue", borderwidth=1, relief="solid", font="ARIAL 12")
label3.pack(pady=(0, 5))

discription = Text(button_frame, bg="lightblue", borderwidth=1, relief="solid", font="ARIAL 18", width=20, height=5)
discription.pack()

'''
img = PhotoImage(file="Images/TestImg.png")
smallerimg = img.subsample(4, 4)
image_label = Label(button_frame, image=smallerimg)
image_label.pack(pady=(20, 3))


label4 = Label(button_frame, text=health, bg="lightblue", borderwidth=1, relief="solid", font="ARIAL 12")
label4.pack(pady=(0, 20))
'''



#--Class manager window ^




#the second frame contents
frame_cent = Frame(container)
frame_cent.place(relheight=1, relwidth=1)

#--- Enter date window
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
Button(frame_cent, text="Back", command=lambda: show_frame(frame_main)).pack()#takes me back to the main frame


'''print(today)
'''
#how to ensure that the due date is due
''' 
str_d1 = today # curent date
str_d2 = today #Due date --> Instead of today, it needs to be the date in the json dictionary

# convert string to date object
#d1 = datetime.strptime(str_d1, "%Y/%m/%d")
#d2 = datetime.strptime(str_d2, "%Y/%m/%d")

# difference between dates in timedelta
delta = str_d2 - str_d1 # Due date - Curent date
print(f'Difference is {delta} days')
'''



with open ("TaskManagerV1json") as f:
    data = json.load(f)


#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#I am trying to display the json dictionary items

question_num = len(data)  # check how many questions are already in the quiz 
taskframe = Frame(container, width=350, height=250)
taskframe.pack(fill="both", expand=True)
Button(taskframe, text="Back", command=lambda: show_frame(frame_main), font="Arial 20").pack(pady=20)

for key, value in data.items():
    c = value["taskname"]
    a = value["discription"]
    b = value["Duedate"]
    dis01 = Label(taskframe, text="Task Name", bg="lightblue", bd=2, relief="solid", width=30, font="Arial").pack(pady=(0,0))
    dis1 = Label(taskframe, text=c, bg="lightblue", bd=2, relief="solid", width=30, font="Arial").pack(pady=(0,0))
    dis02 = Label(taskframe, text="Discription", bg="lightblue", bd=2, relief="solid", width=30, font="Arial").pack(pady=(0,0))
    dis2 = Label(taskframe, text=a, bg="lightblue", bd=2, relief="solid", width=30, font="Arial").pack(pady=(0,0))
    dis03 = Label(taskframe, text="Due Date", bg="lightblue", bd=2, relief="solid", width=30, font="Arial").pack(pady=(0,0))
    dis3 = Label(taskframe, text="Due by " + b, bg="lightblue", bd=2, relief="solid", width=30, font="Arial").pack(pady=(0,40))



#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
    

# Show main frame when proram starts
show_frame(frame_main)
root.mainloop()