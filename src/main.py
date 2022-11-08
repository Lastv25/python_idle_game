import Tkinter as tk
from gui.frames import BaseFrame



root = tk.Tk()
root.title('Mage City')
root.update()

app = BaseFrame(root,300,300)

root.mainloop()