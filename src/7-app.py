import gradio as gr
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import os
import warnings
warnings.filterwarnings("ignore")

# Loading the trained XGBoost model
model = joblib.load(os.path.join("outputs", "xgb_model.pkl"))

# Defining the prediction function
def predict_energy(region, hour, dayofweek, quarter, month, year,
                   dayofyear, dayofmonth, weekofyear, is_holiday):

    PJME_MW = 0  
    
    if region == "PJME":
        PJME_MW = 1000 
    
    # input data
    input_df = pd.DataFrame({
        "PJME_MW": [PJME_MW],  
        "hour": [hour],
        "dayofweek": [dayofweek],
        "quarter": [quarter],
        "month": [month],
        "year": [year],
        "dayofyear": [dayofyear],
        "dayofmonth": [dayofmonth],
        "weekofyear": [weekofyear],
        "is_holiday": [1 if is_holiday else 0]
    })
    
    # making the prediction
    prediction = model.predict(input_df)[0]

    # Forecasting for next 24 hours (using the same features for forecasting)
    hours = list(range(24))
    forecast_input = pd.DataFrame({
        "PJME_MW": [PJME_MW] * 24, 
        "hour": hours,
        "dayofweek": [dayofweek] * 24,
        "quarter": [quarter] * 24,
        "month": [month] * 24,
        "year": [year] * 24,
        "dayofyear": [dayofyear] * 24,
        "dayofmonth": [dayofmonth] * 24,
        "weekofyear": [weekofyear] * 24,
        "is_holiday": [1 if is_holiday else 0] * 24
    })
    
    forecast = model.predict(forecast_input)

    # Ploting the forecast
    fig, ax = plt.subplots()
    ax.plot(hours, forecast, marker='o')
    ax.set_title(f"24-Hour Forecast: {region}")
    ax.set_xlabel("Hour")
    ax.set_ylabel("Energy (MW)")
    ax.grid(True)

    return round(prediction, 2), fig

inputs = [
    #gr.Radio(["PJME"], label="Region"),
    gr.Slider(0, 23, step=1, label="Hour"),
    gr.Slider(0, 6, step=1, label="Day of Week (0=Mon)"),
    gr.Slider(1, 4, step=1, label="Quarter"),
    gr.Slider(1, 12, step=1, label="Month"),
    gr.Slider(2015, 2025, step=1, label="Year"),
    gr.Slider(1, 366, step=1, label="Day of Year"),
    gr.Slider(1, 31, step=1, label="Day of Month"),
    gr.Slider(1, 52, step=1, label="Week of Year"),
    gr.Checkbox(label="Is Holiday")
]


iface = gr.Interface(
    fn=predict_energy,
    inputs=inputs,
    outputs=["number", "plot"],
    title="⚡ Energy Consumption Forecasting System",
    description="Here we are going to see the Energy Consumption Forecasting for specific regions within the PJM Interconnection (PJM) system. PJM Interconnection is a regional transmission organization (RTO) in the United States that coordinates the movement of wholesale electricity and ensures grid reliability.",
    theme="huggingface",     
    live=True,            
    allow_flagging="never")

iface.launch()