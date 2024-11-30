from tkinter import *
from tkinter import messagebox
import json
from os import path

tasks = []

def set_placeholder(entry, placeholder_text):
    def on_entry_click(event):
        if entry.get() == placeholder_text:
            entry.delete(0, END)
            entry.config(fg='white')

    def on_focusout(event):
        if entry.get() == '':
            entry.insert(0, placeholder_text)
            entry.config(fg='white')

    entry.insert(0, placeholder_text)
    entry.config(fg='white')
    entry.bind('<FocusIn>', on_entry_click)
    entry.bind('<FocusOut>', on_focusout)

def load():
    global tasks
    try:
        with open(path.expanduser("~\\AppData\\Roaming\\todo.json"), "r") as file:
            tasks = json.load(file)
            for task in tasks:
                listbox.insert(0, task)
    except FileNotFoundError:
        pass

def deltask():
    global tasks
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)   
        tasks.pop(index)

        with open(path.expanduser("~\\AppData\\Roaming\\todo.json"), "w+") as file:
            json.dump(tasks, file, indent=4)
    else:
        messagebox.showinfo("Info", "First, highlight any task")

def addtask():
    global tasks
    task = entry.get()
    if task:
        listbox.insert(END, task)
        entry.delete(0, END)
        tasks.append(task)
        with open(path.expanduser("~\\AppData\\Roaming\\todo.json"), "w+") as file:
            json.dump(tasks, file, indent=4)
    else:
        messagebox.showinfo("Info", "First, enter any task")

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

root = Tk()
root.geometry("300x280")
root.configure(bg="#75e0f0")
root.resizable(False, False)
root.title("Maya4ok's TODO")

delbtn = Button(text="Delete", command=deltask, relief=FLAT, bg="#FF6347", fg="#FFFFFF", 
                font=("Roboto Medium", 16), width=11, activebackground="#eb4325", activeforeground="#FFFFFF")
delbtn.place(rely=0.1, relx=0.25, anchor=CENTER)
addbtn = Button(text="Add", command=addtask, relief=FLAT, bg="#007FFF", fg="#FFFFFF", 
                font=("Roboto Medium", 16), width=11, activebackground="#1573d2", activeforeground="#FFFFFF")
addbtn.place(rely=0.1, relx=0.75, anchor=CENTER)
listbox = Listbox(font=("Roboto Medium", 16), bg="#756df0", height=7, highlightbackground="#007FFF",
                  relief=FLAT, highlightthickness=2,highlightcolor="#75aeef", fg="#ffffff", activestyle="none",)
listbox.pack(side="bottom", pady=3, padx=5, fill="both")
entry = Entry(bg="#756df0", fg="#ffffff", font=("Roboto Medium", 16), highlightbackground="#007FFF",
               relief=FLAT, highlightthickness=2,highlightcolor="#75aeef")
entry.pack(side="bottom", pady=5, padx=5, fill="x")

set_placeholder(entry, "Enter your task name here...")
load()
center_window(root)

root.mainloop()