
# AI-Based Network Intrusion Detection System

This project uses Machine Learning to detect real-time network intrusions by analyzing traffic patterns. It focuses on three common types of attacks:

- **Port Scanning**
- **DHCP Starvation**
- **IoT Botnet Scanning**

---

## 📁 Project Structure

```

ai\_network\_intrusion\_detection/
├── dataset/              # Contains sample.pcap and extracted CSV data
├── model/                # Trained ML model stored as rf\_model.pkl
├── src/                  # All Python scripts (feature extractor, trainer, live detector)
├── requirements.txt      # Python library dependencies
├── README.md             # GitHub project info (this file)
└── project\_description.txt # Detailed project explanation and theory

````

---

## ⚙️ Technologies Used

- Python 3
- Scikit-learn
- Scapy
- Pandas
- Joblib

---

## 🚀 How to Run

1. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

2. **Extract Features from `.pcap` File**

    ```bash
    python src/feature_extractor.py
    ```

3. **Train the Model**

    ```bash
    python src/train_model.py
    ```

4. **Run Live Detection**

    ```bash
    sudo python src/live_detector.py
    ```

> Ensure that your dataset contains labeled `.csv` and that a sample `.pcap` file is available for testing.

---

## 👨‍💻 Team NeuroNets


---

## 📌 Note

This project is created for educational and demonstration purposes under Intel® Unnati Industrial Training Program 2025. The attack simulations and datasets are minimal and designed for proof-of-concept.

```

