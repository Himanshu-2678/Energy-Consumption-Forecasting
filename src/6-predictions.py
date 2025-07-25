## making predictions using the trained model

import joblib
import pandas as pd

def load_and_predict(model_name, X_test):
    # Load the model
    model_path = f'C:\\Users\\himan\\Desktop\\Projects\\Energy_Forecasting_System\\outputs\\{model_name}1.pkl'
    model = joblib.load(model_path)
    
    # Make predictions
    predictions = model.predict(X_test)
    
    return predictions