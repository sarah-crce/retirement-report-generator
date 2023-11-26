import numpy as np
import pickle


def inflation_predict(year):
    model_filename = 'inflation_model/inflation_prediction_model.pkl'
    with open(model_filename, 'rb') as model_file:
        loaded_model = pickle.load(model_file)


    prediction_input = np.array([[year]])

    predicted_inflation_rate = loaded_model.predict(prediction_input)[0]

    return predicted_inflation_rate
