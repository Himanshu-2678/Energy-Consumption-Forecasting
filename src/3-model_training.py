## model training 
from xgboost import XGBRegressor
import joblib

def train_model(X_train, y_train):
    model = XGBRegressor()
    model.fit(X_train, y_train)
    return model


## saving the model
def save_model(model, model_name):
    joblib.dump(model, f'C:\Users\himan\Desktop\Projects\Energy_Forecasting_System\outputs\{model_name}1.pkl')
    print(f"Model saved to \outputs\{model_name}1.pkl")