import plotly.graph_objects as go

class XYFigure:
    """
    docstring
    """
    def __init__(self, title):
        self.figure = go.Figure()
        self.figure.update_layout(title=title)
    
    def getFigure(self):
        return self.figure
