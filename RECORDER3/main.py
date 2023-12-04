from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from audiostream import get_input
import soundfile as sf
import os

class AudioRecorderApp(App):
    def build(self):
        self.audio_file_path = None
        self.mic = None

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.record_button = Button(text='Start Recording')
        self.record_button.bind(on_press=self.toggle_recording)
        layout.add_widget(self.record_button)

        return layout

    def toggle_recording(self, instance):
        if self.audio_file_path is None:
            # Start recording
            self.audio_file_path = self.start_recording()
            self.record_button.text = 'Stop Recording'
        else:
            # Stop recording
            self.stop_recording()
            self.record_button.text = 'Start Recording'
            self.audio_file_path = None

    def start_recording(self):
        # Create a temporary file to store the recorded audio
        temp_dir = self.user_data_dir
        audio_file_path = os.path.join(temp_dir, 'recorded_audio.wav')

        # Get the microphone input
        self.mic = get_input(callback=self.record_callback)
        self.mic.start()

        return audio_file_path

    def stop_recording(self):
        if self.mic:
            # Stop recording
            self.mic.stop()
            self.mic = None

            print(f"Recording saved: {self.audio_file_path}")

    def record_callback(self, data):
        # Process and save the recorded audio data
        sf.write(self.audio_file_path, data, self.mic.samplerate, format='wav')

if __name__ == '__main__':
    AudioRecorderApp().run()
