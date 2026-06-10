from nfstream import NFStreamer

def packet_stream(interface):
    streamer = NFStreamer(source=interface, promiscuous_mode=True)

    features = [
        "id", "expiration_id", "src_ip", "src_mac", "src_oui", "src_port",
        "dst_ip", "dst_mac", "dst_oui", "dst_port", "protocol", "ip_version",
        "bidirectional_first_seen_ms", "bidirectional_last_seen_ms",
        "bidirectional_duration_ms", "bidirectional_packets", "bidirectional_bytes",
        "src2dst_first_seen_ms", "src2dst_last_seen_ms",
        "src2dst_duration_ms", "src2dst_packets", "src2dst_bytes",
        "dst2src_first_seen_ms", "dst2src_last_seen_ms",
        "dst2src_duration_ms", "dst2src_packets", "dst2src_bytes",
        "application_name", "application_category_name"
    ]

    for flow in streamer:
        flow_dict = {feat: getattr(flow, feat, None) for feat in features}
        yield flow_dict
