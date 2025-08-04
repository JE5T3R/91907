#displaying images
'''# taken code from -https://www.geeksforgeeks.org/python/how-to-add-an-image-in-tkinter/-
from tkinter import *
from tkinter import PhotoImage

parent = Tk()
parent.title("Image in Tkinter")

# Load the image 
image = PhotoImage(file="Images/TestImg.png")

# Create a label to display the image
image_label = Label(parent, image=image)
image_label.pack()

# Start the Tkinter event loop
parent.mainloop()'''

#Basic layout
'''
from tkinter import *
from datetime import date
import json



root = Tk()
radio_var = StringVar()
root.title = "Task Manager"

health = 100
today = date.today()



my_frame = Frame(root, borderwidth=2, relief="solid", padx=10, pady=10)
my_frame.pack(pady=20) # Use pack to position the frame in the root window

label1 = Label(my_frame, text="Task manager", bg="lightblue", borderwidth=1, relief="solid", font="ARIAL 20")
label1.grid(row=0, column=0, padx=5, pady=5)



label2 = Label(my_frame, text="Task Name", bg="lightblue", borderwidth=1, relief="solid", font="ARIAL 12")
label2.grid(row=1, column=0, padx=5, pady=5)

taskname = Entry(my_frame, bg="lightblue", borderwidth=1, relief="solid", font="ARIAL 18", width=20)
taskname.grid(row=2, column=0, padx=5, pady=(5, 30))




date_label = Label(my_frame, text=today, font="Arial 15")
date_label.grid(row=3, column=0, padx=20, pady=20)




label3 = Label(my_frame, text="Task Discription", bg="lightblue", borderwidth=1, relief="solid", font="ARIAL 12")
label3.grid(row=4, column=0, padx=5, pady=5)

discription = Text(my_frame, bg="lightblue", borderwidth=1, relief="solid", font="ARIAL 18", width=20, height=5)
discription.grid(row=5, column=0, padx=5, pady=(5, 30))



label4 = Label(my_frame, text=health, bg="lightblue", borderwidth=1, relief="solid", font="ARIAL 12")
label4.grid(row=6, column=1, padx=5, pady=5)


root.mainloop()
'''


#Entering a date in the future
#some code from -https://www.geeksforgeeks.org/python/create-a-date-picker-calendar-tkinter/-

from tkinter import *
from datetime import date

root = Tk()

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

root = Tk()
root.title("Enter A Future Date")

Label(root, text="Year:").pack()
year_entry = Entry(root)
year_entry.pack()

Label(root, text="Month:").pack()
month_entry = Entry(root)
month_entry.pack()

Label(root, text="Day:").pack()
day_entry = Entry(root)
day_entry.pack()

submit_button = Button(root, text="Submit", command=get_future_date)
submit_button.pack()

result_label = Label(root, text="")
result_label.pack()

root.mainloop()

#frames and switching between them
'''
#Code taken from my earlier code in the year for a temperature converter
from tkinter import *

root = Tk()
root.title("Temperature Converter")
root.geometry("400x200")
root.resizable(0, 0)

style = "Arial 15"

# Function to raise a frame
def show_frame(frame):
    frame.tkraise()


# -------- Main container frame ----------
container = Frame(root)
container.pack(fill="both", expand=True)

# --------- Frame 1: Main Menu ----------
frame_main = Frame(container)
frame_main.pack(fill = X)



# Button row (L and R side-by-side)
button_frame = Frame(frame_main)
button_frame.pack()

#Takes you to the second frame
btn_cent = Button(button_frame, text="to Centigrade", bg="yellow", font=style, command=lambda: show_frame(frame_cent))
btn_cent.pack(side=LEFT, padx=10)


#the second frame contents
frame_cent = Frame(container)
frame_cent.pack(fill = X)

Label(frame_cent, text="Enter temperature in Fahrenheit", font=("Arial", 18)).pack(pady=20)
Button(frame_cent, text="Back", command=lambda: show_frame(frame_main)).pack()#takes me back to the main frame


# Show main frame when proram starts
show_frame(frame_main)

root.mainloop()'''

#Using Json files
'''import tkinter as tk
import json
import os 

def save_to_json():
    #takles the 3 inputs fro the user and then saves the inputs as a string which is used in adding the inputs in a dictionary in the Json file
    input1_data = entry1.get()
    input2_data = entry2.get()
    input3_data = entry3.get()

    # Layout for the dictionary in the json file
    new_entry = {
        input1_data, {
        "Task Discription": input2_data,
        "Due Date": input3_data}
    }

    file_name = "TaskManagerV1json"
    data = [] #adds inputs into a dictionary in the python file, I dont remener why but yk

   

    # makes sure tht the user input is a list to append to
    if not isinstance(data, list):
        data = [] # Reset if it's not a list
#inputs the user inputs into the json file
    data.append(new_entry)

    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)

#After pressing save, the entry boxes will have the information deleted and be ready for new inputs
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)

    status_label.config(text="Data saved successfully!")

root = tk.Tk()
root.title("User Input to JSON")

#  Labels and Entry boxes
tk.Label(root, text="Task Name:").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Task Description:").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Due date:").grid(row=2, column=0, padx=5, pady=5)
entry3 = tk.Entry(root)
entry3.grid(row=2, column=1, padx=5, pady=5)

# Save to json Button
save_button = tk.Button(root, text="Save to JSON", command=save_to_json)
save_button.grid(row=3, column=0, columnspan=2, pady=10)

# words that apear when user wants to save file
status_label = tk.Label(root, text="")
status_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
'''


#-----------------------------------
#-----------------------------------
#-----------------------------------
#posable add ons for future versions
#-----------------------------------
#-----------------------------------
#-----------------------------------


#Cheking if the file exists or not
#formed together from multaple sources in the internet, not sure if it works yet
''' if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
    try:
        with open(file_name, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        data = []'''