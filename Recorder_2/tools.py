from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.graph import Graph, LinePlot
from kivy.clock import Clock
from audiostream import get_input

class AudioStreamApp(App):
    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical')

        # Create a graph for plotting the microphone input
        self.graph = Graph(x_ticks_major=1000, y_ticks_major=0.5,
                           x_grid_label=True, y_grid_label=True,
                           padding=5, x_grid=True, y_grid=True,
                           xmin=0, xmax=1000, ymin=-1, ymax=1)

        # Create a LinePlot with a blue color
        self.plot = LinePlot(color=[0, 0, 1, 1], line_width=2)

        # Add the plot to the graph
        self.graph.add_plot(self.plot)

        # Add the graph to the layout
        layout.add_widget(self.graph)

        # Schedule the update function to be called every 0.1 seconds
        Clock.schedule_interval(self.update_plot, 0.1)

        # Open the microphone stream
        self.stream = get_input(channels=1, rate=44100, buffersize=2048)

        return layout

    def update_plot(self, dt):
        # Read audio data from the microphone
        data = self.stream.read(2048)

        # Update the plot with the new data
        self.plot.points = [(i, val) for i, val in enumerate(data)]

if __name__ == '__main__':
    AudioStreamApp().run()
