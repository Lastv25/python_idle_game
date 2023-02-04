from kivy.uix.screenmanager import Screen
import time

class MainScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_counter = 0
        self.row_limit = 5
        self.time_text = 1

    
    def add_text(self, text):
        self.ids.label.text += text
        self.text_counter += 1
        self.ids.scroll_view.scroll_y = 0

    def text_pop(self):
        with open('src/assets/texts/lorem_ipsum.txt', 'r') as file:
            for row in range(self.row_limit):
                print('-'*100)
                line = file.readline()
                self.add_text(line)
                print(line)
                time.sleep(self.time_text)


