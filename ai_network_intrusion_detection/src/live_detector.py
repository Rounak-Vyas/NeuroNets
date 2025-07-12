from scapy.all import sniff, IP, TCP, UDP, DHCP
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

MODEL_PATH = "../model/rf_model.pkl"

# Load trained model
model = joblib.load(MODEL_PATH)

def extract_features_from_packet(pkt):
    src_port = dst_port = proto = packet_len = is_dhcp = 0

    if IP in pkt:
        proto = pkt[IP].proto
        packet_len = len(pkt)
        if TCP in pkt:
            src_port = pkt[TCP].sport
            dst_port = pkt[TCP].dport
        elif UDP in pkt:
            src_port = pkt[UDP].sport
            dst_port = pkt[UDP].dport
            if DHCP in pkt:
                is_dhcp = 1

    return [[src_port, dst_port, proto, packet_len, is_dhcp]]

def detect_attack(pkt):
    try:
        features = extract_features_from_packet(pkt)
        prediction = model.predict(features)[0]

        if prediction == 1:
            print("[ALERT] Port Scanning Detected!")
        elif prediction == 2:
            print("[ALERT] DHCP Starvation Attack Detected!")
        elif prediction == 3:
            print("[ALERT] IoT Botnet Scanning Detected!")
    except Exception:
        pass

if __name__ == "__main__":
    print("Monitoring live traffic... Press Ctrl+C to stop.")
    sniff(prn=detect_attack, store=0)
