from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.graph import Graph, MeshLinePlot
from kivy.lang import Builder
from math import sin

Builder.load_string("""
<MyGraph>:
    graph: graph
    orientation: 'vertical'
    Graph:
        id: graph
        xlabel: 'X'
        ylabel: 'Y'
        x_ticks_minor: 5
        x_ticks_major: 25
        y_ticks_major: 1
        y_grid_label: True
        x_grid_label: True
        padding: 5
        x_grid: True
        y_grid: True
        xmin: 0
        xmax: 100
        ymin: -1
        ymax: 1
""")

class MyGraph(BoxLayout):
    def __init__(self, **kwargs):
        super(MyGraph, self).__init__(**kwargs)
        plot = MeshLinePlot(color=[1, 0, 0, 1])
        plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
        self.graph.add_plot(plot)

class MicrophoneApp(App):
    def build(self):
        return MyGraph()

if __name__ == '__main__':
    MicrophoneApp().run()
