
#based on Simulation Modeling and Analysis, Averil Law

from random import random,uniform
from numpy.random import exponential as rndExponential
from bisect import insort_right

BASE_SIM_TIME = 0
MAX_SIM_TIME = 120
INTIAL_INVENTORY = 60
ORDER_SIZES = {1:1,2:2,3:2,4:1}
SETUP_COST = 32
INCREMENTAL_COST = 3


#returns time,size
def getNextPurchase(simTime):
    return simTime + rndExponential(0.1)

def getNextPurchaseItems():
    roll = random()*6 #value between 0 and 6
    for size,weight in ORDER_SIZES.items():
        roll -= weight
        if roll <= 0:
            break 
    return size


def getNextOrderArrival(simTime):
    return simTime + uniform(.5,1)

def getNextOrderCost(s,S,I):
    if I>s:
        return 0
    return SETUP_COST + INCREMENTAL_COST * (S-I)

def getHandlingCosts(I):
    return I if I else 0

def getShortageCosts(I):
    return I*-5 if I<0 else 0

def monthlyEval(s,S,I):
    sc = getShortageCosts(I)
    hc = getHandlingCosts(I)
    oc = getNextOrderCost(s,S,I)
    return sc,hc, oc


def main(s,S):

    # simulation clock
    sim_time = BASE_SIM_TIME
    limit_time = MAX_SIM_TIME
    
    #stats
    ordering_cost = 0
    handling_cost = 0
    shortage_cost = 0


    I = 60
    
    events = [ (x,"INV_CHECK") for x in range(sim_time,122)]
    insort_right(events,(getNextOrderArrival(sim_time),"DEMAND")) #force in 1st demand
    while True:
        event = events.pop(0)
        event_time = event[0]
        event_type = event[1]
        sim_time = event_time
        if sim_time>=limit_time:
            break
        if event_type == 'INV_CHECK':
            sc,hc, oc = monthlyEval(s,S,I)
            shortage_cost+=sc
            handling_cost+=hc
            ordering_cost+=oc
            if oc: #schedule order arrival
                arrival = getNextOrderArrival(sim_time)
                insort_right(events, (arrival,'ARRIVAL',S-I))      
        elif event_type == 'ARRIVAL':
            I+=event[2]
        elif event_type == 'DEMAND':
            quant = getNextPurchaseItems()
            I-=quant
            insort_right(events,(getNextOrderArrival(sim_time),"DEMAND")) #add next DEMAND

    return ordering_cost+handling_cost+shortage_cost ,ordering_cost,handling_cost,shortage_cost
if __name__ =="__main__":
    smallS = [20 * i for i in range(1,4)]
    bigS = [20 * i for i in range(2,6)]
    combos = [(x,y) for x in smallS for y in bigS if x<y]
    for x,y in combos:
        stats = main(x,y)
        print(f"Stats for parameters s={x} , S={y}")
        print(f"Total cost :{stats[0]}  Ordering Cost:{stats[1]}  handling_cost:{stats[2]}  shortage_cost:{stats[3]}")
        print()