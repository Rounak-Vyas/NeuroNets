import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

def train_model(csv_path, model_output_path):
    df = pd.read_csv(csv_path)

    X = df[['src_port', 'dst_port', 'protocol', 'packet_length', 'is_dhcp']]
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    joblib.dump(clf, model_output_path)
    print(f"Model saved at {model_output_path}")

if __name__ == "__main__":
    csv_path = "../dataset/traffic_features.csv"
    model_path = "../model/rf_model.pkl"

    if os.path.exists(csv_path):
        train_model(csv_path, model_path)
    else:
        print("CSV file not found. Please run feature extractor first.")
