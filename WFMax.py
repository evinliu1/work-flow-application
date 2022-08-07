# for the GUI
import tkinter as tk
# for elements in application
from tkinter import filedialog, Text
from tkinter import *
from PIL import ImageTk, Image

# allows us to run apps
import os

# root is like our HTML body where the elements are attatched to
root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
        

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
    filetypes = (("executables","*.exe"),("all files","*.*")))

    apps.append(filename)

    for app in apps:
        label = tk.Label(frame, text = app, bg = "gray")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)

bg = PhotoImage(file="background.gif")

canvas = tk.Canvas(root, height=700, width=700, bg='white')
canvas.create_image(20,20,anchor=NW, image = bg)
canvas.pack()

frame = tk.Canvas(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx = 0.1, rely = 0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()


for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

# in order to run our application
root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')