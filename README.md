- LSTM-Based Energy Consumption Forecasting & Anomaly Detection

Real-time energy consumption forecasting and anomaly detection using Multivariate LSTM on hourly power grid data from PJM Interconnection.


- What It Does


Forecasts future energy consumption using Multivariate LSTM
Detects anomalies in power usage patterns automatically
Serves predictions via a live web application (app.py)
Uses real hourly energy data from the AEP (American Electric Power) region



- Dataset

Source: PJM Interconnection — AEP Region
File: AEP_hourly.csv


Hourly energy consumption readings
Real power grid data from the US East Coast



- Model


Architecture: Multivariate LSTM (Long Short-Term Memory)
Task: Time series forecasting + anomaly detection
Saved model: energy_forecast_model.h5
Anomaly output: anomalies_data.csv



- Tech Stack

Deep Learning:   TensorFlow / Keras · LSTM
Data:            pandas · NumPy
Visualisation:   Matplotlib · Seaborn
App:             Streamlit / Flask (app.py)


- Project Structure

```
├── AEP_hourly.csv                  # Raw hourly energy dataset
├── MultivariateLSTMproject.ipynb   # Full training pipeline
├── energy_forecast_model.h5        # Saved trained LSTM model
├── anomalies_data.csv              # Detected anomalies output
├── vis_df.pkl                      # Pre-processed data for visualisation
├── app.py                          # Web application
└── README.md
```

- Future Improvements


 Add Prophet baseline for comparison
 Deploy app permanently on Streamlit Cloud
 Add real-time data ingestion via API
 Extend anomaly detection with isolation forest ensemble
