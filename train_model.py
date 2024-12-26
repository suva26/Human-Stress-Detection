import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

def train():
    # Load the dataset
    data = pd.read_csv('data/Stress.csv')
    
    # Define features (X) and target (y)
    X = data[['sr', 'rr', 't', 'lm', 'bo', 'rem', 'sh', 'hr']]
    y = data['sl']
    
    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Initialize Random Forest classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Save the trained model
    with open('models/stress_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    # Predict on the test set
    y_pred = model.predict(X_test)
    
    # Calculate accuracy score
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy on test set: {accuracy}')

# Call the train function to train the model and print accuracy
train()
