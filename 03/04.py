import plotly.express as px 
import pandas as pd

def differential(x):
    return differential.r*x*(1- x/ differential.K)

def initialize():
    return 0.1

def eulerForward(currentval, current , nexttime):
    return currentval + (nexttime-current)*differential(current)

def rungeKutta(currentval,current,  nexttime):
    timediff = (nexttime-current)
    f1 = timediff * differential(current)
    f2 = timediff * differential(current+f1/2)
    f3 = timediff * differential(current+f2/2)
    f4  = timediff * differential(current+f3)
    return currentval + f1/6 + f2/3 + f3/3 +f4/6


if __name__ == "__main__":
    differential.r = 0.2
    differential.K = 1
    x = initialize()
    x_kutta = x
    t = 0
    logs = []
    logs_kutta = []
    delta_t = 0.01
    for t in range(100):
        logs.append(x)
        logs_kutta.append(x_kutta)
        x = eulerForward(x,t,t+delta_t)
        x_kutta = rungeKutta(x,t,t+delta_t)
        t+=delta_t

    frame = pd.DataFrame(logs)
    fig = px.line(frame)
    fig.show()
    frame = pd.DataFrame(logs_kutta)
    fig = px.line(frame)
    fig.show()
    