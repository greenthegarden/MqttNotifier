# config file creator

from configobj import ConfigObj
config = ConfigObj()
config.filename = 'MqttNotifier.cfg'


# mqtt configuration
mqtt_configuration = {
	'MQTT_BROKER_IP'           : "192.168.1.55",
	'MQTT_BROKER_PORT'         : "1883",
	'MQTT_BROKER_PORT_TIMEOUT' : "60",
	}
config['mqtt_configuration'] = mqtt_configuration

config['mqtt_topics'] = {}
# add additional topics to subscribe to here!!
config['mqtt_topics']['TOPICS'] = [
                                   'all/contoller/dst',
                                   'pibot/motor/#',
                                   'pibot/controller/#',
                                   'pibot/tool/#',
                                   'relayduino/status/#',
                                   'relayduino/request/#',
                                   'relayduino/control/#',
                                   'lcddisplay/status/#',
                                   'weather/status/#',
                                   'weather/measurement/#',
                                   'weather/sunairplus/#',
                                   'weather/sunairplus/#',
                                   'bomforecast/#',
 #                                 '$SYS/#',
                                   ]

config.write()
