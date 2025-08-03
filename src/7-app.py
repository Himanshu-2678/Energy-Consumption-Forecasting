import gradio as gr
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import os
import warnings

warnings.filterwarnings("ignore")

# Loading the trained XGBoost model
model = joblib.load(r'C:\Users\himan\Desktop\Projects\Energy_Forecasting_System\outputs\xgb_model.pkl')

# Loading cleaned data
df = pd.read_parquet(r'C:\Users\himan\Desktop\Projects\Energy_Forecasting_System\data\processed-data\est_hourly_cleaned_with_features.parquet')

# Calculating the average energy consumption per year
yearly_avg = df.groupby('year')['PJME_MW'].mean()

# Function to plot average energy consumption per year
def plot_avg_energy_per_year():
    plt.figure(figsize=(10, 6))
    yearly_avg.plot(kind='bar', color='tab:blue')
    plt.title('Average Energy Consumption Per Year')
    plt.xlabel('Year')
    plt.ylabel('Average Energy Consumption (MW)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    # Save the figure to return
    return plt

# Defining the prediction function
def predict_energy(region, hour, dayofweek, quarter, month, year,
                   dayofyear, dayofmonth, weekofyear, is_holiday):

    PJME_MW = 0  

    if region == "PJME":
        PJME_MW = 1000  # Placeholder value based on the region
    
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

    # Plotting the forecast 
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    ax1.plot(hours, forecast, marker='o', color='tab:blue')
    ax1.set_title(f"24-Hour Forecast: {region}")
    ax1.set_xlabel("Hour")
    ax1.set_ylabel("Energy (MW)")
    ax1.grid(True)

    # Plotting the yearly average energy consumption (this stays static unless data changes)
    fig2 = plot_avg_energy_per_year()

    return round(prediction, 2), fig1, fig2  

inputs = [
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
    outputs=[gr.Number(), gr.Plot(), gr.Plot()],  
    title="⚡ Energy Consumption Forecasting System",
    description="Energy consumption forecasting for the PJM Interconnection system using XGBoost.",
    theme="huggingface",  
    live=True,  
    allow_flagging="never",  
)

# Launch the interface
iface.launch(share=True, server_name="127.0.0.1", server_port=7860)
