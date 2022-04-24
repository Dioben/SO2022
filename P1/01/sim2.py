#functional differences from sim1:
#   there is now an event for entering second server + a delay calc for that
#   there is a new function to handle that event
#   all code relative to handling server 2 on exit server 1 has been moved there
from bisect import insort_right
from numpy.random import exponential as rndExponential
from random import uniform as rndUniform


def getNextServer1User(time):
    return time + rndExponential(1)

def getServer1ExitTime(time):
    return time + rndExponential(.7)

def getServer2EnterTime(time):
    return time + rndUniform(0, 2)

def getServer2ExitTime(time):
    return time + rndExponential(.9)


events = [None]

server1Queue = []
server2Queue = []

server1Busy = False
server2Busy = False

#for statistics
#when applicable only considers users who have actually finished usage
server1Served = 0 
server2Served = 0

server1LastEntryTS = None
server2LastEntryTS = None

server1LastQueueSizeEvaluationTS = 0
server2LastQueueSizeEvaluationTS = 0

server1Delay = 0 
server2Delay = 0

server1QueueSizeAverage = 0 
server2QueueSizeAverage = 0

server1Usage = 0 
server2Usage = 0


START_TIME = 0
END_TIME = 1000

#calculate next entry
#if busy add to queue else calculate exit time
#updates queue size average
def handleServer1Enter(timestamp):
    global server1Busy,server1LastEntryTS,server1LastQueueSizeEvaluationTS,server1QueueSizeAverage

    server1QueueSizeAverage+= (timestamp-server1LastQueueSizeEvaluationTS) * len(server1Queue)
    server1LastQueueSizeEvaluationTS = timestamp

    insort_right(events, (getNextServer1User(timestamp),"SERVER_1_ENTER") )
    if server1Busy:
        server1Queue.append(timestamp)
    else:
        insort_right(events, (getServer1ExitTime(timestamp),"SERVER_1_EXIT") )
        server1LastEntryTS = timestamp
    server1Busy = True

#check server 1 backlog
#insert into server 2
#if busy add to queue else calculate exit time 
#updates served count, calculates server delay,usage rate,queue size averages
def handleServer1Exit(timestamp):
    global server1Served,server1LastEntryTS,server1Usage,server1LastQueueSizeEvaluationTS,server1QueueSizeAverage,server1Delay,server1Busy

    server1Served+=1
    server1Usage+=timestamp-server1LastEntryTS
    server1QueueSizeAverage+= (timestamp-server1LastQueueSizeEvaluationTS) * len(server1Queue)
    server1LastQueueSizeEvaluationTS = timestamp


    if server1Queue:
        oldTs = server1Queue.pop(0)
        server1Delay += timestamp-oldTs
        server1LastEntryTS = timestamp
        insort_right(events, (getServer1ExitTime(timestamp),"SERVER_1_EXIT"))
    else:
        server1Busy = False
    
    insort_right(events, (getServer2EnterTime(timestamp),"SERVER_2_ENTER"))

#functionally same as server 1 enter except it doesnt calculate next server 1 enter
def handleServer2Enter(timestamp):
    global server2Busy,server2LastEntryTS,server2LastQueueSizeEvaluationTS,server2QueueSizeAverage

    server2QueueSizeAverage+= (timestamp-server2LastQueueSizeEvaluationTS) * len(server2Queue)
    server2LastQueueSizeEvaluationTS = timestamp

    if server2Busy:
        server2Queue.append(timestamp)
    else:
        server2LastEntryTS = timestamp
        insort_right(events, (getServer2ExitTime(timestamp),"SERVER_2_EXIT") )
    server2Busy = True

#check server 2 backlog
#if any in backlog work, else set self as not busy 
#updates served count, calculates server delay,usage rate,queue size averages
def handleServer2Exit(timestamp):
    global server2Served,server2LastEntryTS,server2Usage,server2Delay,server2Busy,server2LastQueueSizeEvaluationTS,server2QueueSizeAverage
    
    server2Served+=1
    server2Usage+=timestamp-server2LastEntryTS

    server2QueueSizeAverage+= (timestamp-server2LastQueueSizeEvaluationTS) * len(server2Queue)
    server2LastQueueSizeEvaluationTS = timestamp

    if server2Queue:
        oldTs = server2Queue.pop(0)
        server2Delay += timestamp-oldTs
        server2LastEntryTS = timestamp
        insort_right(events, (getServer2ExitTime(timestamp),"SERVER_2_EXIT"))
    else:
        server2Busy = False


if __name__ == "__main__":
    
    #register first user
    events[0]=(getNextServer1User(START_TIME),"SERVER_1_ENTER")
    
    while True:
        event = events.pop(0)
        #are we past time limit?
        if event[0]> END_TIME:
            break
        #handle given event
        if event[1]=="SERVER_1_ENTER":
            handleServer1Enter(event[0])
        elif event[1]=="SERVER_1_EXIT":
            handleServer1Exit(event[0])
        elif event[1]=="SERVER_2_ENTER":
            handleServer2Enter(event[0])
        elif event[1]=="SERVER_2_EXIT":
            handleServer2Exit(event[0])
    
    #UPDATE RUNTIME
    if server1Busy:
        server1Usage+=END_TIME-server1LastEntryTS
    if server2Busy:
        server2Usage+=END_TIME-server2LastEntryTS
    
    #UPDATE QSA
    server1QueueSizeAverage += (END_TIME - server1LastQueueSizeEvaluationTS) * len(server1Queue)
    server2QueueSizeAverage += (END_TIME - server2LastQueueSizeEvaluationTS) * len(server2Queue)

    server1QueueSizeAverage/=END_TIME
    server2QueueSizeAverage/=END_TIME

    print(f"{'#'*11} Server 1 Stats {'#'*11}")
    print(f"Average Queue Delay: {server1Delay/server1Served :.3f} minutes")
    print(f"           Use Time: {server1Usage :.3f} minutes")
    print(f" Average Queue Size: {server1QueueSizeAverage :.3f} users")

    print(f"\n{'#'*11} Server 2 Stats {'#'*11}")
    print(f"Average Queue Delay: {server2Delay/server2Served :.3f} minutes")
    print(f"           Use Time: {server2Usage :.3f} minutes")
    print(f" Average Queue Size: {server2QueueSizeAverage :.3f} users")