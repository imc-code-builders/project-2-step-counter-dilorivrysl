from microbit import *
import log

log.set_labels('strength')
while True:
    # Use log.add() to record the accelerometer strength
    strength = accelerometer.get_strength()
    # You can get the strength with accelerometer.get_strength()
    # You must pass a dictionary to log.add
    # with the key as the name of the data ('strength') and the value as the actual strength
    dict = {"strength": strength} 

    # pass dict to log.add
    log.add(dict)
    

    sleep(100)