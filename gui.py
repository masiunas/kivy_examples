from kivy.app import App
from kivy.uix.button import Button


class MyFirstKivyApp(App):
    def build(self):
        return Button(text='Hello World!',
                      on_press=self.click)

    def click(self, instance):
        print(self)


if __name__ == '__main__':
    MyFirstKivyApp().run()
