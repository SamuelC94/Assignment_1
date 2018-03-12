import plotly
import plotly.graph_objs as go
from abc import ABCMeta, abstractmethod


class GraphType(metaclass=ABCMeta):
    def __init__(self):
        self.name = "Sam"

    @abstractmethod
    def draw_graph(self, dictionary, key, key2, graph_title):
        pass


class GraphScatter(GraphType):
    def draw_graph(self, dictionary, key, key2, graph_title):
        plotly.offline.plot({
            "data": [go.Scatter(x=dictionary[key], y=dictionary[key2])],
            "layout": go.Layout(title=graph_title)
        }, filename='ScatterGraph.html', image_filename="Plotly_Scatter_Graph")


class GraphPie(GraphType):
    def draw_graph(self, dictionary, key, key2, graph_title):
        plotly.offline.plot({
            "data": [go.Pie(labels=dictionary[key], values=dictionary[key2])],
            "layout": go.Layout(title=graph_title)
        }, filename='PieGraph.html', image_filename="Plotly_Pie_Graph")


class GraphBar(GraphType):
    def draw_graph(self, dictionary, key, key2, graph_title):
        plotly.offline.plot({
            "data": [go.Bar(x=dictionary[key], y=dictionary[key2])],
            "layout": go.Layout(title=graph_title)
        }, filename='BarGraph.html', image='png', image_filename="Plotly_Bar_Graph")

# create parameter for setting filename, image and image_filename if it seems necessary

sample1 = {"data1": [1, 2, 3, 4, 5, 6, 7, 8, 9], "data2": [9, 8, 7, 6, 5, 4, 3, 2, 1]}
sample3 = {"data1": [1, 2, 3, 4, 5, 6, 7, 8, 9], "data2": [9, 8, 7, 6, 5, 4, 3, 2, 1]}
sample2 = {"data1": ["sam", "james", "wesley", "luo feng", "amit sarkar", "mike catman"], "data2": [9, 8, 7, 6, 5, 4, 3, 2, 1]}
my_title = "this is my title"


class ChartController:
    def __init__(self, one, two, three):
        self.scatter = one
        self.pie = two
        self.bar = three

    # def __init__(self):
    #     self.scatter = GraphScatter()
    #     self.pie = GraphPie()
    #     self.bar = GraphBar()
#
    def draw_graph_a(self, dictionary, key, key2, graph_title):
        GraphScatter.draw_graph(self.scatter, dictionary, key, key2, graph_title)

    def draw_graph_b(self, dictionary, key, key2, graph_title):
        GraphPie.draw_graph(self.pie, dictionary, key, key2, graph_title)

    def draw_graph_c(self, dictionary, key, key2, graph_title):
        GraphBar.draw_graph(self.bar, dictionary, key, key2, graph_title)


example = ChartController(GraphScatter(), GraphPie(), GraphBar())
example.draw_graph_a(sample1, "data1", "data2", my_title)
example.draw_graph_b(sample2, "data1", "data2", my_title)
example.draw_graph_c(sample3, "data1", "data2", my_title)

#a = GraphScatter()
#b = GraphPie()
#c = GraphBar()

#a.draw_graph(sample1, "data1", "data2", my_title)

#b.draw_graph(sample2, "data1", "data2", my_title)

#c.draw_graph(sample3, "data1", "data2", my_title)

# only outputting 2 x bar graph rather than 1x bar,pie,scatter
