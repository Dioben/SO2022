def velocity(previousPos, currentPos, timeInterval):
    return (currentPos - previousPos) / timeInterval

def acceleration(velocity):
    return -acceleration.g + acceleration.u / acceleration.m * velocity**2