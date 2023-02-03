import paho.mqtt.client as mqtt
import numpy as np
from rps import *


# 0. define callbacks - functions that run when events happen.
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
  print("Connection returned result: " + str(rc))

  # Subscribing in on_connect() means that if we lose the connection and
  # reconnect then subscriptions will be renewed.
  client.subscribe("ece180d/team4/player1", qos=1)
  client.subscribe("ece180d/team4/player2", qos=1)



# The callback of the client when it disconnects.
def on_disconnect(client, userdata, rc):
  if rc != 0:
    print('Unexpected Disconnect')
  else:
    print('Expected Disconnect')


# The default message callback.
# (won't be used if only publishing, but can still exist)
def on_message(client, userdata, message):
  # print('Received message: "' + str(message.payload) + '" on topic "' +
  #       message.topic + '" with QoS ' + str(message.qos))

    rps_logic = {0: "rock", 1: "paper", 2: "scissors"}
    player1 = False
    player2 = False

    if message.topic == 'ece180d/team4/player1': 
        num = float(message.payload)
        #client.publish('ece180d/team4/ref', , qos=1)
        print("pub: ", num)
        player1 = True

    while player2 == False:
        if message.topic == 'ece180d/team4/player2':
            num_2 = float(message.payload)
            print("pub2: ", num_2)
            #client.publish('ece180d/team4/ref', num+1, qos=1)
            player2 = True
    
    print(player1)
    print(player2)
    if player1==True and player2==True:
        print("player1: ", rps_logic[num], "player2: ", rps_logic[num_2])
        play(rps_logic[num], rps_logic[num_2])
    #play(num, num_2)
    
        

    
  



# 1. create a client instance.
client = mqtt.Client()
# add additional client options (security, certifications, etc.)
# many default options should be good to start off.
# add callbacks to client.
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

# 2. connect to a broker using one of the connect*() functions.
# client.connect_async("test.mosquitto.org")
client.connect_async('mqtt.eclipseprojects.io')

# 3. call one of the loop*() functions to maintain network traffic flow with the broker.
client.loop_start()

# 4. use subscribe() to subscribe to a topic and receive messages.

# 5. use publish() to publish messages to the broker.
# payload must be a string, bytearray, int, float or None.
print('Publishing...')
for i in range(1):
    print
    
    

while True: 
  pass

# 6. use disconnect() to disconnect from the broker.
client.loop_stop()
client.disconnect()