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
# Input: [Bsidebool, Slatedbool, combinedholeytier, combinedpizzatier] so 4 buttons
# /////////////////////////////// Initialize Window
winmain = tk.Tk()
winmain.title('Tally Laborer - Input')
winmain.geometry('300x300')
winmain.config(bg='#8FD032')
winmain.resizable(False, False)
winmain.iconbitmap('greencube.ico')
# /////////////////////////////// Initialize Variables
bsidevar = tk.IntVar()
slatedvar = tk.IntVar()
nfile = open('fixeddata.txt', 'a') # nfile used to append to fixeddata
# ///////////////////////////////
def senddata():
    bbool = '0'
    sbool = '0'
    if str(bsidevar) == 'PY_VAR1':
        bbool = '1'
    if str(slatedvar) == 'PY_VAR1':
        sbool = '1'
    htier = holey_txt.get() # get combined holey
    ptier = pizza_txt.get() # get combined pizza
    nfile.write('\n') # newline
    nfile.write(bbool + '/' + sbool + '/' + htier + '/' + ptier) # data storage format

def clearallconfirm():
    winconfirm = tk.Toplevel(winmain)
    winconfirm.geometry('200x200')
    winconfirm.config(bg='#61A53F')
    winconfirm.title('CONFIRM DATA ERASURE')
    winconfirm.iconbitmap('greencube.ico')
    def wcdestroy():
        winconfirm.destroy()
    def wcconfirm():
        open('fixeddata.txt','w').write('')
        wcdestroy()
    tk.Label(winconfirm, text='Are you sure you want to \n erase all data to file? \n This includes all previous entries.').place(x=10, y=10)
    tk.Button(winconfirm, text='NO', command=wcdestroy).place(x=50,y=100)
    tk.Button(winconfirm, text='YES', command=wcconfirm).place(x=120,y=100)

def graphdata():
    wingraph = tk.Toplevel(winmain)
    wingraph.geometry('500x500')
    wingraph.title('GRAPHED OUTPUT')
    wingraph.iconbitmap('greencube.ico')
    wingraph.config(bg='#61A53F')
# ///////////////////////////////
tk.Label(winmain, text='Tally Laborer Calculator for CCO').place(x=10,y=10)

tk.Label(winmain, text='Check box if Collector\'s is B-Side.',relief='raised').place(x=10,y=70,height=25)
bside_cb = tk.Checkbutton(winmain, text='B-Side?', variable=bsidevar, onvalue=1, offvalue=0)
bside_cb.config(bg='#61A53F',selectcolor='#C4F129', relief='raised')
bside_cb.place(x=200,y=70)

tk.Label(winmain, text='Check box if Collector\'s is Slated.',relief='raised').place(x=10,y=100,height=25)
slated_cb = tk.Checkbutton(winmain, text='Slated?', variable=slatedvar, onvalue=1, offvalue=0)
slated_cb.config(bg='#61A53F',selectcolor='#C4F129', relief='raised')
slated_cb.place(x=200,y=100)

tk.Label(winmain, text='Input Combined Tier of Holeys: ',relief='raised').place(x=10,y=140)
holey_txt = tk.Entry(winmain,relief='raised')
holey_txt.place(x=200,y=140,width=90)

tk.Label(winmain, text='Input Combined Tier of Pizzas: ',relief='raised').place(x=10,y=170)
pizza_txt = tk.Entry(winmain,relief='raised')
pizza_txt.place(x=200,y=170,width=90)

send_bn = tk.Button(winmain,relief='raised',text='Store Inputs',command=senddata)
send_bn.place(x=50,y=200)

clearfile_bn = tk.Button(winmain,relief='raised',text='CLEAR ALL DATA',command=clearallconfirm)
clearfile_bn.place(x=150,y=200)

graphdata_bn = tk.Button(winmain,relief='raised',text='Graph All Data',command=graphdata)
graphdata_bn.place(x=100,y=240)

bside_cb.flash()
slated_cb.flash()
winmain.mainloop()