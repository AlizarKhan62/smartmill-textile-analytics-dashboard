import pandas as pd
import joblib

def predict_fault(input_data, model_path="../models/Random_Forest_best.pkl"):
    """
    Predict if a machine/fabric has a fault based on input parameters.
    """
    model = joblib.load(model_path)
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    proba = model.predict_proba(df).max()
    return prediction, round(proba, 2)
