#Day 23
#1Create a browse option with a specific folder which has all the JPEG Files & create a Convert button to convert the image from JPEG to PNG – Basic Image converter App

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
root = tk.Tk()
canvas1 = tk.Canvas(root, width=550, height=550, bg='white', relief='raised')
canvas1.pack()
label1 = tk.Label(root, text='Convert From JPEG To PNG')
label1.config(font=('Arial', 20))
canvas1.create_window(250,40, window=label1)
def getJPEG():
    global img1
    import_file_path = filedialog.askopenfilename()
    img1 = Image.open(import_file_path)
browseButton_JPG = tk.Button(text="       JPEG File     ", command=getJPEG, bg='red', fg='white',font=('Arial', 14, 'bold'))
canvas1.create_window(250, 200, window=browseButton_JPG)
def convToPNG():
    global img1
    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    img1.save(export_file_path)
saveAsButton_PNG = tk.Button(text='Convert JPG to PNG', command=convToPNG, bg='red', fg='white',font=('Arial', 14, 'bold'))
canvas1.create_window(250, 280, window=saveAsButton_PNG)
root.mainloop()



#2 Create two browse button and place the .pdf file for the buttons and create a merge pdf option -  Watermark Merger App



from tkinter import *
from tkinter import filedialog as fd
from PyPDF2 import PdfFileReader,PdfFileWriter,PdfFileMerger,PageRange


root = Tk()

#3 naming the GUI interface to image_conversion_APP
root.title("PDF APP ")

def merger():
	global pdf1,pdf2
	import1=fd.askopenfilename()
	pdf1=PdfFileReader(import1)
	import2=fd.askopenfilename()
	pdf2=PdfFileReader(import2)

	obj=PdfFileMerger()
	obj.append(pdf1,'rb')
	obj.append(pdf2,'rb')
	obj.write('mergedpdf.PDF')
  
 button1=Button(root,text="pdf merger",width=10,height=1,bg='blue',fg='white',font=('helvetica',10,'bold'),command=merger)
button1.grid(column=1,row=6)

root.geometry("500x500+400+200")
root.mainloop()