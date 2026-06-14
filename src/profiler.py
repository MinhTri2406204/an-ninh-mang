import time
import csv
import os

if not os.path.exists("/home/ids/IDS_Project/logs/stage_latency.csv"):
    with open("/home/ids/IDS_Project/logs/stage_latency.csv", "w") as f:
        writer=csv.writer(f)
        writer.writerow(["stage", "latency"])

class Profile:
    def __init__(self,name):
        self.name=name
        self.start=time.time()
    def stop(self):
        latency=(time.time()-self.start)*1000
        with open("/home/ids/IDS_Project/logs/stage_latency.csv", "a") as f:
            writer=csv.writer(f)
            writer.writerow([self.name,latency])
        return latency
