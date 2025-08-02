import gradio as gr
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the trained RandomForest model 
model = joblib.load(os.path.join("outputs", "random_forest_model.pkl"))

# Define prediction function
def predict_energy(region, hour, dayofweek, quarter, month, year,
                   dayofyear, dayofmonth, weekofyear, is_holiday):

    # Prepare the input data as a pandas DataFrame
    input_df = pd.DataFrame({
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

    # Make the prediction
    prediction = model.predict(input_df)[0]

    # Forecast for the next 24 hours
    hours = list(range(24))
    forecast_input = pd.DataFrame({
        "hour": hours,
        "dayofweek": [dayofweek]*24,
        "quarter": [quarter]*24,
        "month": [month]*24,
        "year": [year]*24,
        "dayofyear": [dayofyear]*24,
        "dayofmonth": [dayofmonth]*24,
        "weekofyear": [weekofyear]*24,
        "is_holiday": [1 if is_holiday else 0]*24
    })

    forecast = model.predict(forecast_input)

    # Plot forecast for the next 24 hours
    fig, ax = plt.subplots()
    ax.plot(hours, forecast, marker='o')
    ax.set_title(f"24-Hour Forecast: {region}")
    ax.set_xlabel("Hour")
    ax.set_ylabel("Energy (MW)")
    ax.grid(True)

    return round(prediction, 2), fig

# Define the UI components
inputs = [
    gr.Radio(["PJME", "PJMW"], label="Region"),
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

# Set up the Gradio interface
iface = gr.Interface(
    fn=predict_energy,
    inputs=inputs,
    outputs=["number", "plot"],
    title="⚡ Energy Forecasting System",
    description="Forecasts hourly energy consumption using Random Forest. Trained on hourly data from PJME and PJMW."
)

# Launch the interface
iface.launch()
