import paho.mqtt.client as mqtt  # import the client1
import json
import schedule
import time
from dashboard.models import machine_hw,data_hg

def on_message(client, userdata, message):
    
    payload = str(message.payload.decode("utf-8", "ignore"))
    payload_json = json.loads(payload)
    print(payload_json)   
    if(message.topic == "homegrown/inputs"):
        new_model = data_hg()
        new_model.machine = machine_hw.objects.get(id_machine = payload_json["id"])
        new_model.temp_1 = payload_json["temp_1"]
        new_model.humid_1 = payload_json["humid_1"]
        new_model.sw_1 = payload_json["sw_1"]
        new_model.sw_2 = payload_json["sw_2"]
        new_model.save()

        pass


def on_connect(client, userdata, flags, rc):
    client.subscribe("homegrown/inputs")
    if rc==0:
        print("connected OK Returned code=",rc)
    else:
        print("Bad connection Returned code=",rc)

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")
    else:
        print("Disconnected")


broker_address = "192.168.1.46"
client = mqtt.Client("wb")  # create new instance
client.connect(broker_address)  # connect to broker
client.on_message = on_message  # attach function to callback
client.on_disconnect = on_disconnect
client.on_connect = on_connect
client.loop_start()