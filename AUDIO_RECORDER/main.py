from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.switch import Switch  # Corrected typo here
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.clock import Clock  # Corrected the Clock import


Builder.load_string('''
<AudioTool>
    orientation: 'vertical'
    Label:
        id:display_label
        text: '00:00'
    BoxLayout:
        size_hint: 1, .2
        TextInput:
            id: user_input
            text: '5'
        Switch:
            id: duration_switch
    BoxLayout:
        Button:
            id:start_button
            text: 'Start Recording'
        Button:
            id: stop_button
            text: 'Stop Recording'
''')


class AudioApp(App):
    def build(self):
        return AudioTool()

class AudioTool(BoxLayout):
    def __init__(self, **kwargs):  # Corrected the typo in the method name
        super(AudioTool, self).__init__(**kwargs)

        pass


if __name__ == '__main__':
    AudioApp().run()  # Corrected the instantiation of AudioApp
