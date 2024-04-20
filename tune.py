import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Data Preprocessing
data = pd.read_csv('your_data.csv')

# 2. Feature Engineering
# Add features as needed, for example, time differences, indicators for critical times, etc.

# 3. Training and Testing Sets
X = data[['hour', 'minute', 'Y', 'd', 'maximise']]
y = data['next_10x']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Model Selection with Hyperparameter Tuning
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 10, 20, 30]
}

model = RandomForestClassifier()
grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Print the best parameters
print("Best Parameters:", grid_search.best_params_)

# Get the best model
best_model = grid_search.best_estimator_

# 5. Model Training
best_model.fit(X_train, y_train)

# 6. Model Evaluation
predictions = best_model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f'Best Model Accuracy: {accuracy}')

# 7. Prediction
# Example input series for prediction
input_series = [
    [5, 52, 1.0, 0, 1],  # You can replace these values with your own input
    [5, 52, 1.00, 0, 1],
    [5, 52, 2.54, 1, 0]
]

# Predict the next 10x based on the input series
next_10x_prediction = best_model.predict(input_series)
print(f'Predicted next 10x: {next_10x_prediction}')
