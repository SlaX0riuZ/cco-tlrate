import tkinter as tk
import math as math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
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
# /////////////////////////////// [INITIALIZE WINDOW]
winmain = tk.Tk()
winmain.title('Tally Laborer - Input')
winmain.geometry('300x300')
winmain.config(bg='#8FD032')
winmain.resizable(False, False)
winmain.iconbitmap('greencube.ico')
# /////////////////////////////// [INITIALIZE VARIABLES]
bsidevar = tk.IntVar()
slatedvar = tk.IntVar() # Checkboxes can only manipulate .IntVar variable types
nfile = open('fixeddata.txt', 'a') # nfile used to append to fixeddata
# /////////////////////////////// [COMMANDS]
def senddata():
    bbool = '0' # Temporary variables; should be 0 each time senddata() is used
    sbool = '0'
    try:
        if str(bsidevar) == 'PY_VAR1': # Both if statements are used to convert the .IntVar string to a numerical one
            bbool = '1'
        if str(slatedvar) == 'PY_VAR1':
            sbool = '1'
        htier = holey_txt.get() # get combined holey
        ptier = pizza_txt.get() # get combined pizza
        nfile.write('\n') # newline
        nfile.write(bbool + 'S' + sbool + 'H' + htier + 'P' + ptier) # data storage format
    except:
        err_lbl.config(text='Error with sending data. \nMake sure ALL DATA is numbers.')

def clearallconfirm(): # function to open confirmation window
    # Initialize window "winconfirm" from winmain
    winconfirm = tk.Toplevel(winmain)
    winconfirm.geometry('200x200')
    winconfirm.config(bg='#61A53F')
    winconfirm.title('CONFIRM DATA ERASURE')
    winconfirm.iconbitmap('greencube.ico')
    # Respective commands for "YES" click and "NO" click
    def wcdestroy():
        winconfirm.destroy()
    def wcconfirm():
        open('fixeddata.txt','w').write('') # Clearing the file
        wcdestroy()
    # Setup confirmation label and buttons
    tk.Label(winconfirm, text='Are you sure you want to \n erase all data to file? \n This includes all previous entries.').place(x=10, y=10)
    tk.Button(winconfirm, text='NO', command=wcdestroy).place(x=50,y=100)
    tk.Button(winconfirm, text='YES', command=wcconfirm).place(x=120,y=100)

def graphdata(): # function to graph the data
    # Initialize window "wingraph" from winmain
    wingraph = tk.Toplevel(winmain)
    wingraph.geometry('500x500')
    wingraph.title('GRAPHED OUTPUT')
    wingraph.iconbitmap('greencube.ico')
    wingraph.config(bg='#61A53F')
    # Declare initial variables
    tcps = 0 # tally credits per spin
    rfile = open('fixeddata.txt', 'r') # readonly
    try:
        filelines = rfile.readlines()
        for fline in range(len(filelines)):
            ffl = filelines[fline]
            hindex = ffl[ffl.index('H')+1:ffl.index('P')]
            print(str(hindex))
            pindex = ffl[ffl.index('P'):]
            if fline[2] == '1': # Check type
                tcps = tcps + math.ceil(((1.4 * (hindex + 1)) * (1.4 * pindex * 1.2)) * 0.4) # using string slicing, add calculation to tcps
            else:
                tcps = tcps + math.ceil((hindex+1) * (pindex * 1.2)) # again, but if type did not pass slated check
    except:
        wingraph.destroy()
        err_lbl.config(text='Error with graphing. \nTry clearing and re-inputting all data.')
    try:
        xaxisnames = ['+1', '+2', '+3', '+4', '+5', '+6', '+7', '+8', '+9']
        yvalues = [1680, 3920, 6720, 10080, 14000, 18480, 23520, 29120, 35280]
        plt.bar(xaxisnames, yvalues)
        plt.show()
    except:
        wingraph.destroy()
        err_lbl.config(text='Error with graphing inputs.\n Make sure all inputs are numbers.')

# /////////////////////////////// [WINDOW SETUP]
# Respective title label
tk.Label(winmain, text='Tally Laborer Calculator for CCO').place(x=10,y=10)
# Checkbox and label setup for B-Side Boolean
tk.Label(winmain, text='Check box if Collector\'s is B-Side.',relief='raised').place(x=10,y=70,height=25)
bside_cb = tk.Checkbutton(winmain, text='B-Side?', variable=bsidevar, onvalue=1, offvalue=0)
bside_cb.config(bg='#61A53F',selectcolor='#C4F129', relief='raised')
bside_cb.place(x=200,y=70)
# Checkbox and label setup for Slated Boolean
tk.Label(winmain, text='Check box if Collector\'s is Slated.',relief='raised').place(x=10,y=100,height=25)
slated_cb = tk.Checkbutton(winmain, text='Slated?', variable=slatedvar, onvalue=1, offvalue=0)
slated_cb.config(bg='#61A53F',selectcolor='#C4F129', relief='raised')
slated_cb.place(x=200,y=100)
# Label and respective input for Holey Sigils
tk.Label(winmain, text='Input Combined Tier of Holeys: ',relief='raised').place(x=10,y=140)
holey_txt = tk.Entry(winmain,relief='raised')
holey_txt.place(x=200,y=140,width=90)
# Label and respective input for Pizza Sigils
tk.Label(winmain, text='Input Combined Tier of Pizzas: ',relief='raised').place(x=10,y=170)
pizza_txt = tk.Entry(winmain,relief='raised')
pizza_txt.place(x=200,y=170,width=90)
# Sending Data Button
send_bn = tk.Button(winmain,relief='raised',text='Store Inputs',command=senddata)
send_bn.place(x=10,y=200)
# Clearing File Button
clearfile_bn = tk.Button(winmain,relief='raised',text='CLEAR ALL DATA',command=clearallconfirm)
clearfile_bn.place(x=90,y=200)
# Graphing Button
graphdata_bn = tk.Button(winmain,relief='raised',text='Graph All Data',command=graphdata)
graphdata_bn.place(x=200,y=200)
# Error Handling Label
err_lbl = tk.Label(winmain,text='ERROR HANDLER', font=('Arial', 10))
err_lbl.place(x=10,y=240,width=280,height=40)
# /////////////////////////////// [UPDATES AND LOOPS]
# Update the Checkboxes using .flash()
bside_cb.flash()
slated_cb.flash()
# Mainloop
winmain.mainloop()