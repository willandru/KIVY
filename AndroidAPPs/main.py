from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text='Hello, Kivy!', on_press=self.on_button_press)

    def on_button_press(self, instance):
        print('Button pressed!')

if __name__ == '__main__':
    MyApp().run()
