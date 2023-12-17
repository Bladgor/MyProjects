import time
import tkinter as tk
import tkinter.colorchooser as cc
from tkinter import ttk
from time import sleep

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 250
window_height = 200
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.title("Выбор цвета")
frame = tk.Frame(root)
frame.grid()


def exit_():
    root.destroy()


def choose_color():
    color = cc.askcolor()[1]
    color_label.config(text=f"Вы выбрали цвет {color}")
    second_label.config(bg=color)
    print(color)


color_button = tk.Button(frame, text="Выбрать цвет", command=choose_color)
exit_button = tk.Button(frame, text='Выход')
color_label = tk.Label(frame, text="Нажмите кнопку, чтобы выбрать цвет")
second_label = tk.Label(root, text="\t\t\t\n\t\t\t")
color_button.grid(row=0, column=0)
color_label.grid(row=1, column=0)
second_label.grid(row=2, column=0)
exit_button.grid(row=3, column=0)


root.mainloop()
