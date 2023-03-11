import tkinter as tk

class ToDoListManager:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List Manager")

        # Create the GUI elements
        self.task_label = tk.Label(master, text="Task:")
        self.task_entry = tk.Entry(master, width=30)
        self.add_button = tk.Button(master, text="Add", command=self.add_task)
        self.task_listbox = tk.Listbox(master, width=30)
        self.edit_button = tk.Button(master, text="Edit", command=self.edit_task)
        self.delete_button = tk.Button(master, text="Delete", command=self.delete_task)
        self.save_button = tk.Button(master, text="Save", command=self.save_tasks)
        self.load_button = tk.Button(master, text="Load", command=self.load_tasks)

        # Position the GUI elements
        self.task_label.grid(row=0, column=0)
        self.task_entry.grid(row=0, column=1)
        self.add_button.grid(row=1, column=0, columnspan=2)
        self.task_listbox.grid(row=2, column=0, columnspan=2)
        self.edit_button.grid(row=3, column=0)
        self.delete_button.grid(row=3, column=1)
        self.save_button.grid(row=4, column=0)
        self.load_button.grid(row=4, column=1)

        # Load any saved tasks
        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def edit_task(self):
        selected_task = self.task_listbox.curselection()
        if len(selected_task) == 1:
            new_task = tk.simpledialog.askstring("Edit Task", "Enter new task:")
            if new_task != "":
                self.task_listbox.delete(selected_task)
                self.task_listbox.insert(selected_task, new_task)

    def delete_task(self):
        selected_task = self.task_listbox.curselection()
        if len(selected_task) == 1:
            self.task_listbox.delete(selected_task)

    def save_tasks(self):
        tasks = self.task_listbox.get(0, tk.END)
        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                tasks = f.readlines()
            for task in tasks:
                self.task_listbox.insert(tk.END, task.strip())
        except FileNotFoundError:
            pass

root = tk.Tk()
app = ToDoListManager(root)
root.mainloop()
