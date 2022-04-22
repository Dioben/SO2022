from bisect import insort_right
from numpy.random import exponential as rndExponential


def getNextServer1User(time):
    return time + rndExponential(1)

def getServer1ExitTime(time):
    return time + rndExponential(.7)

def getServer2ExitTime(time):
    return time + rndExponential(.9)


events = [None]

server1Queue = []
server2Queue = []

server1Busy = False
server2Busy = False

START_TIME = 0
END_TIME = 1000

#calculate next entry
#if busy add to queue else calculate exit time
def handleServer1Enter(timestamp):
    global server1Busy
    insort_right(events, (getNextServer1User(timestamp),"SERVER_1_ENTER") )
    if server1Busy:
        server1Queue.append(timestamp)
    else:
        insort_right(events, (getServer1ExitTime(timestamp),"SERVER_1_EXIT") )
    server1Busy = True

#check server 1 backlog
#insert into server 2
#if busy add to queue else calculate exit time 
def handleServer1Exit(timestamp):

    if server1Queue:
        oldTs = server1Queue.pop(0)
        insort_right(events, (getServer1ExitTime(timestamp),"SERVER_1_EXIT"))
    else:
        global server1Busy
        server1Busy = False
    
    global server2Busy
    
    if server2Busy:
        server2Queue.append(timestamp)
    else:
        insort_right(events, (getServer2ExitTime(timestamp),"SERVER_2_EXIT") )
    server2Busy = True



#check server 2 backlog
#if any in backlog work, else set self as not busy 
def handleServer2Exit(timestamp):

    if server2Queue:
        oldTs = server2Queue.pop(0)
        insort_right(events, (getServer2ExitTime(timestamp),"SERVER_2_EXIT"))
    else:
        global server2Busy
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
        elif event[1]=="SERVER_2_EXIT":
            handleServer2Exit(event[0])
