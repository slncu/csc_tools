from tkinter import filedialog

dir = './'
fld = filedialog.askdirectory(initialdir = dir) 

print(fld)