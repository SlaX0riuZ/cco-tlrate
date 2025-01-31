import tkinter as tk
from tkinter import messagebox

'''
Your task is to create a multi-window app that passes data from one window to another. App must include at minumum:

2 windows
Background Colors
App Favicon
2 text boxes
2 Buttons
1 Relevant and Purposeful Image
Graphing of data
Extra Credit Awarded for Creativity
'''
# Input: [Bsidebool, Slatedbool, combinedholeytier, combinedpizzatier, tallycap] so 5 buttons
# /////////////////////////////// Initialize Window
winmain = tk.Tk()
winmain.title('CCO-tsrate')
winmain.geometry('300x300')
winmain.config(bg='#8FD032')
winmain.resizable(False, False)
winmain.iconbitmap('greencube.ico')
# /////////////////////////////// Initialize Variables
bsidevar = tk.IntVar()
slatedvar = tk.IntVar()
htier = 0
ptier = 0
tcap = 0
# ///////////////////////////////
tk.Label(winmain, text='Tally Laborer Calculator for CCO').place(x=10,y=10)
tk.Label(winmain, text='Cube Input Section').place(x=10,y=40)

tk.Label(winmain, text='Check box if Collector\'s is B-Side.',relief='raised').place(x=10,y=70,height=25)
bside_cb = tk.Checkbutton(winmain, text='B-Side?', variable=bsidevar, onvalue=1, offvalue=0)
bside_cb.config(bg='#61A53F',selectcolor='#C4F129', relief='raised')
bside_cb.place(x=200,y=70)

tk.Label(winmain, text='Check box if Collector\'s is Slated.',relief='raised')
slated_cb = tk.Checkbutton(winmain, text='Slated?', variable=slatedvar, onvalue=1, offvalue=0)
slated_cb.config(bg='#61A53F',selectcolor='#C4F129', relief='raised')

tk.Label(winmain, text='Input Combined Tier of Holeys: ',relief='raised')
tk.Entry(winmain,relief='raised')
bside_cb.flash()
slated_cb.flash()
winmain.mainloop()