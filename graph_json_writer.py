import json
import pprint
from pyconfig import *
from random import randint
import time
from datetime import datetime


if __name__ == "__main__":

    ##############
    # ENTRY DATA #
    ##############
    deviceid = "VSR1000"
    INDEX = 47
    ifDescr = "GigabitEthernet0/0"
    ifHCInOctets = randint(0, 1000)
    ifHCOutOctets = randint(0, 1000)
    ifSpeed = 1000000000

    try:
        with open('html/data/interface_stats.json') as json_file:
            interface_stats = json.load(json_file)
    except FileNotFoundError:
        interface_stats = dict()

    #
    # READ IS DONE, NOW WE CHECK
    #
    #print(json.dumps(interface_stats, indent=4))

    #
    # EXTEND
    #

    now = datetime.now()
    print("Now: " + str(now))
    # print("Printable: " + str(now.strftime('%Y-%m-%d %H:%M:%S')))
    timestamp = int(datetime.timestamp(now))
    print("Timestamp: " + str(timestamp))
    # REVERSE IS
    #time.sleep(1)
    #print("Timestamp: " + str(int(datetime.timestamp(datetime.now()))))
    #time.sleep(10)
    #print("Timestamp: " + str(int(datetime.timestamp(datetime.now()))))
    #
    # READ IS DONE, NOW WE CHECK
    #
    print(json.dumps(interface_stats, indent=4))

    #interface_stats[deviceid] = device_interfaces_stats
    #with open('html/data/interface_stats.json', 'w') as outfile:
     #   json.dump(interface_stats, outfile, sort_keys=True, indent=4)