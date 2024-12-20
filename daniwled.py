import requests
from time import sleep
import json


f = open("wledip.txt", "r")

wled_device_ip = f.readline()
api_endpoint = f"http://{wled_device_ip}/json/state"

def wled(bright):
    json_data = {"on":True,"bri":bright,"transition":7,"mainseg":0,"seg":[{"id":0,"start":0,"stop":157,"grp":1,"spc":0,"of":0,"on":True,"frz":False,"bri":bright,"cct":127,"col":[[128,128,128],[0,0,0],[255,0,0]],"fx":0,"sx":0,"ix":105,"pal":2,"sel":True,"rev":False,"mi":False},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0}]}
    headers ={'content-type':'application/json'}
    r = requests.post(api_endpoint, data=json.dumps(json_data),headers=headers)

def wled_off():
    json_data = {"on":False,"bri":2,"transition":7,"mainseg":0,"seg":[{"id":0,"start":0,"stop":157,"grp":1,"spc":0,"of":0,"on":True,"frz":False,"bri":2,"cct":127,"col":[[128,128,128],[0,0,0],[255,0,0]],"fx":0,"sx":0,"ix":105,"pal":2,"sel":True,"rev":False,"mi":False},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0}]}
    headers ={'content-type':'application/json'}
    r = requests.post(api_endpoint, data=json.dumps(json_data),headers=headers)
    
def wled_on(bright):
    json_data = {"on":True,"bri":bright,"transition":7,"mainseg":0,"seg":[{"id":0,"start":0,"stop":157,"grp":1,"spc":0,"of":0,"on":True,"frz":False,"bri":bright,"cct":127,"col":[[128,128,128],[0,0,0],[255,0,0]],"fx":0,"sx":0,"ix":105,"pal":2,"sel":True,"rev":False,"mi":False},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0},{"stop":0}]}
    headers ={'content-type':'application/json'}
    r = requests.post(api_endpoint, data=json.dumps(json_data),headers=headers)
    
def wled_aurora(bri):
    json_data = {"on":True,"bri":bri,"transition":7,"ps":-1,"pl":-1,"nl":{"on":False,"dur":60,"mode":1,"tbri":0,"rem":-1},"udpn":{"send":False,"recv":True,"sgrp":1,"rgrp":1},"lor":0,"mainseg":0,"seg":[{"id":0,"start":0,"stop":75,"len":75,"grp":1,"spc":0,"of":0,"on":True,"frz":False,"bri":bri,"cct":127,"set":0,"col":[[128,128,128],[0,0,0],[255,0,0]],"fx":38,"sx":24,"ix":128,"pal":50,"c1":128,"c2":128,"c3":16,"sel":True,"rev":False,"mi":False,"o1":False,"o2":False,"o3":False,"si":0,"m12":0}]}
    headers ={'content-type':'application/json'}
    r = requests.post(api_endpoint, data=json.dumps(json_data),headers=headers)


