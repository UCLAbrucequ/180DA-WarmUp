import paho.mqtt.client as mqtt
from rps import *

subscribe_topic = "ch2"
publish_topic = "ch1"

def get_player():
    client.publish(publish_topic, input("Enter name and choice (0|1|2): "))


def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))
    client.subscribe(topic, qos=1)
    get_player()


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print('Unexpected Disconnect')
    else:
        print('Expected Disconnect')

def on_message(client, userdata, message):
    print(int(message.payload))

client = mqtt.Client()

client.on_connect = connect("")
client.on_disconnect = on_disconnect
client.on_message = on_message


client.connect_async('mqtt.eclipseprojects.io')
# client.connect_async("localhost")
client.loop_start()

# while True: # perhaps add a stopping condition using some break or something.
#     pass

client.loop_stop()
client.disconnect()
