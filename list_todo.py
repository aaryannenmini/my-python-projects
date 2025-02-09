from tkinter import *
import tkmacosx as b
from tkinter import messagebox

todo = Tk()
todo.config(bg="darkgoldenrod1")
todo.geometry("250x450")

def addt():
    task = enter.get()
    if task:
        list.insert(END,task)
        enter.delete(0,END)
    else:
        messagebox.showwarning("Warning","You must enter a task before entering")

def removet():
    try:
        selectindex= list.curselection()[0]
        list.delete(selectindex)
    except IndexError:
        messagebox.showwarning("Warning","You must select a task to remove task")

def markt():
    try:
        selectindex= list.curselection()[0]
        task = list.get(selectindex)
        list.delete(selectindex)
        list.insert(END,f"{task}⭐️")
    except IndexError:
        messagebox.showwarning("Warning","It needs to be marked completed")

todolist = Label(todo,text="Todo List App",bg="darkgoldenrod1",fg="darkblue",font=("Arial bold",20))
enter = Entry(todo,bg="lightblue",fg="darkblue")
add= b.Button(todo,text="Add Item",bg="lightblue",fg="darkblue",command=addt)
remove = b.Button(todo,text="Remove Item",bg="lightblue",fg="darkblue",command=removet)
mark=b.Button(todo,text="Mark as Completed",bg="lightblue",fg="darkblue",command=markt)
list = Listbox(todo,selectmode=SINGLE,bg="lightblue",fg="darkblue")

todolist.pack(pady=20)
enter.pack(pady=10)
add.pack(pady=10)
remove.pack(pady=10)        
mark.pack(pady=10)
list.pack(pady=10)




todo.mainloop()