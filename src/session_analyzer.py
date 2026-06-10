from collections import defaultdict
import time

sessions=defaultdict(list)
WINDOW=60
def analyze(flow):
    ip=flow.get("src_ip", "unknown")
    now=time.time()
    sessions[ip].append(now)
    sessions[ip]=[
        x
        for x in sessions[ip]
        if now-x<WINDOW
    ]
    count=len(
        sessions[ip]
    )
    flow["session_flow_count"]=count
    return flow
