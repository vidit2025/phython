from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Setting up main window
root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

# Adding Image and labels in the main window 
upload = Image.open("app_img.jpg")
#resize the image using resize() method
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(root,
               text="Hey User! welcome to Denomination couter application.",
               bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

#Function to display a messagebox and proceed if OK is clicked 
def msg():
    Msgbox = messagebox.showinfo(
        "Alert", "Do you want to calculate The Denomination count?")
    if Msgbox == 'ok' :
        topwin()

#Adding buttons to the main window 
button1         
