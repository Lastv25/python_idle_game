import tkinter as tk

from gui.frames import TestFrame

root = tk.Tk()
root.title("Mage City")
root.update()

app = TestFrame(root, 300, 300)

root.mainloop()
