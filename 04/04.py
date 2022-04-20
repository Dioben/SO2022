import pandas as pd
import plotly.express as px

def LSRG():
    LSRG.buffer.append(LSRG.buffer[2]!=LSRG.buffer[4])
    LSRG.buffer = LSRG.buffer[1:]
    val = LSRG.buffer[0]
    for i in range(1,len(LSRG.buffer)):
        val+= LSRG.buffer[i]**i
    return val


if __name__ == "__main__":

    LSRG.buffer = [1,1,1,1,1,1,1,1] 

    logs = []
    for i in range(100):
        logs.append(LSRG())
    print(logs)
    frame = pd.DataFrame(logs)
    fig = px.histogram(frame)
    fig.show()