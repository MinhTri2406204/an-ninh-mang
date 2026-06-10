#from scapy.all import sniff

#def packet_callback(packet):
#    if packet.haslayer('IP'):
#        src = packet['IP'].src
#        dst = packet['IP'].dst
#        print(f"[PACKET] {src} -> {dst}")

#print("Scapy dang truc chien tren ens33... Hay thu tan cong tu Kali!")
#sniff(iface="ens33", prn=packet_callback, store=0)


from nfstream import NFStreamer

streamer = NFStreamer(source="ens33", promiscuous_mode=True)

for flow in streamer:
    print(flow)
