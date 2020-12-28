import dash
import dash_core_components as dcc
import dash_html_components as html
from flask import Flask

class RealtimeDashPlotter:
    """
    Real time Dash Plotter Server

    A Dashboard Plotter Server to plot realtime data
    """
    def __init__(self, name:str, host_address:str = "0.0.0.0", port:int = 8050, debug:bool = False):
        self.host_address = host_address
        self.port = port
        self.debug = debug
        self.server = Flask(name)
        self.app = dash.Dash(name, server=self.server)

        self.app_children = [html.H1(children=name)]

        self.figureNumbers = 0

    def appendGraph(self, figure, id = None):
        if id is None:
            id = str(self.figureNumbers)
        self.app_children.append(dcc.Graph(
            id = id,
            figure=figure.getFigure()
        ))
        self.figureNumbers +=1
    
    def run(self):
        self.app.layout = html.Div(children=self.app_children)
        self.app.run_server(debug=self.debug, port=self.port, host=self.host_address)
