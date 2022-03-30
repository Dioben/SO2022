import plotly.express as px 
import pandas as pd

def initialize():
    return {"x":1.0,"y":1.0}

def observe(vars,histories):
   histories["x"].append(vars["x"])
   histories["y"].append(vars["y"])
   return histories

def update(histories):
    return {"x": .5*histories["x"][-1]+histories["y"][-1],"y": -.5 * histories["x"][-1]+histories["y"][-1]}

if __name__ == "__main__":

    vars = initialize()
    logs = {"x":[],"y":[]}
    for t in range(101):
        observe(vars,logs)
        vars = update(logs)
    frame = pd.DataFrame(logs)
    fig = px.line(frame)
    fig.show()
    