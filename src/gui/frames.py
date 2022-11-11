from gui.base_frames import BaseFrame
from gui.button import BaseButton


def print_hello():
    print("-" * 100)
    print("hello")
    print("-" * 100)


class TestFrame(BaseFrame):
    def __init__(self, master, height, width):
        super().__init__(master, height, width)

        self.add_button("Hello", print_hello, (1, 0))
        self.add_button("Hi", print_hello, (2, 0))
        self.add_button("Bye", print_hello, (3, 0))
        self.add_button("Good", print_hello, (4, 0))
