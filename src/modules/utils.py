import os
import joblib

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def save_model(model, path):
    ensure_dir(os.path.dirname(path))
    joblib.dump(model, path)
    print(f"💾 Model saved at: {path}")
