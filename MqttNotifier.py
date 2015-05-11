#!/usr/bin/env python

#---------------------------------------------------------------------------------------
# Load configuration values
#
#---------------------------------------------------------------------------------------

# see https://wiki.python.org/moin/ConfigParserShootout
from configobj import ConfigObj
config = ConfigObj('mqttNotifier.cfg')

print("{0}".format("MQTT Notifier"))


#---------------------------------------------------------------------------------------
# Modules and methods to support MQTT
#
#---------------------------------------------------------------------------------------

import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc) :

  print("Connected with result code "+str(rc))

  # Subscribing in on_connect() means that if the connection is lost
  # the subscriptions will be renewed when reconnecting.

  for topic in config['mqtt_topics']['TOPICS'] :
  	client.subscribe(topic)

# system topics
#   #client.subscribe("$SYS/#")
#
# general topics
#   client.subscribe("all/contoller/dst")
#
# pibot topics
#   client.subscribe("pibot/motor/#")
#   client.subscribe("pibot/controller/#")
#   client.subscribe("pibot/tool/#")
#
# relayduino topics
#   client.subscribe("relayduino/status/#")
#   client.subscribe("relayduino/request/#")
#   client.subscribe("relayduino/control/#")
#
# lcd display topics
#   client.subscribe("lcddisplay/status/#")
#
# weather station topics
# #  client.subscribe("weather/status/#")
# #  client.subscribe("weather/measurement/#")
# #  client.subscribe("weather/sunairplus/#")
#   client.subscribe("weather/#")
#
#   client.subscribe("bomforecast/#")
#
# add additional topics to subscribe to here!!

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg) :
  print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client_addr = "192.168.1.55"
#client_addr = "localhost"

client.connect(client_addr, 1883, 60) # address of broker, broker port,

client.loop_forever()
