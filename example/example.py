import sys
sys.path.append("../")
from realtime_dash_plotter.realtime_dash_plotter.realtime_dash_plotter import RealtimeDashPlotter
from realtime_dash_plotter.realtime_dash_plotter.plot_figure import XYFigure


plotter = RealtimeDashPlotter("Example Plotter", debug=True)
graph = XYFigure("Example Graph")
plotter.appendGraph(graph)


plotter.run()
