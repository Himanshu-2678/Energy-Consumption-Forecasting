# Energy Forecasting System

## Overview
**Dataset Link**: [Hourly Energy Consumption Dataset](https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption)

The **Energy Forecasting System** is a machine learning application built to predict hourly energy consumption using historical data from the **PJM Interconnection**. The model is trained on hourly energy consumption data for the **PJME (East)** region. Using machine learning algorithms such as **XGBoost (XGBRegressor)**, the system predicts future energy consumption based on various factors such as time of day, season, holidays, and more.

This is my first Machine Learning project created from scratch, aimed at upskilling and gaining practical experience in data science, machine learning, and deployment.

## Features
- **Energy Consumption Prediction**: Predicts hourly energy consumption for PJM East.
- **Interactive UI**: Provides an easy-to-use interface for users to input parameters and view predictions.
- **Live Forecasting**: Visualizes a 24-hour energy consumption forecast based on historical data.
- **Customizable Inputs**: Users can adjust parameters such as region, hour, day of the week, quarter, month, and holiday status to see how different factors affect energy consumption.
- **Visual Output**: Displays predictions alongside graphical plots to help users understand energy trends.
- **Real-Time Results**: The system shows energy predictions live based on user inputs, allowing for real-time forecasting.

## Tech Stack
- **Backend**: Python
- **Machine Learning Model**: XGBoost (XGBRegressor)
- **Web Interface**: Gradio
- **Libraries**:
  - `joblib` (for model serialization)
  - `pandas` (data handling)
  - `matplotlib` (for visualization)
  - `scikit-learn` (for model building and evaluation)
  - `xgboost` (for training the model)
  - `numpy` (for numerical computations)

## Installation & Setup
To run the **Energy Forecasting System** locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Energy_Forecasting_System.git
   cd Energy_Forecasting_System
3. Run the app -> 
   ```bash
   python src/7-app.py
   
