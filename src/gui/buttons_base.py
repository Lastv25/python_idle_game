
from kivy.uix.button import Button


class BaseButton(Button):

    def callback(self, instance):
        print('The button <%s> is being pressed' % instance.text)

    def __init__(self,text):
        self.button = Button(text=text)
        self.button.bind(on_press=self.callback)
    
    def get_button(self):
        return self.button