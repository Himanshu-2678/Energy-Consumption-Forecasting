# Energy Consumption Forecasting 

## Overview

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

## Project Structure
Energy_Forecasting_System/
│
├── data/ ← Raw and cleaned CSV data files
│ ├── raw_data.csv ← Raw energy consumption data (PJM)
│ ├── cleaned_data.csv ← Cleaned and preprocessed data for training
│
├── notebooks/ ← Jupyter Notebooks for experimentation and EDA
│ ├── 1-data_cleaning.ipynb ← Data cleaning and preprocessing
│ ├── 2-data_visualizations.ipynb ← Exploratory data analysis (EDA) and visualizations
│ ├── 3-feature_engineering.ipynb ← Feature engineering process
│ ├── 4-model_building.ipynb ← Model building and evaluation
│
├── src/ ← Source code for data processing, model training, and evaluation
│ ├── preprocessing.py ← Data cleaning and feature engineering functions
│ ├── model_train.py ← Model training, hyperparameter tuning, and saving the model
│ ├── evaluate.py ← Metrics, plots, and model evaluation
│ ├── data_preprocessing.py ← Helper functions for data preprocessing
│ ├── model_evaluation.py ← Functions to evaluate model performance and generate plots
│ ├── feature_engineering.py ← Feature extraction and transformation
│ ├── model_training.py ← Model training pipeline and hyperparameter tuning
│ ├── model_utils.py ← Helper functions for model management
│ ├── predictions.py ← Predictive pipeline and output generation
│
├── models/ ← Saved models (e.g., XGBoost model)
│ └── xgb_model.pkl ← Trained XGBoost model
│
├── outputs/ ← Output files such as predictions and forecasts
│ └── predictions.csv ← Forecasted values for future energy consumption
│
├── main.py ← Main driver script to start the application and deploy the model
├── requirements.txt ← List of dependencies
└── README.md ← Project documentation (this file)



