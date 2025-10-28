import plotly.express as px

def plot_efficiency_trend(df):
    fig = px.line(df, x="Date", y="Efficiency", color="Machine_ID", title="Machine Efficiency Over Time")
    return fig

def plot_downtime(df):
    fig = px.bar(df, x="Machine_ID", y="Downtime_Hours", color="Shift", title="Downtime Comparison by Machine")
    return fig

def plot_temperature_vibration(df):
    fig = px.scatter(df, x="Temperature", y="Vibration", color="Fault_Label",
                     title="Temperature vs Vibration by Fault Status")
    return fig
