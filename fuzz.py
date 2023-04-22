import requests
import time
file = open("commun.txt","r")
file = file.readlines()
while(True):
  time.sleep(1)
  for line in file:
    res= requests.get("https://https://wix.com/"+line.rstrip("\r\n"))
    print("req code:\t"+str(res.status_code)+"\t length:\t"+str(len(res.text))
