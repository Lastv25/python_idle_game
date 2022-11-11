import tkinter as tk
from tkinter import ttk


class BaseButton(ttk.Button):
    def __init__(self, parent, text, command, position):
        button = ttk.Button(parent, text=text, command=command, bg="black", fg="White")
        button.grid(row=position[0], column=position[1])
