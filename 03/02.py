import plotly.express as px 
import pandas as pd

def initialize():
    return 1.0

def observe(var,history):
    history.append(var)

def update(x,factor,constant):
    return x * factor + constant

if __name__ == "__main__":

    factors = [.99, 1.0, 1.01]
    constants = [0,.1,.2]
    fullStorage = []
    for factor in factors:
        for constant in constants:
            x = initialize()
            xlogs = []
            for t in range(101):
                observe(x,xlogs)
                x = update(x,factor,constant)
            for i,value in enumerate(xlogs):
                fullStorage.append({"factor":(factor,constant),"value":value,"iteration":i})
    frame = pd.DataFrame(fullStorage)
    fig = px.line(frame, color="factor",x="iteration",y="value")
    fig.show()
    