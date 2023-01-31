from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

# Builder.load_file('./components/screen_manager.kv')


class MyApp(App):
    def build(self):
        return Builder.load_file('components/screen_manager.kv')


if __name__ == '__main__':
    MyApp().run()

