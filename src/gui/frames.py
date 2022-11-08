from gui.base_frames import BaseFrame

class TestFrame(BaseFrame):

    def __init__(self,master,height,width):
        super().__init__(master,height,width)

        self.add_label_text('hello world')