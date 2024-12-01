from tkinter import *
from tkinter import messagebox
import json
from os import path
tasks = []

# функция для установки текста-подсказки в Entry
def set_placeholder(entry, placeholder_text):
    def on_entry_click(event):
        if entry.get() == placeholder_text:
            entry.delete(0, END)
            entry.config(fg='black')

    def on_focusout(event):
        if entry.get() == '':
            entry.insert(0, placeholder_text)
            entry.config(fg='grey')

    entry.insert(0, placeholder_text)
    entry.config(fg='grey')
    entry.bind('<FocusIn>', on_entry_click)
    entry.bind('<FocusOut>', on_focusout)

# функция для загрузки задач из файла
def load():
    global tasks
    try:
        with open(path.join(path.expanduser("~"), "todo.json"), "r") as file:
            tasks = json.load(file)
            for task in tasks:
                listbox.insert(END, task)
    except FileNotFoundError:
        pass

# функция для удаления задачи
def deltask():
    global tasks
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        tasks.pop(index)

        with open(path.join(path.expanduser("~"), "todo.json"), "w") as file:
            json.dump(tasks, file, indent=4)
    else:
        messagebox.showinfo("Info", "First, highlight any task")

# функция для добавления новой задачи
def addtask():
    global tasks
    task = entry.get()
    if task == "Enter your task name here..." or task.strip() == "":
        messagebox.showinfo("Info", "First, enter any task")
    else:
        listbox.insert(END, task)
        entry.delete(0, END)
        tasks.append(task)
        with open(path.join(path.expanduser("~"), "todo.json"), "w") as file:
            json.dump(tasks, file, indent=4)

# функция для центрирования окна
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

# инициализация основного окна
root = Tk()
root.geometry("300x280")
root.configure(bg="#e0f7fa") # светло-голубой фон
root.resizable(False, False)
root.title("Maya4ok's TODO")

# кнопка "Delete"
delbtn = Button(text="Delete", command=deltask, relief=FLAT, bg="#ff5252", fg="#FFFFFF", # красный фон
                font=("Roboto Medium", 16), width=11, activebackground="#ff1744", activeforeground="#FFFFFF")
delbtn.place(rely=0.1, relx=0.25, anchor=CENTER)

# кнопка "Add"
addbtn = Button(text="Add", command=addtask, relief=FLAT, bg="#4caf50", fg="#FFFFFF", # зелёный фон
                font=("Roboto Medium", 16), width=11, activebackground="#388e3c", activeforeground="#FFFFFF")
addbtn.place(rely=0.1, relx=0.75, anchor=CENTER)

# Listbox для задач
listbox = Listbox(font=("Roboto Medium", 16), bg="#b3e5fc", height=7, highlightbackground="#75aeef", # светло-синий фон
                  relief=FLAT, highlightthickness=2, highlightcolor="#007FFF", fg="#000000", activestyle="none")
listbox.pack(side="bottom", pady=3, padx=5, fill="both")

# Entry для ввода задач
entry = Entry(bg="#b3e5fc", fg="#000000", font=("Roboto Medium", 16), highlightbackground="#75aeef", # светло-синий фон
              relief=FLAT, highlightthickness=2, highlightcolor="#007FFF")
entry.pack(side="bottom", pady=5, padx=5, fill="x")

# установка placeholder
set_placeholder(entry, "Enter your task name here...")
# загрузка существующих задач
load()
# центрирование окна
center_window(root)

# запуск основного цикла Tkinter
root.mainloop()from tkinter import *
from tkinter import messagebox
import json
from os import path
tasks = []

# функция для установки текста-подсказки в Entry
def set_placeholder(entry, placeholder_text):
    def on_entry_click(event):
        if entry.get() == placeholder_text:
            entry.delete(0, END)
            entry.config(fg='black')

    def on_focusout(event):
        if entry.get() == '':
            entry.insert(0, placeholder_text)
            entry.config(fg='grey')

    entry.insert(0, placeholder_text)
    entry.config(fg='grey')
    entry.bind('<FocusIn>', on_entry_click)
    entry.bind('<FocusOut>', on_focusout)

# функция для загрузки задач из файла
def load():
    global tasks
    try:
        with open(path.join(path.expanduser("~"), "todo.json"), "r") as file:
            tasks = json.load(file)
            for task in tasks:
                listbox.insert(END, task)
    except FileNotFoundError:
        pass

# функция для удаления задачи
def deltask():
    global tasks
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        tasks.pop(index)

        with open(path.join(path.expanduser("~"), "todo.json"), "w") as file:
            json.dump(tasks, file, indent=4)
    else:
        messagebox.showinfo("Info", "First, highlight any task")

# функция для добавления новой задачи
def addtask():
    global tasks
    task = entry.get()
    if task == "Enter your task name here..." or task.strip() == "":
        messagebox.showinfo("Info", "First, enter any task")
    else:
        listbox.insert(END, task)
        entry.delete(0, END)
        tasks.append(task)
        with open(path.join(path.expanduser("~"), "todo.json"), "w") as file:
            json.dump(tasks, file, indent=4)

# функция для центрирования окна
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

# инициализация основного окна
root = Tk()
root.geometry("300x280")
root.configure(bg="#e0f7fa") # светло-голубой фон
root.resizable(False, False)
root.title("Maya4ok's TODO")

# кнопка "Delete"
delbtn = Button(text="Delete", command=deltask, relief=FLAT, bg="#ff5252", fg="#FFFFFF", # красный фон
                font=("Roboto Medium", 16), width=11, activebackground="#ff1744", activeforeground="#FFFFFF")
delbtn.place(rely=0.1, relx=0.25, anchor=CENTER)

# кнопка "Add"
addbtn = Button(text="Add", command=addtask, relief=FLAT, bg="#4caf50", fg="#FFFFFF", # зелёный фон
                font=("Roboto Medium", 16), width=11, activebackground="#388e3c", activeforeground="#FFFFFF")
addbtn.place(rely=0.1, relx=0.75, anchor=CENTER)

# Listbox для задач
listbox = Listbox(font=("Roboto Medium", 16), bg="#b3e5fc", height=7, highlightbackground="#75aeef", # светло-синий фон
                  relief=FLAT, highlightthickness=2, highlightcolor="#007FFF", fg="#000000", activestyle="none")
listbox.pack(side="bottom", pady=3, padx=5, fill="both")

# Entry для ввода задач
entry = Entry(bg="#b3e5fc", fg="#000000", font=("Roboto Medium", 16), highlightbackground="#75aeef", # светло-синий фон
              relief=FLAT, highlightthickness=2, highlightcolor="#007FFF")
entry.pack(side="bottom", pady=5, padx=5, fill="x")

# установка placeholder
set_placeholder(entry, "Enter your task name here...")
# загрузка существующих задач
load()
# центрирование окна
center_window(root)

# запуск основного цикла Tkinter
root.mainloop()
