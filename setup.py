from setuptools import setup, find_packages

setup(
    name="faisalabad_textile_analytics",
    version="1.0.0",
    description="Data Analytics and Machine Monitoring System for Faisalabad Textile Industry",
    author="Alizar Ali",
    packages=find_packages(),
    install_requires=[
        "pandas", "numpy", "scikit-learn", "plotly", "streamlit", "joblib", "matplotlib", "seaborn"
    ],
)
