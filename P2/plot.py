import pandas as pd
import plotly.express as px

### GRASP
if False:
    df = pd.read_csv("GRASP.csv", names=["n","time","r","LS1","LS2"])

    df = df.groupby(["n","r"]).mean().reset_index()

    fig = px.line(df, x="r", y="LS1", color="n", title="Average results per r")
    fig.show()

### Memetic
if False:
    df = pd.read_csv("Memetic.csv", names=["n","time","population size","elitism","mutation chance","LS1","LS2"])

    col = "mutation chance"

    df = df.groupby(["n",col]).mean().reset_index()
    fig = px.line(df, x=col, y="LS1", color="n", title=col)
    fig.show()