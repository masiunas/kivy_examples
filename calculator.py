from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "300")
Config.set("graphics", "height", "300")

saveInput = ''


class CalculatorApp(App):
    def calculate(self, instance):
        global saveInput
        if instance.text == 'C':
            self.result.text = saveInput = ''
        elif instance.text is not '=':
            self.result.text += instance.text
            saveInput = self.result.text
        else:
            try:
                saveInput = self.result.text = str(eval(saveInput))
            except:
                saveInput = self.result.text = ''

    def build(self):
        form = BoxLayout(orientation='vertical', padding=5)
        self.result = TextInput(readonly=True, font_size=25, size_hint=[1, .75],
                                background_color=[1, 1, 1, .8])
        form.add_widget(self.result)
        button_box = GridLayout(cols=5)
        button_box.add_widget(Button(text='7', on_press=self.calculate))
        button_box.add_widget(Button(text='8', on_press=self.calculate))
        button_box.add_widget(Button(text='9', on_press=self.calculate))
        button_box.add_widget(Button(text='+', on_press=self.calculate))
        button_box.add_widget(Button(text='C', on_press=self.calculate))

        button_box.add_widget(Button(text='4', on_press=self.calculate))
        button_box.add_widget(Button(text='5', on_press=self.calculate))
        button_box.add_widget(Button(text='6', on_press=self.calculate))
        button_box.add_widget(Button(text='-', on_press=self.calculate))
        button_box.add_widget(Button(text='(', on_press=self.calculate))

        button_box.add_widget(Button(text='1', on_press=self.calculate))
        button_box.add_widget(Button(text='2', on_press=self.calculate))
        button_box.add_widget(Button(text='3', on_press=self.calculate))
        button_box.add_widget(Button(text='*', on_press=self.calculate))
        button_box.add_widget(Button(text=')', on_press=self.calculate))

        button_box.add_widget(Button(text='0', on_press=self.calculate))
        button_box.add_widget(Button(text='.', on_press=self.calculate))
        button_box.add_widget(Button(text='=', on_press=self.calculate))
        button_box.add_widget(Button(text='/', on_press=self.calculate))
        button_box.add_widget(Button(text='%', on_press=self.calculate))
        form.add_widget(button_box)
        return form


if __name__ == '__main__':
    CalculatorApp().run()
