from tkinter import *
from tkinter import PhotoImage
from datetime import date
import json
import os 



root = Tk()
root.geometry("340x700")
root.resizable(0, 0)
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
label1.grid(row=0, column=0, padx=5, pady=5)

my_frame = Frame(root, borderwidth=2, relief="solid", padx=10, pady=10)
my_frame.pack(pady=20) # Use pack to position the frame in the root window

label2 = Label(button_frame, text="Task Name", bg="lightblue", borderwidth=1, relief="solid", font="ARIAL 12")
label2.grid(row=1, column=0, padx=5, pady=5)

taskname = Entry(button_frame, bg="lightblue", borderwidth=1, relief="solid", font="ARIAL 18", width=20)
taskname.grid(row=2, column=0, padx=5, pady=(5, 30))




date_label = Label(button_frame, text=today, font="Arial 15")
date_label.grid(row=3, column=0, padx=20, pady=20)


label3 = Label(button_frame, text="Task Discription", bg="lightblue", borderwidth=1, relief="solid", font="ARIAL 12")
label3.grid(row=4, column=0, padx=5, pady=5)

discription = Text(button_frame, bg="lightblue", borderwidth=1, relief="solid", font="ARIAL 18", width=20, height=5)
discription.grid(row=5, column=0, padx=5, pady=(5, 30))


img = PhotoImage(file="Images/TestImg.png")
smallerimg = img.subsample(4, 4)
image_label = Label(button_frame, image=smallerimg)
image_label.grid(row=6, column=0, padx=5, pady=5, sticky="W")


label4 = Label(button_frame, text=health, bg="lightblue", borderwidth=1, relief="solid", font="ARIAL 12")
label4.grid(row=6, column=0, padx=100, pady=50, sticky="E")


#Takes you to the second frame
btn_cent = Button(button_frame, text="Enter date", bg="yellow", font=style, command=lambda: show_frame(frame_cent))
btn_cent.grid(padx=10, row=7, column=0, pady=40)


#--Class manager window ^


#the second frame contents
frame_cent = Frame(container)
frame_cent.place(relwidth=1, relheight=1)

#--- Enter date window
Label(frame_cent, text="Year:").grid(row=0, column=0, sticky="WE")
year_entry = Entry(frame_cent)
year_entry.grid(row=1, column=0)

Label(frame_cent, text="Month:").grid(row=2, column=0)
month_entry = Entry(frame_cent)
month_entry.grid(row=3, column=0)

Label(frame_cent, text="Day:").grid(row=4, column=0)
day_entry = Entry(frame_cent)
day_entry.grid(row=5, column=0)

submit_button = Button(frame_cent, text="Submit", command=get_future_date)
submit_button.grid(row=6, column=0)

result_label = Label(frame_cent, text="")
result_label.grid(row=7, column=0)
Button(frame_cent, text="Back", command=lambda: show_frame(frame_main)).grid(row=8, column=0)#takes me back to the main frame



# Show main frame when proram starts
show_frame(frame_main)
root.mainloop()