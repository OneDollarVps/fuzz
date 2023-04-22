import requests
import time

file = open("commun.txt", "r")
file = file.readlines()
x = 0
while true:
    time.sleep(1)
    for line in file:
        res = requests.get("https://https://wix.com/" + line.rstrip("\r\n"))
        x = x + 1
        print("req code:\t" + str(res.status_code) + "N:\t" + str(x))
