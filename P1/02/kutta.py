import argparse  # process command line
import plotly.express as px  # plotting libs
import pandas as pd
from common import acceleration

def kuttaPosition(pos, vel, timeInterval):
    f1 = timeInterval * vel
    f2 = timeInterval * (vel + f1/2)
    f3 = timeInterval * (vel + f2/2)
    f4 = timeInterval * (vel + f3)
    return pos + f1/6 + f2/3 + f3/3 + f4/6

def kuttaVelocity(vel, timeInterval):
    f1 = timeInterval * acceleration(vel)
    f2 = timeInterval * acceleration(vel + f1/2)
    f3 = timeInterval * acceleration(vel + f2/2)
    f4 = timeInterval * acceleration(vel + f3)
    return vel + f1/6 + f2/3 + f3/3 + f4/6

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--initial",
        help="Initial height",
        type=float,
        required=True
    )
    parser.add_argument(
        "--initial-derivative",
        help="Initial derivative (velocity)",
        type=float,
        required=True
    )
    parser.add_argument(
        "--mass",
        help="initial object mass, defaults to 1",
        type=float,
        default=1
    )
    parser.add_argument(
        "--gravity",
        help="Gravity constant, defaults to 9.81",
        type=float,
        default=9.81
    )
    parser.add_argument(
        "--tick-interval",
        help="How often data is computed",
        type=float,
        default=1
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
    acceleration.m = args.mass
    acceleration.g = args.gravity
    acceleration.u = args.wind_resistance

    snapshotTimers = [x * args.tick_interval for x in range(int(args.stop_point / args.tick_interval))]
    positionResults = [None for _ in range(len(snapshotTimers))]
    velocityResults = [None for _ in range(len(snapshotTimers))]

    positionResults[0] = args.initial
    velocityResults[0] = args.initial_derivative

    for idx in range(1, len(snapshotTimers)):
        # position and velocity use the previous step to calculate
        positionResults[idx] = kuttaPosition(positionResults[idx-1], velocityResults[idx-1], args.tick_interval)
        velocityResults[idx] = kuttaVelocity(velocityResults[idx-1], args.tick_interval)

    mappedData = [{"time": snapshotTimers[x], "type": "position", "value": positionResults[x]} for x in range(len(snapshotTimers))]
    mappedData += [{"time": snapshotTimers[x], "type": "velocity", "value": velocityResults[x]} for x in range(len(snapshotTimers))]

    frame = pd.DataFrame(mappedData)
    fig = px.line(frame, x="time", y="value", color="type")
    fig.show()
