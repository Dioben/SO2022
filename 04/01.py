import pandas as pd
import plotly.express as px

def midsquare(seed):
    seed = seed * seed
    seed = seed // 100 #cut lowest 2 digits
    seed = seed % 10000 #cut to 4 digits
    
    return seed



if __name__ == "__main__":

    var = 1234
    logs = []
    while var>100:
        logs.append(var)
        var = midsquare(var)
    logs.append(var)
    print(logs)
    frame = pd.DataFrame(logs)
    fig = px.line(frame)
    fig.show()