from kivy.uix.screenmanager import Screen
import time

class MainScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time_text = 0.01
        self.characters_per_row = 56

    
    def add_text(self, text):
        print(text)
        self.ids.label.text += text
        self.ids.scroll_view.scroll_y = 1

    def text_init(self):
        with open('src/assets/texts/lorem_ipsum.txt', 'r') as file:
            for row in file:
                len_row = len(row)
                charac_count = 0
                while charac_count < len_row:
                    init = charac_count
                    end = self.characters_per_row+charac_count
                    self.add_text(row[init:end]+"\n")
                    charac_count += self.characters_per_row
                time.sleep(self.time_text)


