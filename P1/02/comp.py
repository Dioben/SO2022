import argparse  # process command line
import plotly.express as px  # plotting libs
import pandas as pd
from euler import eulerForward,differential
from kutta import rungeKutta




if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--initial", help="Initial height", type=float, required=True)
    parser.add_argument(
        "--initial-derivative", help="Initial derivative", type=float, required=True
    )
    parser.add_argument(
        "--mass", help="initial object mass, defaults to 1", type=float, default=1
    )
    parser.add_argument(
        "--gravity", help="Gravity constant, defaults to 9.81", type=float, default=9.81
    )
    parser.add_argument(
        "--tick-interval", help="How often data is computed", type=float, default=1
    )
    parser.add_argument(
        "--stop-point",
        help="When to stop computing in seconds, defaults to 20 seconds",
        type=float,
        default=20,
    )
    parser.add_argument(
        "--wind-resistance",
        help="Wind resistance constant, defaults to 0",
        type=float,
        default=0,
    )

    args = parser.parse_args()

    # assign args to the differential model
    differential.m = args.mass
    differential.g = args.gravity
    differential.u = args.wind_resistance

    snapshotTimers = [x*args.tick_interval for x in range(int(args.stop_point/args.tick_interval))]

    derivationResults = [None for _ in range(len(snapshotTimers))]
    positionResults = [None for _ in range(len(snapshotTimers))]
    derivationResultsKutta = [None for _ in range(len(snapshotTimers))]
    positionResultsKutta = [None for _ in range(len(snapshotTimers))]

    #start euler
    positionResults[0] = args.initial
    derivationResults[0] = args.initial_derivative

    positionResults[1] = args.initial + args.tick_interval * args.initial_derivative
    derivationResults[1] = differential(positionResults[0], positionResults[1], args.tick_interval)

    #start rk4
    positionResultsKutta[0] = args.initial
    derivationResultsKutta[0] = args.initial_derivative

    positionResultsKutta[1] = args.initial + args.tick_interval * args.initial_derivative #TODO: ASK LAU WHETHER EULER START IS APPROPRIATE
    derivationResultsKutta[1] = differential(positionResults[0], positionResults[1], args.tick_interval)


    for idx in range(2, len(snapshotTimers)):
        #euler
        derivationResults[idx] = differential(positionResults[idx - 2], positionResults[idx-1], args.tick_interval)
        positionResults[idx] = eulerForward(positionResults[idx - 2], positionResults[idx-1], args.tick_interval)
        #rk4
        derivationResultsKutta[idx] = differential(positionResultsKutta[idx - 2], positionResultsKutta[idx-1], args.tick_interval)
        positionResultsKutta[idx] = rungeKutta(positionResultsKutta[idx - 2], positionResultsKutta[idx-1], args.tick_interval)


    mappedData = [{"time": snapshotTimers[x], "method":"Euler","type": "Euler Position", "value": positionResults[x]}for x in range(len(snapshotTimers))]
    mappedData += [{"time": snapshotTimers[x],"method":"Euler", "type": "Euler Derivative", "value": derivationResults[x]}for x in range(len(snapshotTimers))]
    mappedData += [{"time": snapshotTimers[x], "method":"RK4","type": "RK4 Position", "value": positionResultsKutta[x]}for x in range(len(snapshotTimers))]
    mappedData += [{"time": snapshotTimers[x],"method":"RK4", "type": "RK4 Derivative", "value": derivationResultsKutta[x]}for x in range(len(snapshotTimers))]

    frame = pd.DataFrame(mappedData)
    fig = px.line(frame, x="time", y="value", color="type")
    fig.show()
