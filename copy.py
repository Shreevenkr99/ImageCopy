##IMPORTING LIBRARIES
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
from io import BytesIO
import win32clipboard
from PIL import Image,ImageTk

##CREATING PARENT WINDOW WITH THEME
root=tk.ThemedTk()
root.title('Image Copy')
root.get_themes()
root.set_theme("radiance")
root.geometry('300x110') 

##DEFINING VARIABLES
font1=('Arial', 14, 'bold')

##DEFINING FUNCTIONS
def send_to_clipboard(clip_type, data):                                   #COPYING IMAGE TO CLIPBOARD
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()
    
def click(event):                                                         #FUNCTION FOR BINDING THE BUTTON WITH LEFT MOUSE BUTTON CLICK
    if event.widget['text'] == "Import Image":
        try:    
            global image1
            image1 = Image.open(r"C:\\Users\\bsbha\\Pictures\\bhupender.png")
            copyCnfrm.grid_remove()
            importCnfrm = Label(root, text = "Import Finished")
            importCnfrm.grid(row = 2, column = 0)
            img = PhotoImage(file=r"C:\\Users\\bsbha\\Pictures\\bhupender.png")
            #canvas.create_image(40,20, anchor=NW, image=img)
        except EXCEPTION as error:
                messagebox.error("error", error)        
        
    if event.widget['text'] == "Copy Image":
        output = BytesIO()
        image1.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.seek(0)
        output.close()
        send_to_clipboard(win32clipboard.CF_DIB, data)
        copyCnfrm.grid(row = 2, column = 1)

##CREATING STYLE
btnStyle = ttk.Style()
btnStyle.configure("NS.TButton",font = font1, border = 0)        
        
##CREATING WIDGETS
##canvas = Canvas(root, width = 300, height = 300, border = 5)
##canvas.grid(row = 1, column = 0, padx = 40, pady = 20)
getImageBtn = ttk.Button(root, text = "Import Image")
getImageBtn.grid(row = 0, column = 0, padx = 10, pady = 10)
getImageBtn.bind("<Button-1>", click)
copyImageBtn = ttk.Button(root, text = "Copy Image")
copyImageBtn.grid(row = 0, column = 1, padx = 10, pady = 10)
copyImageBtn.bind("<Button-1>", click)
copyCnfrm = Label(root, text = "Copying Finished")

root.mainloop()
