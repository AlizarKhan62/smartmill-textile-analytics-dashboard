# app/streamlit_app.py

import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
import os

# --- Page Config ---
st.set_page_config(page_title="SmartMill Analytics Dashboard", layout="wide")

# --- Title and Description ---
st.title("🏭 SmartMill Analytics Dashboard")
st.markdown("""
This interactive dashboard visualizes **textile production**, **machine performance**, 
and **defect prediction** using AI-powered analytics.
""")

# --- Load Processed Data ---
data_path = "data/processed/features.csv"
if os.path.exists(data_path):
    df = pd.read_csv(data_path)
else:
    st.error("⚠️ Processed data not found! Please run the data pipeline first.")
    st.stop()

# --- KPIs Section ---
st.subheader("📊 Key Performance Indicators (KPIs)")
col1, col2, col3 = st.columns(3)

col1.metric("Total Fabric Samples", len(df))
col2.metric("Defective Samples", int(df['defect_flag'].sum()) if 'defect_flag' in df else 0)
col3.metric("Avg Machine Efficiency (%)", round(df['efficiency'].mean(), 2) if 'efficiency' in df else 0)

# --- Fabric Quality Overview ---
st.subheader("🧵 Fabric Quality Overview")
if 'defect_type' in df.columns:
    fig1 = px.histogram(df, x='defect_type', color='defect_type', title="Fabric Defect Distribution", text_auto=True)
    st.plotly_chart(fig1, use_container_width=True)

# --- Machine Performance Visualization ---
if 'machine_id' in df.columns and 'efficiency' in df.columns:
    st.subheader("⚙️ Machine Efficiency Trend")
    fig2 = px.box(df, x='machine_id', y='efficiency', color='machine_id', title="Machine Efficiency Variation")
    st.plotly_chart(fig2, use_container_width=True)

# --- Load Trained Model ---
model_path = "models/Random_Forest_best.pkl"
if os.path.exists(model_path):
    model = joblib.load(model_path)
    st.subheader("🔮 Predict Fabric Defects")

    # Define feature names manually if not available
    try:
        model_features = list(model.feature_names_in_)
    except AttributeError:
        model_features = [
            'mean_R', 'mean_G', 'mean_B',
            'std_R', 'std_G', 'std_B',
            'contrast', 'smoothness', 'entropy', 'edge_density'
        ]

    with st.expander("Upload sample feature data for prediction"):
        uploaded_file = st.file_uploader("Upload CSV file for prediction", type=["csv"])

        if uploaded_file:
            input_df = pd.read_csv(uploaded_file)
            st.write("✅ File uploaded successfully!")

            # --- Clean and Match Features ---
            if 'defect_code' in input_df.columns:
                input_df = input_df.drop('defect_code', axis=1)

            missing_cols = [col for col in model_features if col not in input_df.columns]
            extra_cols = [col for col in input_df.columns if col not in model_features]

            if missing_cols:
                st.error(f"❌ Missing required features: {missing_cols}")
            else:
                input_df = input_df[model_features]

                # --- Predict ---
                preds = model.predict(input_df)
                pred_df = pd.DataFrame(preds, columns=["Predicted Defect"])
                st.success("✅ Prediction complete!")
                st.dataframe(pred_df)

                # --- Download Predictions ---
                csv_data = pred_df.to_csv(index=False).encode('utf-8')
                st.download_button("📥 Download Predictions", csv_data, "predictions.csv", "text/csv")
else:
    st.warning("⚠️ Model not found. Please train the model first.")

# --- Correlation Heatmap ---
if 'efficiency' in df.columns:
    st.subheader("📈 Correlation Analysis")
    fig3 = px.imshow(df.corr(), text_auto=True, color_continuous_scale="Blues", title="Feature Correlation Heatmap")
    st.plotly_chart(fig3, use_container_width=True)

# --- Footer ---
st.markdown("---")
st.markdown("✅ **Developed by:** Data Analyst | Faisalabad Textile Analytics Project")
st.markdown("💡 **Goal:** Improve production efficiency, predict defects early, and optimize resource usage.")
