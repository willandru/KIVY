from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.graph import Graph, MeshLinePlot
from kivy.clock import Clock
from audiostream.core import AudioSample
import numpy as np

class MicrophoneApp(App):
    def build(self):
        print("Build method executed")
        layout = BoxLayout(orientation='vertical')

        self.graph = Graph(xlabel='Time', ylabel='Amplitude', x_ticks_minor=5, x_ticks_major=1,
                           y_ticks_major=0.5, y_grid_label=True, x_grid_label=True, padding=5,
                           x_grid=True, y_grid=True, xmin=0, xmax=10, ymin=-1, ymax=1)

        self.plot = MeshLinePlot(color=[1, 0, 0, 1])
        self.graph.add_plot(self.plot)
        layout.add_widget(self.graph)

        Clock.schedule_interval(self.update_plot, 0.1)
        self.sample = AudioSample(callback=self.update_audio)

        return layout

    def update_audio(self, in_data, frame_count, time_info, status):
        try:
            data = np.frombuffer(in_data, dtype=np.float32)
            self.plot.points = [(i, val) for i, val in enumerate(data)]
            return in_data, 0
        except Exception as e:
            print("Error in update_audio:", e)
            return in_data, 0


        return in_data, 0

    def update_plot(self, dt):
        print("Update plot method executed")

        self.graph.xmax += dt
        self.graph.xmin = max(0, self.graph.xmax - 10)

if __name__ == '__main__':
    MicrophoneApp().run()
