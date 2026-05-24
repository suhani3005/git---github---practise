import tkinter as tk
window = tk.Tk()
window.title("DSA Progress Tracker")
window.geometry("600x600")
window.configure(bg="#f0f0f0")
label = tk.Label(window, text="DSA Progress Tracker", font=("Arial", 20, "bold"), bg="#f0f0f0")
label.pack(pady=10)
entry = tk.Entry(window, width =40)
entry.pack(pady=15, ipady=3)
listbox = tk.Listbox(window, width=50)
listbox.pack(pady=10, ipadx=20, ipady=20)
def add():
    text = entry.get()
    if text !="":
        listbox.insert(tk.END, text)
        save_data()
def delete():
    selected = listbox.curselection()
    for  i in selected:
        listbox.delete(i)
        save_data()
def mark_solved():
    selected = listbox.curselection()
    for i in selected:
        item = listbox.get(i)
        listbox.delete(i)
        listbox.insert(i, "[SOLVED]" + item)
def save_data():
    tasks = listbox.get(0, tk.END)
    with open("progress.txt", "w")as file:
        for task in tasks:
            file.write(task + "\n")
def load_data():
    try:
        with open ("progres.txt", "r")as file:
            tasks = file.readlines()
        for task in tasks:
            listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass
btn_add = tk.Button(window, text="Add Problem", width=20, command=add)
btn_add.pack()
btn_delete = tk.Button(window, text="Delete Problem", width=20, command=delete)
btn_delete.pack(pady=5)
btn_solved = tk.Button(window, text="Mark as Solved", width=20, command=mark_solved)
btn_solved.pack(pady=5)
load_data()
window.mainloop()