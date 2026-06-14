import time
import numpy as np

flows = {}

def get_key(flow_dict):
    return (
        flow_dict.get("src_ip"),
        flow_dict.get("dst_ip"),
        flow_dict.get("src_port"),
        flow_dict.get("dst_port"),
        flow_dict.get("protocol")
    )

def build_flow(flow_dict):
    key = get_key(flow_dict)
    now = time.time()

    if key not in flows:
        flows[key] = {
            "start": now,
            "packet_sizes": [],
            "iat": [],
            "packet_count": 0,
            "byte_count": 0,
            "syn": 0,
            "ack": 0,
            "fin": 0,
            "rst": 0,
            "psh": 0
        }

    f = flows[key]

    bidirectional_packets = flow_dict.get("bidirectional_packets", 0)
    bidirectional_bytes = flow_dict.get("bidirectional_bytes", 0)

    f["packet_count"] += bidirectional_packets
    f["byte_count"] += bidirectional_bytes

    size = bidirectional_bytes
    f["packet_sizes"].append(size)

    duration = now - f["start"]

    if len(f["iat"]) > 0:
        f["iat"].append(now - f["iat"][-1])
    else:
        f["iat"].append(0)

    try:
        flags_val = flow_dict.get("tcp_flags", 0)

        if flags_val & 0x02: f["syn"] += 1
        if flags_val & 0x10: f["ack"] += 1
        if flags_val & 0x01: f["fin"] += 1
        if flags_val & 0x04: f["rst"] += 1
        if flags_val & 0x08: f["psh"] += 1
    except:
        pass

    result = {
        "src_ip": flow_dict.get("src_ip"),
        "dst_ip": flow_dict.get("dst_ip"),
        "src_port": flow_dict.get("src_port"),
        "dst_port": flow_dict.get("dst_port"),
        "protocol": flow_dict.get("protocol"),
        "Flow Duration": duration,
        "Total Fwd Packets": f["packet_count"],
        "Total Backward Packets": 0,
        "Flow Bytes/s": f["byte_count"] / (duration + 0.001),
        "Flow Packets/s": f["packet_count"] / (duration + 0.001),
        "Packet Length Mean": np.mean(f["packet_sizes"]),
        "Packet Length Std": np.std(f["packet_sizes"]),
        "Min Packet Length": np.min(f["packet_sizes"]),
        "Max Packet Length": np.max(f["packet_sizes"]),
        "Average Packet Size": np.mean(f["packet_sizes"]),
        "Flow IAT Mean": np.mean(f["iat"]),
        "Flow IAT Std": np.std(f["iat"]),
        "Flow IAT Max": np.max(f["iat"]),
        "Flow IAT Min": np.min(f["iat"]),
        "SYN Flag Count": f["syn"],
        "ACK Flag Count": f["ack"],
        "FIN Flag Count": f["fin"],
        "RST Flag Count": f["rst"],
        "PSH Flag Count": f["psh"]
    }
    return result
