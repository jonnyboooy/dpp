from paho.mqtt import client as mqtt
from random import randint
import time
Brocker = "mqtt.eclipseprojects.io"
client = mqtt.Client("###Publisher###")
client.connect(Brocker)

def v(t,v0,v1,v2):
    v_result = (v0*0.6)+(v1*0.3)+(v2*0.1)
    if t == 0:
        return v_result, 0, 0
    elif t == 1:
        return v_result, v0, 0
    else:
        return v_result, v0, v1

def print_time(second):
    second += 1
    time.sleep(1)
    return second

if __name__ == '__main__':
    sec = 0
    v0 = 10
    v1 = 0
    v2 = 0

    while True:
        output_str = 'V(t = ' + str(sec) + ') = ' + str(v0)
        client.publish("Topic", output_str)
        sec = print_time(sec)
        v0,v1,v2 = v(sec,v0,v1,v2)
