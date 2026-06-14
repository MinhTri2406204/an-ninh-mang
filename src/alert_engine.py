from datetime import datetime
def send_alert(label, confidence, flow):
    if confidence>.80:
        print()
        print("="*50)
        print("[WARNING]")
        print(datetime.now())
        print(label)
        print(confidence)
        print(flow["src_ip"])
        print(flow["dst_ip"])
        print("="*50)
