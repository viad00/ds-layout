import re
import os

res=[]
spiski=os.listdir(path="/sys/bus/w1/devices/")
spiski.remove("w1_bus_master1")
for deviceNum in  spiski:
    path = "/sys/bus/w1/devices/" + deviceNum + "/w1_read"
    file = open(path)
    values = file.read().split("\n")
    data = []

    for key in values:
        value = re.findall(r"t=(\d{5,6})",key)

        if value != []:
            data.append(value)
            res.append(value)
    print(data)
