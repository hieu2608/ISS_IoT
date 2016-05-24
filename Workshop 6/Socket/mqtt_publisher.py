from mosquitto import *
import datetime

client = Mosquitto("my_id_pub")
client.connect("localhost")
message = str(datetime.datetime.now())
topic = "temp"
client.publish(topic, message)