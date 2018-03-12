<<<<<<< HEAD
from plotly import offline
from plotly.graph_objs import Scatter, Layout, Pie, Bar
from abc import ABCMeta, abstractmethod


# Same
class GraphType(metaclass=ABCMeta):
    # Wesley
    def __init__(self, data, filename):
        self.filename = filename
        self.data = data

    # Sam
    @abstractmethod
    def draw_graph(self, x_key, y_key, title):
        pass


# Sam
class ScatterGraph(GraphType):
    def draw_graph(self, x_key, y_key, graph_title):
        offline.plot({
            "data": [Scatter(x=self.data[x_key], y=self.data[y_key])],
            "layout": Layout(title=graph_title)
        }, filename=self.filename)


# Sam
class PieGraph(GraphType):
    def draw_graph(self, x_key, y_key, graph_title):
        offline.plot({
            "data": [Pie(labels=self.data[x_key], values=self.data[y_key])],
            "layout": Layout(title=graph_title)
        }, filename=self.filename)


# Sam
class BarGraph(GraphType):
    def draw_graph(self, x_key, y_key, graph_title):
        offline.plot({
            "data": [Bar(x=self.data[x_key], y=self.data[y_key])],
            "layout": Layout(title=graph_title)
        }, filename=self.filename)


# Wesley
class Graph:
    # Wesley
    def __init__(self):
        self.file_type = None

    # Wesley
    def set_data(self, dictionary, a_type, filename):
        """
        Set the data to be used
        :param dictionary: Will contain the data that will be used

        :param a_type: set the type of graph to generate
        :param filename: sets the save location and file name
        :return: void
        """
        types = {
            'pie': PieGraph(dictionary, filename),
            'scatter': ScatterGraph(dictionary, filename),
            'bar': BarGraph(dictionary, filename)
        }
        self.file_type = types[a_type]

    def draw(self, x_key, y_key, title):
        self.file_type.draw_graph(x_key, y_key, title)

# Testing - Works
# # sample data being used
# sample1 = {"x axis": [1, 2, 3, 4, 5, 6, 7, 8, 9], "y axis": [9, 8, 7, 6, 5, 4, 3, 2, 1]}
#
#
# # Created a class to handle the graph as a whole
# a = Graph()
# # Insert data, type of graph and save location with the file name
# # can change the graph type to whatever and will output
# a.set_data(sample1, "scatter", "C:\\temp\\random.html")
# # x and y axis are the key values in the dictionary being passed
# a.draw("x axis", "y axis", "the title")
=======
from plotly import offline
from plotly.graph_objs import Scatter, Layout, Pie, Bar
from abc import ABCMeta, abstractmethod


# Same
class GraphType(metaclass=ABCMeta):
    # Wesley
    def __init__(self, data, filename):
        self.filename = filename
        self.data = data

    # Sam
    @abstractmethod
    def draw_graph(self, x_key, y_key, title):
        pass


# Sam
class ScatterGraph(GraphType):
    def draw_graph(self, x_key, y_key, graph_title):
        offline.plot({
            "data": [Scatter(x=self.data[x_key], y=self.data[y_key])],
            "layout": Layout(title=graph_title)
        }, filename=self.filename)


# Sam
class PieGraph(GraphType):
    def draw_graph(self, x_key, y_key, graph_title):
        offline.plot({
            "data": [Pie(labels=self.data[x_key], values=self.data[y_key])],
            "layout": Layout(title=graph_title)
        }, filename=self.filename)


# Sam
class BarGraph(GraphType):
    def draw_graph(self, x_key, y_key, graph_title):
        offline.plot({
            "data": [Bar(x=self.data[x_key], y=self.data[y_key])],
            "layout": Layout(title=graph_title)
        }, filename=self.filename)


# Wesley
class Graph:
    # Wesley
    def __init__(self):
        self.file_type = None

    # Wesley
    def set_data(self, dictionary, a_type, filename):
        """
        Set the data to be used
        :param dictionary: Will contain the data that will be used

        :param a_type: set the type of graph to generate
        :param filename: sets the save location and file name
        :return: void
        """
        types = {
            'pie': PieGraph(dictionary, filename),
            'scatter': ScatterGraph(dictionary, filename),
            'bar': BarGraph(dictionary, filename)
        }
        self.file_type = types[a_type]

    def draw(self, x_key, y_key, title):
        self.file_type.draw_graph(x_key, y_key, title)

# Testing - Works
# # sample data being used
# sample1 = {"x axis": [1, 2, 3, 4, 5, 6, 7, 8, 9], "y axis": [9, 8, 7, 6, 5, 4, 3, 2, 1]}
#
#
# # Created a class to handle the graph as a whole
# a = Graph()
# # Insert data, type of graph and save location with the file name
# # can change the graph type to whatever and will output
# a.set_data(sample1, "scatter", "C:\\temp\\random.html")
# # x and y axis are the key values in the dictionary being passed
# a.draw("x axis", "y axis", "the title")
>>>>>>> 6540e0402541687358a943f73273ca0ddaad4381
