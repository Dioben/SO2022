import argparse  # process command line
import plotly.express as px  # plotting libs
import pandas as pd


def differential(previousPos, currentPos, timeInterval):
    velocity = (currentPos - previousPos) / timeInterval
    return -differential.m * differential.g + differential.u * velocity**2




def rungeKutta(previousVal,currentVal,timeInterval): #TODO: evaluate whether this is remotely right
    f1 = timeInterval * differential(previousVal,currentVal,timeInterval)
    f2 = timeInterval * differential(previousVal,currentVal+ f1 / 2, timeInterval/2)
    f3 = timeInterval * differential(previousVal, currentVal + f2 / 2, timeInterval/2)
    f4 = timeInterval * differential(previousVal, currentVal + f3, timeInterval*2)
    return currentVal + f1 / 6 + f2 / 3 + f3 / 3 + f4 / 6


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

    positionResults[0] = args.initial
    derivationResults[0] = args.initial_derivative

    positionResults[1] = args.initial + args.tick_interval * args.initial_derivative #TODO: ASK LAU WHETHER EULER START IS APPROPRIATE
    derivationResults[1] = differential(positionResults[0], positionResults[1], args.tick_interval)

    for idx in range(2, len(snapshotTimers)):
        derivationResults[idx] = differential(positionResults[idx - 2], positionResults[idx-1], args.tick_interval)
        positionResults[idx] = rungeKutta(positionResults[idx - 2], positionResults[idx-1], args.tick_interval)

    mappedData = [{"time": snapshotTimers[x], "type": "position", "value": positionResults[x]}for x in range(len(snapshotTimers))]
    mappedData += [{"time": snapshotTimers[x], "type": "derivative", "value": derivationResults[x]}for x in range(len(snapshotTimers))]

    frame = pd.DataFrame(mappedData)
    fig = px.line(frame, x="time", y="value", color="type")
    fig.show()
