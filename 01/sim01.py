
#based on Simulation Modeling and Analysis, Averil Law

import random
import sys

from pandas import to_timedelta

BASE_SIM_TIME = 0
time_arrival = []

# event list  
sched = {}
sched['arrive'] = BASE_SIM_TIME + random.uniform(0,10)
sched['depart'] = 1e10

# statistics
num_custs_delayed = 0
delays = []
served = 0


def calculateNextEvent(): 
    global last_time
    min_time_next_event = 1e9

    next_event_type = ''

    for e,time in sched.items():
        if time < min_time_next_event:
            min_time_next_event = time
            next_event_type = e

    if next_event_type == '':
        print('Event list is empty at time', sim_time)
        sys.exit()

    sim_time = min_time_next_event
    return next_event_type,sim_time

def arrive(sim_time, status):
    global served
    global num_custs_delayed

    served+=1
    sched['arrive'] = sim_time + random.uniform(0,10)
    time_arrival.append(sim_time)
    
    if status == SERVERS:
        num_custs_delayed += 1
    else:
       status+= 1
       sched['depart'] = sim_time + random.uniform(0,9.5)

    print(f'arrive event at {sim_time:.2f} size of queue is {len(time_arrival)-1 if (time_arrival)  else 0}, status is {status}')
    return status
 
def depart(sim_time,status):
    arrival = time_arrival.pop(0)
    if len(time_arrival) == 0:
       status-=1
       sched['depart'] = 1e10
    else:
       sched['depart'] = sim_time + random.uniform(3,9)  

    print(f'depart event at {sim_time:.2f} size of queue is {len(time_arrival)-1 if (time_arrival)  else 0}, status is {status}')
    if status==SERVERS:
        delays.append(sim_time - time_arrival[0])
        print(f"A costumer had been delayed for {delays[-1]}")
    return status

def main():

    # simulation clock
    sim_time = BASE_SIM_TIME
    last_time = sim_time
    used_time = 0
    meanQueueSize = 0
    next_event_type = ''
    # state variables
    status   = 0
    
  
    next_event_type,sim_time = calculateNextEvent()
    while num_custs_delayed < 5:
        used_time+= (sim_time-last_time)*(status)
        meanQueueSize+= (0 if not time_arrival else len(time_arrival)-1)*(sim_time-last_time)
        if next_event_type == 'arrive':
            status = arrive(sim_time,status)
        elif next_event_type == 'depart':
            status = depart(sim_time,status)
        
        
        last_time = sim_time
        next_event_type,sim_time = calculateNextEvent()
    meanQueueSize/=last_time
    print()
    print(f"received {served} costumers")
    print(f"fully served {served - len(time_arrival)} costumers")
    print("actual full delays:")
    print(delays)
    print(f"average delay for actually served costumers was {sum(delays)/(served - len(time_arrival))}")
    for x in time_arrival: #count people we didnt even serve
        delays.append(sim_time - x)
    print("all delays:")
    print(delays)
    print(f"true average delay was {sum(delays)/served}")
    print(f"Mean Queue Size: {meanQueueSize}")
    print(f"Total Use Time: {used_time:.2f}")
    print(f"Average Server Use Time: {used_time/SERVERS:.2f}")
    print(f"Use Rate: {used_time/last_time*100/SERVERS:.2f}%")
    
    return delays,meanQueueSize,used_time ,served
if __name__ =="__main__":
    SERVERS = 10
    runs = 10
    totaldelay = []
    mqs = 0
    used_time = 0
    total_served =0
    for x in range(runs):
        delays,meanQueueSize,time,served = main()
        num_custs_delayed = 0
        totaldelay.extend(delays)
        mqs+=meanQueueSize
        used_time+=time
        total_served+=served
    print("-"*50)
    print("-"*50)
    print(f"True Average Delay: {sum(totaldelay)/total_served}")
    print(f"Mean Queue Size: {mqs/runs}")
    print(f"Average Server Use: {used_time/SERVERS/runs}")