def velocity(previousPos, currentPos, timeInterval):
    return (currentPos - previousPos) / timeInterval

def acceleration(velocity):
    try:
        return -acceleration.g + acceleration.u / acceleration.m * velocity**2
    except:
        print("Wind resistance value caused an overflow by making acceleration too big.")
        exit(1);