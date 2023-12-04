from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.garden.audiorecorder import AudioRecorder
import os

class AudioRecorderApp(App):
    def build(self):
        self.audio_file_path = None

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.record_button = Button(text='Start Recording')
        self.record_button.bind(on_press=self.toggle_recording)
        layout.add_widget(self.record_button)

        self.audio_recorder = AudioRecorder()
        layout.add_widget(self.audio_recorder)

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

    def start_recording(self):
        # Create a temporary file to store the recorded audio
        temp_dir = self.user_data_dir
        audio_file_path = os.path.join(temp_dir, 'recorded_audio.wav')

        # Set the output file for the audio recorder
        self.audio_recorder.set_output_file(audio_file_path)

        # Start recording
        self.audio_recorder.start()

        return audio_file_path

    def stop_recording(self):
        # Stop recording
        self.audio_recorder.stop()

        print(f"Recording saved: {self.audio_file_path}")

if __name__ == '__main__':
    AudioRecorderApp().run()
