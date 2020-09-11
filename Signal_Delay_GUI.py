from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
# main window
win = tk.Tk()
## added icon on gui will work on windows only
# p1 = PhotoImage(file = 'think.png')
# win.iconphoto(False, 'think.png')

# background color for gui
win.configure(background='#96e4f7')

# this for getting OPTIONS to gui text box
def change(*kwargs):
    box4 = OPTIONS[variable.get()]   # to get the valus of OPTIONS dict
    if variable.get() == 'RED': #checking
        # for box
        box.config(state=NORMAL) # this is used to disable the text box when user select something from OPTIONS menu
        box.delete(0.0,tk.END)
        box.insert(0.0,variable.get()) # if it match then box will get the key of dict
        box.config(state=DISABLED) # it will get disabled after selectin OPTINX menu
        # for box1
        box1.config(state=NORMAL)
        box1.delete(0.0,tk.END)
        box1.insert(0.0,box4) # if it match then box1 will get the value of dict
        box1.config(state=DISABLED)

    elif variable.get() == 'GREEN':
        box.config(state=NORMAL)        
        box.delete(0.0,tk.END)
        box.insert(0.0,variable.get())
        box.config(state=DISABLED)
        box1.config(state=NORMAL)
        box1.delete(0.0,tk.END)
        box1.insert(0.0,box4)
        box1.config(state=DISABLED)

    elif variable.get() == 'YELLOW':
        box.config(state=NORMAL)
        box.delete(0.0,tk.END)
        box.insert(0.0,variable.get())
        box.config(state=DISABLED)
        box1.config(state=NORMAL)
        box1.delete(0.0,tk.END)
        box1.insert(0.0,box4)
        box1.config(state=DISABLED)

win.title('User Data')
win.resizable(False,False)

# OPTIONS for optionmenu 
OPTIONS = {
    '': 'Select',
    'RED':10,
    'GREEN':30,
    'YELLOW':90,
}


# for getting the default value
def_variable = ''
# storing the options into variable
variable = tk.StringVar(win) 
# for default value
default = OPTIONS[def_variable]
variable.set(default)
# fro using the function 'change'
variable.trace('w',change)

# assigning the optionmenu to gui
w = tk.OptionMenu(win, variable, *OPTIONS)
w.grid(columnspan=2,column=0,row=0,pady=5,sticky='ne')
# configured the optionmenu
w.config(font=('calibri',(10)),bg='#aeefd7',width=15)

# labels for showing the key values
# # added some colors here
label = tk.Label(win,text="Existing Delay :",width="30",font="22",bg="#e86195")
label.grid(row=1,column=0,columnspan=3,pady=10)
box = Text(win,width=20,height=1,insertbackground="red",font=('bold',14))
box.grid(row=2,column=0,pady=5,padx=15)
box1 = Text(win,width=20,height=1,insertbackground="red",font=('bold',14))
box1.grid(row=2,column=1,pady=5,padx=5,columnspan=2)

# labels for storing the new value
# # added some colors here
label2 = tk.Label(win,text="New Label :",width="30",font="22",bg="#e86195")
label2.grid(row=3,column=0,columnspan=3,pady=10)
box2 = Entry(win,highlightcolor="#c078ed",font=('bold',14))
box2.grid(row=4,column=1,columnspan=2)

# submit function
def sbtn():
    try:
        # getting the both text 'box' value and the user entered value
        add = int(box2.get())
        inpu = box.get(0.0,tk.END)
        # this to \n which we getting from line no.84 becoz of 'END'
        a = inpu.replace('\n','')
        # updating the dict value by user inserted value
        OPTIONS.update({a:add})
        # to clear the box2 after submiting of value
        box2.delete(0,tk.END)
        # for getting the new dictionary
        print(OPTIONS)
        # to show message
        m_box.showinfo('Result','Information Updated Successfully')
    except ValueError:
        m_box.showerror('Error','Please Enter The Numbers Only')
# button
btn = ttk.Button(win,text="Submit",command=sbtn)
btn.grid(row=5,column=1,pady=5,sticky='ne')

# to close the window
def close():
    win.destroy()
# button1
btn1 = ttk.Button(win,text="Close",command=close)
btn1.grid(row=5,column=0,pady=5)

# styling for the buttons
style = ttk.Style()
# changing the theme of the buttons
style.theme_use('clam')

# configuration for button
style.configure('btn1.TButton', font=('calibri', 10, 'bold', 'underline'),background="red")
btn1.configure(style='btn1.TButton')

# configuration for button1
style.configure('btn.TButton', font=('calibri', 10, 'bold', 'underline'),background="green")
btn.configure(style="btn.TButton")

win.mainloop()