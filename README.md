
```markdown
# 🧵 SmartMill Analytics – Textile Production Monitoring Dashboard

## 📘 Project Overview
**SmartMill Analytics** is a data-driven **Streamlit dashboard** powered by **Snowflake** for advanced textile production monitoring and analytics.  
It helps factory managers and decision-makers track real-time metrics like yarn production, machine efficiency, wastage rates, and cost optimization.

This project demonstrates the use of **data warehousing (Snowflake)**, **data visualization (Streamlit)**, and **machine learning (Scikit-Learn)** to enable actionable insights in textile manufacturing.

---

## 🎯 Objectives
- Centralize production and operational data from multiple sources.
- Provide real-time visual KPIs for better decision-making.
- Automate analytics workflows for textile mill efficiency.
- Apply machine learning for predicting production performance.

---

## 🧠 Tech Stack

| Category | Technology Used |
|-----------|----------------|
| **Frontend / Visualization** | Streamlit |
| **Database & Cloud Data Warehouse** | Snowflake |
| **Data Analysis / ML** | Python, Pandas, Scikit-Learn, Joblib |
| **Visualization Libraries** | Plotly, Matplotlib |
| **Environment Management** | Conda (`environment.yml`) |
| **Automation / CI-CD** | GitHub Actions |

---

## 🏗️ Architecture Diagram

```

```
      ┌────────────────────┐
      │    Data Sources    │
      │ (Excel / CSV / DB) │
      └─────────┬──────────┘
                │
                ▼
      ┌────────────────────┐
      │     Snowflake DB   │
      │   (SMARTMILL_DB)   │
      └─────────┬──────────┘
                │
                ▼
      ┌────────────────────┐
      │  Python + Streamlit│
      │  (Data Fetch + Viz)│
      └─────────┬──────────┘
                │
                ▼
      ┌────────────────────┐
      │   User Dashboard   │
      └────────────────────┘
```

```

---

## 📁 Project Structure

```

SmartMill_Analytics/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   └── Random_Forest_best.pkl
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_feature_extraction.ipynb
│   ├── 03_model_training.ipynb
│   ├── 04_model_evaluation.ipynb
│   └── 05_model_deployment.ipynb
│
├── reports/
│   ├── model_evaluation_report.csv
│   └── inference_results.csv
│
├── src/
│   ├── data/
│   ├── models/
│   └── visualization/
│
├── requirements.txt
└── README.md

````

---

## 🖼️ Dashboard Preview

### 🧩 App Interface  
![App UI](app.png)

### 📊 Production Dashboard  
![Dashboard](app1.png)

### 💻 Backend Code (Snowflake + Streamlit Integration)  
![Backend Code](backend.png)

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/AlizarKhan62/smartmill-textile-analytics-dashboard
cd SmartMill_Analytics
````

### 2️⃣ Create a Virtual Environment

```bash
conda create -n smartmill python=3.9
conda activate smartmill
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Connect to Snowflake

#### a. Create a `.streamlit/secrets.toml` file

This file securely stores your Snowflake credentials.

```toml
[snowflake]
user = "YOUR_SNOWFLAKE_USERNAME"
password = "YOUR_SNOWFLAKE_PASSWORD"
account = "YOUR_SNOWFLAKE_ACCOUNT"  # e.g., abcd1234.ap-southeast-1
warehouse = "SMARTMILL_WH"
database = "SMARTMILL_DB"
schema = "PUBLIC"
role = "ACCOUNTADMIN"
```

> 📝 **Tip:**
> Make sure you’ve created your Snowflake account and a database named `SMARTMILL_DB` in the Singapore region (ap-southeast-1).

#### b. Verify Connection

Test your connection before running the app:

```python
import snowflake.connector

conn = snowflake.connector.connect(
    user="YOUR_SNOWFLAKE_USERNAME",
    password="YOUR_SNOWFLAKE_PASSWORD",
    account="YOUR_SNOWFLAKE_ACCOUNT"
)

cs = conn.cursor()
cs.execute("SELECT CURRENT_VERSION();")
print(cs.fetchone())
```

If you see a version number — ✅ your connection works!

---

### 5️⃣ Run the Streamlit App

```bash
streamlit run app/streamlit_app.py
```

Then open the dashboard in your browser at:
👉 [http://localhost:8501](http://localhost:8501)

---

## 💼 Business Value for Textile Mills

✅ **Reduce Defect Rates:** AI detects defective batches early.
✅ **Boost Efficiency:** Continuous monitoring of machine performance.
✅ **Predictive Maintenance:** Identify underperforming machines before breakdown.
✅ **Cost Optimization:** Data-driven insights reduce wastage and downtime.

---

## 🧾 Example KPIs Displayed on Dashboard

| KPI                          | Description                          |
| ---------------------------- | ------------------------------------ |
| **Yarn Output (tons)**       | Total yarn produced per shift/day    |
| **Machine Efficiency (%)**   | Real-time utilization rate           |
| **Defect Rate (%)**          | Percentage of defective production   |
| **Energy Consumption (kWh)** | Power usage for cost monitoring      |
| **Production Cost (PKR)**    | Aggregated from materials and energy |

---

## 📦 Example Snowflake Query

```sql
SELECT
    MACHINE_ID,
    SHIFT,
    AVG(PRODUCTION_TONS) AS AVG_PRODUCTION,
    AVG(EFFICIENCY) AS AVG_EFFICIENCY,
    AVG(DEFECT_RATE) AS AVG_DEFECT
FROM SMARTMILL_DB.PUBLIC.MACHINE_PERFORMANCE
GROUP BY MACHINE_ID, SHIFT
ORDER BY AVG_EFFICIENCY DESC;
```

---

## 📌 Key Takeaways

* Integrates **Snowflake** for scalable data warehousing.
* Implements **machine learning** for production trend prediction.
* Built with **Streamlit** for real-time web analytics dashboards.
* Designed for **textile manufacturing intelligence** and **data-driven decision-making**.

