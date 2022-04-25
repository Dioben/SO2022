def velocity(previousPos, currentPos, timeInterval):
    return (currentPos - previousPos) / timeInterval

def acceleration(velocity):
    acc = -acceleration.g + acceleration.u / acceleration.m * velocity**2
    if acc < 1e-100: # stops acceleration overflow (too many decimal places) if it becomes too small
        return 0
    return acc