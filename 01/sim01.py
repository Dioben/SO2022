
#based on Simulation Modeling and Analysis, Averil Law

import random


def timing():
    global next_event_type 
    global time_next_event
    global sim_time
    
    min_time_next_event = 1e9

    next_event_type = ''

    for e in time_next_event:
        if time_next_event[e] < min_time_next_event:
            min_time_next_event = time_next_event[e]
            next_event_type = e

    if next_event_type == '':
        print('Event list is emplty at time', sim_time)
        sys.exit()

    sim_time = min_time_next_event

def arrive():
    global time_next_event
    global server_status
    global num_custs_delayed
    global time_arrival
    
    time_next_event['arrive'] = sim_time + random.uniform(0,10)

    if server_status == 'busy':
        time_arrival.append(sim_time)
    else:
       num_custs_delayed += 1
       server_status = 'busy'
       time_next_event['depart'] = sim_time + random.uniform(0,5)

    print('arrive event at {0:5.2f} size of queue is {1:2d}'.format(sim_time, len(time_arrival)))
 
def depart():
    global time_next_event
    global server_status
    global num_custs_delayed
    global time_arrival

    if len(time_arrival) == 0:
       server_status = 'idle'
       time_next_event['depart'] = 1e10
    else:
       num_custs_delayed +=1
       time_next_event['depart'] = sim_time + random.uniform(3,9)

       time_arrival.pop(0)

    print('depart event at {0:5.2f} size of queue is {1:2d}'.format(sim_time, len(time_arrival)))


# main

# initialize

# simulation clock
sim_time = 0.0

# state variables
server_status   = 'idle'
num_in_q        = 0
time_last_event = 0.0

# statistics
num_custs_delayed = 0
    
# event list
time_next_event = {}
time_next_event['arrive'] = sim_time + random.uniform(0,10)
time_next_event['depart'] = 1e10

next_event_type = ''

time_arrival = []

while num_custs_delayed < 5:
    
    timing()
    
    if next_event_type == 'arrive':
        arrive()
    elif next_event_type == 'depart':
        depart()
       