from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.clock import Clock


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
            on_release: root.startRecordingClock()
                    
        Button:
            id: stop_button
            text: 'Stop Recording'
            on_release: root.stopRecording()
            disabled: True
''')


class AudioApp(App):
    def build(self):
        return AudioTool()

class AudioTool(BoxLayout):
    def __init__(self, **kwargs):
        super(AudioTool, self).__init__(**kwargs)

        self.start_button = self.ids['start_button']
        self.stop_button = self.ids['stop_button']
        self.display_label = self.ids['display_label']
        self.switch = self.ids['duration_switch']  # Corrected the method for accessing ids
        self.user_input = self.ids['user_input']  # Corrected the method for accessing ids


    def startRecordingClock(self):
        self.zero = 55
        self.mins = 0
        self.duration = int(self.user_input.text)
        Clock.schedule_interval(self.updateDisplay, 1)
        self.start_button.disabled = True
        self.stop_button.disabled = False
        self.switch.disabled = True

    def stopRecording(self):
        Clock.unschedule(self.updateDisplay)
        self.display_label.text = 'Finished Recording'
        self.start_button.disabled = False
        self.stop_button.disabled = True
        self.switch.disabled = False

    def updateDisplay(self, dt):
        if self.switch.active == False:
            if self.zero < 60 and len(str(self.zero)) == 1:
                self.display_label.text = '0' + str(self.mins) + ':0' + str(self.zero)
                self.zero += 1
            elif self.zero < 60 and len(str(self.zero)) == 2:
                self.display_label.text = '0' + str(self.mins) + ':' + str(self.zero)
                self.zero += 1
            elif self.zero == 60:
                self.mins += 1
                self.display_label.text = '0' + str(self.mins) + ':00'
                self.zero = 1

if __name__ == '__main__':
    AudioApp().run()
