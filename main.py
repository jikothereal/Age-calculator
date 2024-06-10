import tkinter as tk
from tkinter import messagebox
import threading

def center_window(window, width, height):
     window.update_idletasks()
     x = (window.winfo_screenwidth() // 2) - (width // 2)
     y = (window.winfo_screenheight() // 2) - (height // 2)
     window.geometry(f'{width}x{height}+{x}+{y}')

def show_result(root, number):
        calculating_window.destroy()
        messagebox.showinfo("Calculation Result", f"You are {number} years old")
        root.deiconify()

def show_calculating_and_result(root, number):
    global calculating_window

    calculating_window = tk.Toplevel(root)
    calculating_window.title("Please Wait")
    calculating_window.geometry("250x100")
    calculating_window.resizable(False, False)

    center_window(calculating_window, 300, 150)

    tk.Label(calculating_window, text="Calculating...", font=("Helvetica", 16)).pack(expand=True)

    threading.Timer(5, lambda: show_result(root, number)).start()

def on_button_click():
    inputtext = entry.get()
    root.withdraw()

    if not inputtext.strip():
        messagebox.showwarning("Input Error", "You need to enter a number.")
        root.deiconify()
        return
    
    try:
        number = int(inputtext)
    except ValueError:
        messagebox.showwarning("Input Error", "you need to enter a number, no letters.")
        root.deiconify()
        return

    if number > 60:
        messagebox.showerror("Input Error", "Nuh uh, you are NOT that old buddy")
        root.deiconify()
        return
    
    if number < 11:
        messagebox.showerror("Input Error", "Come in my basement if you're actually that young")
        root.deiconify()
        return
    
    show_calculating_and_result(root, number)


root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x150")
root.resizable(False, False)

center_window(root, 300, 150)

tk.Label(root, text="Enter your age:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Submit", command=on_button_click).pack(pady=10)


root.mainloop()