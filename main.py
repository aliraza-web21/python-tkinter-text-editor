
import tkinter as tk
from tkinter import filedialog, messagebox


# New File Function
def new_file():
    text.delete("1.0", tk.END)


# Open File Function
def open_file():
    file_path = filedialog.askopenfilename(
        title="Open Text File",
        defaultextension=".txt",
        filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            text.delete("1.0", tk.END)
            text.insert(tk.END, content)

        except Exception as e:
            messagebox.showerror("Error", f"Unable to open file:\n{e}")


# Save File Function
def save_file():
    file_path = filedialog.asksaveasfilename(
        title="Save Text File",
        defaultextension=".txt",
        filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text.get("1.0", "end-1c"))

            messagebox.showinfo(
                "Success",
                "File saved successfully!"
            )

        except Exception as e:
            messagebox.showerror("Error", f"Unable to save file:\n{e}")


# Exit Function
def exit_app():
    root.destroy()


# Main Window
root = tk.Tk()

root.title("Simple Text Editor")
root.geometry("1366x768")
root.minsize(500, 300)


# Menu Bar
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)

menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)

file_menu.add_separator()

file_menu.add_command(label="Exit", command=exit_app)


# Text Area
text = tk.Text(
    root,
    wrap=tk.WORD,
    font=("Arial", 12),
    fg="blue",
    undo=True
)

text.pack(
    expand=True,
    fill=tk.BOTH,
    padx=10,
    pady=10
)


# Run Application
root.mainloop()
