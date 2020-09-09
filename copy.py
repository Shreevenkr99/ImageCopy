##IMPORTING LIBRARIES
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter.filedialog import askopenfile
from ttkthemes import themed_tk as tk
from io import BytesIO
import win32clipboard
from PIL import Image,ImageTk

##CREATING PARENT WINDOW WITH THEME
root=tk.ThemedTk()
root.title('Image Copy')
root.get_themes()
root.set_theme("radiance")
root.geometry('450x100') 

##DEFINING VARIABLES
font1=('Arial', 14, 'bold')

##DEFINING FUNCTIONS
def send_to_clipboard(clip_type, data):                                   #COPYING IMAGE TO CLIPBOARD
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()
    
def click(event):                                                         #FUNCTION FOR BINDING THE BUTTON WITH LEFT MOUSE BUTTON CLICK
    if event.widget['text'] == "Select Image":
            try:
                global path
                filename = askopenfile(initialdir = "/", title = "Select File", filetypes = [("all files","*.*")])            #THE FORMAT OF FILENAME WILL BE TEXTIOWRAPPER CLASS
                filelist = str(filename)
                print(filelist)
                path = filelist[25:-29]                                   #EXTRACTING THE FILE PATH FROM TEXTIOWRAPPER FORMAT
                print(path)
                selectionCnfrm = Label(root, text = "Selection Finished")
                selectionCnfrm.grid(row = 2, column = 0)
            except EXCEPTION as error:
                messagebox.error("error", error) 

    if event.widget['text'] == "Import Image":                           
        try:    
            global image1
            image1 = Image.open(path)
            copyCnfrm.grid_remove()
            importCnfrm = Label(root, text = "Import Finished")
            importCnfrm.grid(row = 2, column = 1)
            img = PhotoImage(file=r"C:\\Users\\bsbha\\Pictures\\bhupender.png")
        except EXCEPTION as error:
                messagebox.error("error", error)        
        
    if event.widget['text'] == "Copy Image":
        output = BytesIO()
        image1.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.seek(0)
        output.close()
        send_to_clipboard(win32clipboard.CF_DIB, data)
        copyCnfrm.grid(row = 2, column = 2)

##CREATING STYLE
btnStyle = ttk.Style()
btnStyle.configure("NS.TButton",font = font1, border = 0)        
        
##CREATING WIDGETS
selectImgBtn = ttk.Button(root, text = "Select Image")
selectImgBtn.grid(row = 0, column = 0, padx = 10, pady = 10)
selectImgBtn.bind("<Button-1>", click)
getImageBtn = ttk.Button(root, text = "Import Image")
getImageBtn.grid(row = 0, column = 1, padx = 10, pady = 10)
getImageBtn.bind("<Button-1>", click)
copyImageBtn = ttk.Button(root, text = "Copy Image")
copyImageBtn.grid(row = 0, column = 2, padx = 10, pady = 10)
copyImageBtn.bind("<Button-1>", click)
copyCnfrm = Label(root, text = "Copying Finished")

root.mainloop()
