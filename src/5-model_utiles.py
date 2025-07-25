import joblib

def save_model(model, model_name):
    joblib.dump(model, f'C:\Users\himan\Desktop\Projects\Energy_Forecasting_System\outputs\{model_name}1.pkl')
    print(f"Model saved to \outputs\{model_name}1.pkl")

def load_model(model_name):
    model_path = f'C:\Users\himan\Desktop\Projects\Energy_Forecasting_System\outputs\{model_name}1.pkl'
    model = joblib.load(model_path)
    print(f"Model loaded from \outputs\{model_name}1.pkl")
    return model
