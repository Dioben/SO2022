import argparse  # process command line
import plotly.express as px  # plotting libs
import pandas as pd
from common import acceleration
from euler import eulerPosition, eulerVelocity
from kutta import kuttaPosition, kuttaVelocity

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

    snapshotTimers = [x*args.tick_interval for x in range(int(args.stop_point/args.tick_interval))]

    positionResultsEuler = [None for _ in range(len(snapshotTimers))]
    velocityResultsEuler = [None for _ in range(len(snapshotTimers))]

    positionResultsKutta = [None for _ in range(len(snapshotTimers))]
    velocityResultsKutta = [None for _ in range(len(snapshotTimers))]

    positionResultsEuler[0] = args.initial
    velocityResultsEuler[0] = args.initial_derivative

    positionResultsKutta[0] = args.initial
    velocityResultsKutta[0] = args.initial_derivative

    for idx in range(1, len(snapshotTimers)):
        # position and velocity use the previous step to calculate
        positionResultsEuler[idx] = eulerPosition(positionResultsEuler[idx-1], velocityResultsEuler[idx-1], args.tick_interval)
        velocityResultsEuler[idx] = eulerVelocity(velocityResultsEuler[idx-1], args.tick_interval)

        positionResultsKutta[idx] = kuttaPosition(positionResultsKutta[idx-1], velocityResultsKutta[idx-1], args.tick_interval)
        velocityResultsKutta[idx] = kuttaVelocity(velocityResultsKutta[idx-1], args.tick_interval)

    mappedData = [{"method": "Euler", "time": snapshotTimers[x], "type": "Euler position", "value": positionResultsEuler[x]} for x in range(len(snapshotTimers))]
    mappedData += [{"method": "Euler", "time": snapshotTimers[x], "type": "Euler velocity", "value": velocityResultsEuler[x]} for x in range(len(snapshotTimers))]

    mappedData += [{"method": "Kutta", "time": snapshotTimers[x], "type": "Kutta position", "value": positionResultsKutta[x]} for x in range(len(snapshotTimers))]
    mappedData += [{"method": "Kutta", "time": snapshotTimers[x], "type": "Kutta velocity", "value": velocityResultsKutta[x]} for x in range(len(snapshotTimers))]

    frame = pd.DataFrame(mappedData)
    fig = px.line(frame, x="time", y="value", color="type")
    fig.show()
