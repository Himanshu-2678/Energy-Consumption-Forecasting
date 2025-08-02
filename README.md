# Energy Consumption Forecasting 

## Overview

### Dataset link : https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption
The **Energy Forecasting System** is a machine learning application that forecasts hourly energy consumption using **XGBoost**. The model is trained on hourly energy consumption data from the **PJM Interconnection**, specifically the **PJME (East)**region. The system predicts future energy consumption based on various factors such as time of day, season, holidays, and more.

This is actually my first Machine Learning Project which i made from Scratch for upskilling my skills.

## Features

- **Energy Consumption Prediction**: Predicts hourly energy consumption for PJM East.
- **Interactive UI**: Provides a user-friendly interface for users to input parameters and view predictions along with graphical visualizations.
- **Live Forecasting**: Visualizes a 24-hour energy consumption forecast using historical data.
- **Customizable Inputs**: Allows users to adjust parameters such as region, hour, day of the week, quarter, and more.

## Tech Stack

- **Backend**: Python
- **Machine Learning Model**: XGBoost (XGBRegressor)
- **Web Interface**: Gradio
- **Libraries**:
  - `joblib` (for model serialization)
  - `pandas` (data handling)
  - `matplotlib` (for visualization)
  - `scikit-learn` (for ML model building and evaluation)
  - `xgboost` (for the model)





