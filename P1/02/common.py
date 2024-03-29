def acceleration(vel):
    try:
        return -acceleration.g + acceleration.u / acceleration.m * vel**2
    except OverflowError:
        print("Error: Acceleration overflow.")
        exit(1);