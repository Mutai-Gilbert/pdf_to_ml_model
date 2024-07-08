import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import sys

def train_model(df):
    # Split the data into features and labels
    X = df[['feature1', 'feature2']]
    y = df['label']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Random Forest classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy}')

    # Save the model
    joblib.dump(model, 'model.joblib')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python train_model.py <path_to_csv>")
        sys.exit(1)
    
    csv_path = sys.argv[1]
    df = pd.read_csv(csv_path)
    train_model(df)
