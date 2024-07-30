from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model and preprocessor
model = joblib.load("animal_disease_model.pkl")
preprocessor = joblib.load("preprocessor.pkl")


@app.route("/predict", methods=["POST"])
def predict():
    # Get the JSON data from the request
    data = request.json

    # Convert the JSON data to a DataFrame
    df = pd.DataFrame(data)

    # Ensure 'Age' and 'Temperature' columns are dropped if they exist
    df_modified = df.drop(columns=["Age", "Temperature"], errors="ignore")

    # Check if 'Disease' column exists and drop it
    if "Disease" in df_modified.columns:
        df_modified = df_modified.drop(columns=["Disease"])

    # Preprocess the data
    X_new_processed = preprocessor.transform(df_modified)

    # Make predictions
    predictions = model.predict(X_new_processed)

    # Return the predictions as a JSON response
    return jsonify({"predictions": list(predictions)})


if __name__ == "__main__":
    app.run(debug=True)
