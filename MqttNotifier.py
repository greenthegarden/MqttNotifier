#!/usr/bin/env python

#---------------------------------------------------------------------------------------
# Load configuration values
#
#---------------------------------------------------------------------------------------

# see https://wiki.python.org/moin/ConfigParserShootout
from configobj import ConfigObj
config = ConfigObj('MqttNotifier.cfg')

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

	print("Subscribing to topics ...")
	for topic in config['mqtt_topics']['TOPICS'] :
		client.subscribe(topic)
		print("{0}".format(topic))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg) :
  print(msg.topic+" "+str(msg.payload))

client            = mqtt.Client()

client.connect(
               config['mqtt_configuration']['MQTT_BROKER_IP'],
               int(config['mqtt_configuration']['MQTT_BROKER_PORT']),
               int(config['mqtt_configuration']['MQTT_BROKER_PORT_TIMEOUT']),
               )

print("Connected to MQTT broker at {0}".format(config['mqtt_configuration']['MQTT_BROKER_IP']))

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
