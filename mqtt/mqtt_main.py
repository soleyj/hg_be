import paho.mqtt.client as mqtt  # import the client1
import json
import schedule
import time
from dashboard.models import machine_hw,data_hg, data_hg_confgi,data_hg_outputs
from apscheduler.schedulers.background import BackgroundScheduler



def on_message(client, userdata, message):
    
    payload = str(message.payload.decode("utf-8", "ignore"))
    payload_json = json.loads(payload)
    if(message.topic == "homegrown/inputs"):
        machine = machine_hw.objects.get(id_machine = payload_json["id"])
        new_model = data_hg()
        new_model.machine = machine
        new_model.temp_1 = payload_json["temp_1"]
        new_model.humid_1 = payload_json["humid_1"]
        new_model.sw_1 = payload_json["sw_1"]
        new_model.sw_2 = payload_json["sw_2"]
        new_model.save()
        print(payload_json["out_12"][0])
        new_outs_model = data_hg_outputs()
        new_outs_model.Ventilador = payload_json["out_12"][0]
        new_outs_model.Bomba_1 = payload_json["out_12"][1]
        new_outs_model.Bomba_2 = payload_json["out_12"][2]
        new_outs_model.Bomba_3 = payload_json["out_12"][3]
        new_outs_model.Llum = payload_json["rele"][0]
        new_outs_model.Bomba_h20 = payload_json["rele"][1]
        new_outs_model.Altura = 0
        new_outs_model.machine = machine
        print("in")
        new_outs_model.save()
        print("in")



def on_connect(client, userdata, flags, rc):
    client.subscribe("homegrown/inputs")
    client.subscribe("homegrown/data_in/1")
    if rc==0:
        print("connected OK Returned code=",rc)
    else:
        print("Bad connection Returned code=",rc)

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")
    else:
        print("Disconnected")


# broker_address = "192.168.1.46"
broker_address = "localhost"
client = mqtt.Client("wb")  # create new instance
client.connect(broker_address)  # connect to broker
client.on_message = on_message  # attach function to callback
client.on_disconnect = on_disconnect
client.on_connect = on_connect


client.loop_start()



def Publish_alive():
    data ={}
    last_data = data_hg_confgi.objects.order_by("-id")[0]
    data["light_time"] = last_data.Light_time
    data["light_on"] = last_data.Light_on
    data["h20_duty"] = last_data.H20_duty
    data["max_temp"] = last_data.Max_temp
    data["fan_Duty"] = last_data.Fan_Duty
    client.publish("homegrown/data_in/1", json.dumps(data))


scheduler = BackgroundScheduler()
scheduler.add_job(Publish_alive, 'interval', seconds=1)
scheduler.start()