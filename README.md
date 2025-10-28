
# 🏭 Faisalabad Textile Industry Data Analytics & Machine Monitoring System

A complete **AI-powered data analytics solution** built to optimize operations for textile mills in Faisalabad.  
This project integrates **data cleaning, machine monitoring, defect prediction, and real-time visualization** to assist data-driven decision-making.

---

## 🚀 Overview

The **SmartMill Analytics** platform enables mill managers and analysts to:

- Monitor machine performance in real-time
- Detect quality defects using Random Forest AI models
- Visualize production KPIs and patterns across shifts and machines
- Make data-backed decisions for **maintenance, efficiency, and quality improvement**

---

## 🧠 Key Features

- **Data Cleaning Pipeline:** Processes raw sensor and fabric data.
- **Feature Engineering:** Extracts important metrics from production logs.
- **Model Training (Random Forest):** Predicts defect types with high accuracy.
- **Evaluation Notebook:** Generates confusion matrix, reports, and metrics.
- **Streamlit Dashboard:** Interactive visualization for managers and analysts.

---

## 📂 Project Structure



SmartMill_Analytics/
│
├── data/
│ ├── raw/
│ ├── processed/
│
├── models/
│ └── Random_Forest_best.pkl
│
├── notebooks/
│ ├── 01_data_cleaning.ipynb
│ ├── 02_feature_extraction.ipynb
│ ├── 03_model_training.ipynb
│ ├── 04_model_evaluation.ipynb
│ ├── 05_model_deployment.ipynb
│
├── app/
│ └── streamlit_app.py
│
├── reports/
│ ├── model_evaluation_report.csv
│ └── inference_results.csv
│
├── src/
│ ├── data/
│ ├── models/
│ ├── visualization/
│
├── README.md
└── requirements.txt


---

## 📸 Dashboard Preview

| Fabric Defect Distribution | Machine Efficiency |
|----------------------------|--------------------|
| ![defect_chart](https://placehold.co/600x400) | ![machine_efficiency](https://placehold.co/600x400) |

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/SmartMill_Analytics.git
cd SmartMill_Analytics

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Dashboard
streamlit run app/streamlit_app.py


The dashboard will open in your browser at:
👉 http://localhost:8501

💼 Business Value for Textile Mills

Reduce Defect Rates: AI detects defective batches early.

Boost Efficiency: Continuous monitoring of machine performance.

Predictive Maintenance: Identify underperforming machines before breakdown.

Cost Optimization: Data-driven insights help reduce wastage and downtime.

👨‍💻 Developed By

Name: Alizar Ali
Role: Data Analyst / Data Scientist (Textile Industry Applications)
Location: Faisalabad, Pakistan
Tools Used: Python, Pandas, Scikit-learn, Streamlit, Plotly, Power BI


