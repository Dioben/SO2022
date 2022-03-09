
#based on Simulation Modeling and Analysis, Averil Law

import random
import sys

BASE_SIM_TIME = 0
time_arrival = []
delays = []

# event list  
sched = {}
sched['arrive'] = BASE_SIM_TIME + random.uniform(0,10)
sched['depart'] = 1e10

# statistics
num_custs_delayed = 0

def calculateNextEvent(): 
    
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

    global num_custs_delayed

    sched['arrive'] = sim_time + random.uniform(0,10)
    time_arrival.append(sim_time)
    
    if status == 'busy':
        num_custs_delayed += 1
    else:
       status = 'busy'
       sched['depart'] = sim_time + random.uniform(0,9.5)

    print(f'arrive event at {sim_time:.2f} size of queue is {len(time_arrival)-1 if (time_arrival)  else 0}')
    return status
 
def depart(sim_time):
    arrival = time_arrival.pop(0)
    if len(time_arrival) == 0:
       status = 'idle'
       sched['depart'] = 1e10
    else:
       sched['depart'] = sim_time + random.uniform(3,9)
       
       status = "busy"

    print(f'depart event at {sim_time:.2f} size of queue is {len(time_arrival)-1 if (time_arrival)  else 0}')
    return status

def main():

    # simulation clock
    sim_time = BASE_SIM_TIME
    next_event_type = ''
    # state variables
    status   = 'idle'
  

    while num_custs_delayed < 5:
        
        next_event_type,sim_time = calculateNextEvent()
        
        if next_event_type == 'arrive':
            status = arrive(sim_time,status)
        elif next_event_type == 'depart':
            status = depart(sim_time)

if __name__ =="__main__":
    main()