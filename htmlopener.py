from tkinter import *
from tkinter import filedialog
import webbrowser

files = []
def runm():
    for i in range(len(files)):
        webbrowser.open(files[i], 2)
def run():
    one = files[0]
    webbrowser.open(one, 2)
    files.remove(one)
    files.append(one)
def select():
    ope.filename = filedialog.askopenfilename(title = "Open html")
    files.append(ope.filename)
ope = Tk()
s = Button(ope, text = "Select", command = select)
sm = Button(ope, text = "Select more", command = select)
r = Button(ope, text = "Run", command = run)      
rm = Button(ope, text = "Run all", command = runm)

s.pack()
sm.pack()
r.pack()
rm.pack()
mainloop()