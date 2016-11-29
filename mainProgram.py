'''
Created on 21-Oct-2016

@author: rakshika
'''

from Tkinter import *
from PIL import ImageTk, Image
from tkFileDialog import askopenfilename

def geomVis():
    print "Geometry Visualizer"
    
def edgeDet():
    
    print "Edge detection algorithm"
    
    mainUI.pack_forget()
    MainUI.destroy(mainUI)

    edgeDetUI = EdgeDetUI(window)
    edgeDetUI.pack()
    #edgeDetUI.place(x=700, y=0)
    
def openFile():
    print "Opening a file"
    
    global imageLabel
    
    #Open a file dialog
    filename = askopenfilename()
    
    try:
        imageLabel
        
    except NameError:
        print "Not defined"
        
    else:
        imageLabel.pack_forget()
    
    #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    photo = ImageTk.PhotoImage(Image.open(filename))
    
    #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    
    imageLabel = Label(window, image = photo)
    imageLabel.image = photo
    imageLabel.pack()
    
def clearWindow():
    
    print "Clearing the window"
    
    global imageLabel
    global r1, r2, r3, r4
    
    r1.pack_forget()
    r2.pack_forget()
    r3.pack_forget()
    r4.pack_forget()
    
    try:
        imageLabel
    except NameError:
        print "Not defined"
    else:
        imageLabel.pack_forget()
    
    mainUI = MainUI(window)
    mainUI.pack()
    
class MainUI(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master, relief=SUNKEN, bd=2)

        self.menubar = Menu(self)

        modeMenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Mode", menu=modeMenu)
        modeMenu.add_command(label="Geometry Visualizer", command=geomVis)
        modeMenu.add_command(label="Edge detection algorithm", command=edgeDet)        

        try:
            self.master.config(menu=self.menubar)
        except AttributeError:
            # master is a toplevel window (Python 1.4/Tkinter 1.63)
            self.master.tk.call(master, "config", "-menu", self.menubar)
            
    
class EdgeDetUI(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master, relief=SUNKEN, bd=2)

        self.menubar = Menu(self)

        modeMenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Mode", menu=modeMenu)
        modeMenu.add_command(label="Geometry Visualizer", command=geomVis)
        modeMenu.add_command(label="Edge detection algorithm", command=edgeDet)
        
        fileMenu = Menu(self. menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="Open", command=openFile)
        
        windowMenu = Menu(self. menubar, tearoff=0)
        self.menubar.add_cascade(label="Window", menu=windowMenu)
        windowMenu.add_command(label="Clear", command=clearWindow)
        

        try:
            self.master.config(menu=self.menubar)
        except AttributeError:
            # master is a toplevel window (Python 1.4/Tkinter 1.63)
            self.master.tk.call(master, "config", "-menu", self.menubar)
            
        v = IntVar()
        
        global r1, r2, r3, r4
        r1 = Radiobutton(window, text="Initial image", variable=v, value=1)
        r1.pack(anchor=W)
        r2 = Radiobutton(window, text="Pre-processed Image", variable=v, value=2)
        r2.pack(anchor=W)
        r3 = Radiobutton(window, text="Gray-scaled image", variable=v, value=3)
        r3.pack(anchor=W)
        r4 = Radiobutton(window, text="Edge detection algorithm", variable=v, value=4)
        r4.pack(anchor=W)



window = Tk()
window.title("Visualization Software")
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (w, h))
window.configure(background='grey')

global edgeDetUI
global imageLabel

mainUI = MainUI(window)
mainUI.pack()

window.mainloop()
