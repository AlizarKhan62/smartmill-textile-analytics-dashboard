import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

def train_fault_model(df, target_col="Fault_Label", save_path="../models/Random_Forest_best.pkl"):
    """
    Train a Random Forest model to detect machine faults or fabric defects.
    """
    features = ["Temperature", "Vibration", "Speed", "Efficiency"]
    X = df[features]
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"✅ Model Accuracy: {acc:.3f}")

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    joblib.dump(model, save_path)
    print(f"💾 Model saved to: {save_path}")
