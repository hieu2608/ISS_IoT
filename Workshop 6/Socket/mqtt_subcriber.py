from mosquitto import *
def on_message(c, userdata, mesg):
    print "message: %s %s %s" % (userdata, mesg.topic, mesg.payload)

client = Mosquitto("my_id_sub")
client.connect("localhost")
client.on_message = on_message
client.subscribe("temp")
while True:
    client.loop()