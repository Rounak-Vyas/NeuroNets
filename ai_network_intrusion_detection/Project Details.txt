PROJECT: AI-Based Network Intrusion Detection

This project uses Machine Learning (Random Forest Classifier) to detect three common network attacks in real time by analyzing network traffic patterns.

Detected Attacks:
1. Port Scanning
2. DHCP Starvation
3. IoT Botnet Scanning

Folder Structure:

ai_network_intrusion_detection/
├── dataset/              ← pcap files and extracted feature CSV
├── model/                ← Trained machine learning model
├── src/                  ← All Python source code
├── README.txt            ← Instructions (this file)
├── requirements.txt      ← List of required Python packages
└── project_description.txt ← Project explanation and attack theory

How to Run:

Step 1: Extract features from .pcap file
    - Run: python src/feature_extractor.py
    - Input: sample.pcap inside dataset/
    - Output: traffic_features.csv inside dataset/

Step 2: Train the model
    - Run: python src/train_model.py
    - Output: rf_model.pkl inside model/

Step 3: Detect attacks in live traffic
    - Run: sudo python src/live_detector.py
    - This will show alerts for Port Scan / DHCP / IoT Botnet traffic

Dependencies:
Install required Python libraries using:
    pip install -r requirements.txt
      OR
    pip install scapy pandas joblib scikit-learn


Developed by:
Team NeuroNets

