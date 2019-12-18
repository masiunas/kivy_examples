from kivy.app import App
from kivy.uix.button import Button

from random import random


class ClickerApp(App):
    def build(self):
        self.btn = Button(text='0',
                          font_size=30,
                          background_color=[1, 1, 1, 1],
                          on_press=self.click
                          )
        return self.btn

    def click(self, instance):
        self.btn.text = str(int(self.btn.text) + 1)
        self.btn.background_color = [random(), random(), random(), random()]


if __name__ == '__main__':
    ClickerApp().run()
