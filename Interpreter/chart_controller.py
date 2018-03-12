import plotly
from plotly.graph_objs import *
from abc import ABCMeta, abstractmethod


class GraphType(metaclass=ABCMeta):

    @abstractmethod
    def draw_graph(self, dictionary, key, key2, graph_title):
        pass


class GraphScatter(GraphType):
    def draw_graph(self, dictionary, key, key2, graph_title):
        plotly.offline.plot({
            "data": [Scatter(x=dictionary[key], y=dictionary[key2])],
            "layout": Layout(title=graph_title)
        })


class GraphPie(GraphType):
    def draw_graph(self, dictionary, key, key2, graph_title):
        plotly.offline.plot({
            "data": [Pie(labels=dictionary[key], values=dictionary[key2])],
            "layout": Layout(title=graph_title)
        })


class GraphBar(GraphType):
    def draw_graph(self, dictionary, key, key2, graph_title):
        plotly.offline.plot({
            "data": [Bar(x=dictionary[key], y=dictionary[key2])],
            "layout": Layout(title=graph_title)
        })


sample1 = {"data1": [1, 2, 3, 4, 5, 6, 7, 8, 9], "data2": [9, 8, 7, 6, 5, 4, 3, 2, 1]}
sample3 = {"data1": [1, 2, 3, 4, 5, 6, 7, 8, 9], "data2": [9, 8, 7, 6, 5, 4, 3, 2, 1]}
sample2 = {"data1": ["sam", "james", "wesley", "luo feng", "amit sarkar", "mike catman"], "data2": [9, 8, 7, 6, 5, 4, 3, 2, 1]}
my_title = "this is my title"


a = GraphScatter()
b = GraphPie()
c = GraphBar()

a.draw_graph(sample1, "data1", "data2", my_title)
b.draw_graph(sample2, "data1", "data2", my_title)
c.draw_graph(sample3, "data1", "data2", my_title)

# only outputting 2 x bar graph rather than 1x bar,pie,scatter

print("PRINING")
