import pandas as pd
import plotly.express as px

def LCG():
    LCG.seed = (LCG.seed * LCG.mult + LCG.const) % LCG.cap
    return LCG.seed


if __name__ == "__main__":

    LCG.cap = 16
    LCG.seed = 7
    LCG.mult = 5
    LCG.const = 3

    logs = []
    for i in range(100):
        logs.append(LCG())
    print(logs)
    frame = pd.DataFrame(logs)
    fig = px.histogram(frame)
    fig.show()