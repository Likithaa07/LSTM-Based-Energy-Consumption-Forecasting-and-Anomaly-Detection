import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title & description
st.title("Energy Consumption Forecasting and Anomaly Detection")
st.write("""
Interactive dashboard showcasing historical hourly energy usage, 
LSTM-based forecasts, and detected anomalies.

Enables visual comparison of actual vs. predicted demand patterns 
and highlights unusual consumption events for timely insights.
""")

# Example: load prepared visualization data (replace with actual vis_df DataFrame)
# Expecting columns: Datetime, Actual, Predicted, Anomaly
import pickle
with open("vis_df.pkl", "rb") as f:
    vis_df = pickle.load(f)

# Slider to choose number of points
num_points = st.slider("Select number of data points", 100, len(vis_df), 500)
plot_data = vis_df.head(num_points)

# Plot data
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(plot_data['Datetime'], plot_data['Actual'], label='Actual')
ax.plot(plot_data['Datetime'], plot_data['Predicted'], label='Predicted')
anomaly_points = plot_data[plot_data['Anomaly']]
ax.scatter(anomaly_points['Datetime'], anomaly_points['Actual'], color='red', label='Anomalies', marker='x')

ax.set_xlabel("Datetime")
ax.set_ylabel("Normalized Energy Consumption")
ax.set_title("Energy Consumption Forecast vs Actual with Anomalies")
ax.legend()
plt.xticks(rotation=45)
st.pyplot(fig)
