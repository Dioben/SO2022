import pandas as pd
import plotly.express as px

def LCG():
    LCG.seed = (LCG.seed * LCG.mult + LCG.const) % LCG.cap
    return LCG.seed


if __name__ == "__main__":

    LCG.cap = 1
    LCG.seed = .5
    LCG.mult = 1
    LCG.const = 0.00999

    logs = []
    for i in range(100):
        logs.append(LCG())
    print(logs)
    frame = pd.DataFrame(logs)
    fig = px.line(frame)
    fig.show()