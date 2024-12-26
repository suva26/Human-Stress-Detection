import pickle
import numpy as np

def predict(data):
    model = pickle.load(open('models/stress_model.pkl', 'rb'))
    data = np.array(data).reshape(1, -1)
    prediction = model.predict(data)[0]
    
    stress_levels = {
        0: "The person is stress free and calm 😄",
        1: "The person has low stress level 🙂",
        2: "The person has medium stress level 😐",
        3: "The person has high stress level! 😞",
        4: "The person has very high stress level!! 😫"
    }
    
    return stress_levels.get(prediction, "Unknown stress level")
