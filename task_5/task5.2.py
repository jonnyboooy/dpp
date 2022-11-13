# SUBSCRIBER

from paho.mqtt import client as mqtt
import time

def on_message(client, userdata, message):
    print(str(message.payload.decode("utf-8")))

Brocker = "mqtt.eclipseprojects.io"
client = mqtt.Client("###Subscriber###")
client.connect(Brocker)

client.subscribe("position")

client.on_message = on_message

time.sleep(1)

client.loop_forever()