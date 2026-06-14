import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("/home/ids/IDS_Project/logs/stage_latency.csv")
x=df[df["stage"]=="inference"]["latency"]
plt.figure()
plt.plot(x)
plt.xlabel("sample")
plt.ylabel("ms")
plt.title("Latency")
plt.savefig("/home/ids/IDS_Project/pictures/latency.png")
plt.close()

df=pd.read_csv("/home/ids/IDS_Project/logs/resource.csv", header=None)
plt.figure()
plt.plot(df[1])
plt.xlabel("time")
plt.ylabel("%")
plt.title("CPU Usage")
plt.savefig("/home/ids/IDS_Project/pictures/cpu.png")
plt.close()

df=pd.read_csv("/home/ids/IDS_Project/logs/throughput.csv")
plt.figure()
plt.plot(df["flow_per_sec"])
plt.xlabel("time")
plt.ylabel("flow/s")
plt.title("Throughput")
plt.savefig("/home/ids/IDS_Project/pictures/throughput.png")
plt.close()

print()

print(
"Saved:"
)

print(
"latency.png"
)

print(
"cpu.png"
)

print(
"throughput.png"
)
