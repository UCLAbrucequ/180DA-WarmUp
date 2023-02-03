import paho.mqtt.client as mqtt
import rps
import Constants

# 0. define callbacks - functions that run when events happen.
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
  print("Connection returned result: " + str(rc))

  # Subscribing in on_connect() means that if we lose the connection and
  # reconnect then subscriptions will be renewed.
  client.subscribe("ch1", qos=1)


# The callback of the client when it disconnects.
def on_disconnect(client, userdata, rc):
  if rc != 0:
    print('Unexpected Disconnect')
  else:
    print('Expected Disconnect')


# The default message callback.
# (you can create separate callbacks per subscribed topic)
def on_message(client, userdata, message):
  if message.topic == 'ch1': 
    num = float(message.payload)
  player2 = input("Enter a choice (rock, paper, scissors): ")
  rps_logic = {0: "rock", 1: "paper", 2: "scissors"}
  rps.play(rps_logic[num], player2)


def create_client():
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
  # client.connect("test.mosquitto.org", 1883, 60)
  # client.connect("mqtt.eclipse.org")

  # 3. call one of the loop*() functions to maintain network traffic flow with the broker.
  client.loop_start()
  # client.loop_forever()
  return client

# client.publish("ece180d/team4/p2", float(np.random.random(1)), qos=1)
# client.publish("ece180d/team4/p3", float(np.random.random(1)), qos=1)

# while True:  # perhaps add a stopping condition using some break or something.
#   pass
  
# use subscribe() to subscribe to a topic and receive messages.

# use publish() to publish messages to the broker.

# use disconnect() to disconnect from the broker.
# client.loop_stop()
# client.disconnect()