from tkinter import *
import tkinter as tk
from tkinter import ttk
import sys
import random
from bubbleSort import Bsort
from mergesort import merge_sort
from quicksort import quick_sort

running=True


root=tk.Tk()
root.title('sorting algorithms')
root.maxsize(800,600)
root.iconbitmap(r'C:\Users\lee\Pictures\Logo.png')
#variable
selected_alg = StringVar()
data=[]


#functions
def drawdata(data,colorArray):
    canvas.delete("all")
    c_height=400
    c_width=600
    x_width=c_width / (len(data)+1)
    offset=20
    spacing=10
    n_data=[i / max(data) for i in data]
    
    for i, height in enumerate(n_data):
        #top left
        x0=i * x_width + offset+spacing
        y0=c_height-height*340
        #bottom right
        x1=(i+1)*x_width+offset
        y1=c_height

        canvas.create_rectangle(x0, y0,x1, y1,fill=colorArray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]))

    root.update_idletasks()
def generate():
    global data

    minval=int(minentry.get())
    maxval=int(maxentry.get())
    size=int(sizeentry.get())

    data=[]
    for _ in range(size):
        data.append(random.randrange(minval,maxval+1))
        drawdata(data,['red' for x in range(len(data))])#each box painted with red color



def startalgorithm():
    global data
    
    if algmenu.get() =='Bubble sort':
       Bsort(data, drawdata, speedscale.get())
    elif algmenu.get() =='Merge sort':
        merge_sort(data,drawdata,speedscale.get())
    elif algmenu.get() =='Quick sort':
        quick_sort(data,0,len(data)-1,drawdata,speedscale.get())

    drawdata(data, ['green' for x in range(len(data))])

    
    




#frame/ base lauout
top=Frame(root,borderwidth=2,relief='solid') #top frame
bottom=Frame(root,borderwidth=2,relief='solid') #bottom frame
top.grid(pady=10)
bottom.grid()
canvas=Canvas(top,width=800,height=350,bg='#E5E4E2')#container for top frame
canvas.create_text(400,20,text='This is a visulation for Sorting algorithms. We have used different kinds of algorithms for sorting data')#adding text to canvas
canvas.pack(fill=X,padx=10,pady=5)

#frame alignment/arranging things

#algorithm selection
Label(bottom,text="algorithm",bg="grey").grid(row=0,column=0,padx=5,pady=5)
algmenu=ttk.Combobox(bottom,textvariable=selected_alg,values=['Bubble sort','Merge sort','Quick sort'])
algmenu.grid(row=0,column=1,padx=5,pady=5)
algmenu.current(0)

#scale for speed
speedscale=Scale(bottom,from_=0.1,to=2.0,length=200,digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
speedscale.grid(row=0,column=2,padx=5,pady=5)

#scale for sizeentry
sizeentry=Scale(bottom,borderwidth=2,from_=3,to=25,resolution=1,orient=HORIZONTAL, label="Data Size")
sizeentry.grid(row=1,column=0,padx=5,pady=5)

#scale for min values to sort
minentry=Scale(bottom,from_=1,to=10,resolution=1,orient=HORIZONTAL, label="min value")
minentry.grid(row=1,column=1,padx=5,pady=5)

#scale for max values to sort
maxentry=Scale(bottom,from_=10,to=100,resolution=1,orient=HORIZONTAL, label="max values")
maxentry.grid(row=1,column=2,padx=5,pady=5)

#buttons
Button(bottom,text="start",bg='#646D7E',width=20,command=startalgorithm).grid(row=2,column=1,padx=10,pady=10)

Button(bottom,text="generate",bg='#306754',width=20,command=generate).grid(row=2,column=2,padx=10,pady=10)



root.mainloop()

