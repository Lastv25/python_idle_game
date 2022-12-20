from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

Builder.load_file('./components/menu.kv')


class Menu(FloatLayout):
    pass


class MyApp(App):
    def build(self):
        return Menu()


if __name__ == '__main__':
    MyApp().run()

