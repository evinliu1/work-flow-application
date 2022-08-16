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

root.geometry("700x800")
root.resizable(False,False)

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
        
def deletePaths():
    for widget in frame.winfo_children():
        widget.destroy()

    apps.clear()

    

def addApp():
    
    # destroys the elements in the frame to prevent redundancy
    for widget in frame.winfo_children():
        widget.destroy()
        
    # this allows us to select files that are executable and view all types of files
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
    filetypes = (("executables","*.exe"),("all files","*.*")))

    # after choosing the file, it would simply append the filename to the apps list we created
    apps.append(filename)

    # attaches the elements of the list to the frame
    for app in apps:
        label = tk.Label(frame, text = app, bg = "gray")
        label.pack()

# this method simply loops through the filepaths in the list we created and runs the files associated
def runApps():
    for app in apps:
        os.startfile(app)

# using PIL, I set an image that I chose and assigned it to 'bg'
bg = PhotoImage(file="background.gif")

# create a canvas that sets the dimensions of the application itself
canvas = tk.Canvas(root, height=600, width=800)
# this is where I assigned the value of the bg to the canvas background
canvas.create_image(0,0,anchor=NW, image = bg)
canvas.pack()

# this is the part of the GUI where I would display the app names, so I just made a frame and attached to root
frame = tk.Canvas(root, bg="white")
frame.create_image(0,0,anchor=NW, image = bg)
# I set the relative distance from top and bottom using relx, rely, relwidth, and relheight
# relheight and relwidth were 80% of the actual canvase size
# relx and rely were the distances from the top, bottom, left, and right of the canvas
frame.place(relwidth=0.8, relheight=0.8, relx = 0.1, rely = 0.1)

# i made an 'open file' button which referenced a method called addApp
openFile = tk.Button(root, text="Open File", padx=100, pady=5, bg="black", fg="white", command=addApp)
openFile.config(width=10)
openFile.pack()

# i made an 'run apps' button which referenced a method called runApps
runApps = tk.Button(root, text="Run Apps", padx=100, pady=5, bg="black", fg="white", command=runApps)
runApps.pack()
runApps.config(width=10)

# i made a 'delete path' button which referenced a method called deletePaths
deletePath = tk.Button(root, text="Clear Paths", padx=100, pady=5, bg="black", fg="white", command=deletePaths)
deletePath.pack()
deletePath.config(width=10)


for app in apps:
    label = tk.Label(frame, text=app, padx=200, fg="white", bg="black")
    label.pack()

# in order to run our application
root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
