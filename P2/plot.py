import pandas as pd
import plotly.express as px

### GRASP tests
if False:
    df = pd.read_csv("GRASP.csv", names=["n","time","r","LS1","LS2"])

    df = df.groupby(["n","r"]).mean().reset_index()

    fig = px.line(df, x="r", y="LS1", color="n", title="Average results per r")
    fig.show()

### Memetic tests
if False:
    df = pd.read_csv("Memetic.csv", names=["n","time","population size","elitism","mutation chance","LS1","LS2"])

    col = "mutation chance"

    df = df.groupby(["n",col]).mean().reset_index()
    fig = px.line(df, x=col, y="LS1", color="n", title=col)
    fig.show()

### GRASP final
if False:
    df = pd.read_csv("GRASP5min.csv", names=["n","result"])
    df2 = df.groupby(["n"]).agg({"result":["mean","min","max"]})
    print(df2)

    df["run"] = df.groupby(["n"]).cumcount()+1
    fig = px.line(df, x="run", y="result", color="n", title="5 min GRASP")
    fig.show()

### Memetic final
if False:
    df = pd.read_csv("MemeticBest.csv", names=["n","result","time"])
    df2 = df.groupby(["n"]).agg({"time":["mean","min","max"]})
    print(df2)

    df["run"] = df.groupby(["n"]).cumcount()+1
    fig = px.line(df, x="run", y="time", color="n", title="Best memetic")
    fig.show()