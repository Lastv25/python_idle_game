import Tkinter as tk
import ttk
from gui.labels import BaseLabel

class BaseFrame(tk.Frame):
    """
    Displays a series of buttons that change the colour of the Tkinter 
    frame when pressed.
    """
    def __init__(self, master,height,width):
        tk.Frame.__init__(self, master)
        self.master = master

        self.mainf = tk.Frame(master, height=height, width=width, pady=50, padx=50)
        self.mainf.grid(row=0, column=0)

        self.s = ttk.Style()
        self.s.theme_use('aqua')
        self.mainf.configure(background='{}'.format('black'))

    def add_label_text(self, text):
        BaseLabel(self.mainf,text)