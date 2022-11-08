import Tkinter as tk
import ttk

class BaseLabel(tk.Label):
    def __init__(self,parent, text):
        ttk.Label(parent, text=text)