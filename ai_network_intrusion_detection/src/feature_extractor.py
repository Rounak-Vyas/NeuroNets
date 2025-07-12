from scapy.all import rdpcap, TCP, UDP, DHCP, IP
import pandas as pd
import os

def extract_features(pcap_file):
    packets = rdpcap(pcap_file)
    data = []

    for pkt in packets:
        if IP in pkt:
            src_ip = pkt[IP].src
            dst_ip = pkt[IP].dst
            proto = pkt[IP].proto
            packet_len = len(pkt)
            flags = ''
            sport = dport = 0
            is_dhcp = 0

            if TCP in pkt:
                sport = pkt[TCP].sport
                dport = pkt[TCP].dport
                flags = str(pkt[TCP].flags)
            elif UDP in pkt:
                sport = pkt[UDP].sport
                dport = pkt[UDP].dport
                if DHCP in pkt:
                    is_dhcp = 1

            data.append({
                "src_ip": src_ip,
                "dst_ip": dst_ip,
                "src_port": sport,
                "dst_port": dport,
                "protocol": proto,
                "packet_length": packet_len,
                "tcp_flags": flags,
                "is_dhcp": is_dhcp,
                "label": 0  # Placeholder label
            })

    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    input_pcap = "../dataset/sample.pcap"
    output_csv = "../dataset/traffic_features.csv"

    if os.path.exists(input_pcap):
        df = extract_features(input_pcap)
        df.to_csv(output_csv, index=False)
        print(f"Saved to {output_csv}")
    else:
        print("sample.pcap not found.")
