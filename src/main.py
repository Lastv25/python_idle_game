import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import random
# import main


class Game(BoxLayout):
    colors = [(1, 0, 0, 1), (0, 1, 0, 1), (1, 0, 1, 1), (0, 0, 1, 1)]
    Buttonz = ('Button1', 'Button2', 'Button3', 'Button4')

    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        self.padding = 5
        self.orientation = "vertical"
        self.Buttons()

    def Buttons(self):
        for i in range(len(self.Buttonz)):
            btn = Button(text=self.Buttonz[i], background_color=random.choice(self.colors))
            self.add_widget(btn)
            # btn.bind(on_press=main.Political)


class Main(App):
    title = 'ButtonGame'

    def build(self):
        return Game()


if __name__ == '__main__':
    Main().run()