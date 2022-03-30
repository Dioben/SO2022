import plotly.express as px 
import pandas as pd

def initialize():
    return 1.0

def observe(var,history):
    history.append(var)

def update(x,factor):
    return x * factor

if __name__ == "__main__":

    factor = 0.99
    x = initialize()
    xlogs = []
    for t in range(101):
        observe(x,xlogs)
        x = update(x,factor)

    frame = pd.DataFrame(xlogs)
    fig = px.line(frame,y=0, title=f"Growth with factor {factor}")
    fig.show()