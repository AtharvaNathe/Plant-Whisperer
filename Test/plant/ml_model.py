# FileName: MultipleFiles/ml_model.py
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
import joblib
import os

# --- Training the model ---
def train_plant_classifier(csv_file_path="plant_data.csv"):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, csv_file_path)

    df = pd.read_csv(data_path)

    # Remove 'score' from features if present
    feature_columns = ['sunlight', 'watering', 'leaf_color', 'soil_moisture', 'growth', 'pests']
    X = df[feature_columns]
    y = df['label']

    # One-hot encode categorical features
    encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
    X_encoded = encoder.fit_transform(X)
    feature_names = encoder.get_feature_names_out(feature_columns)
    X_encoded_df = pd.DataFrame(X_encoded, columns=feature_names)

    # Train Decision Tree Classifier
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_encoded_df, y)

    # Save model and encoder
    joblib.dump(model, os.path.join(base_dir, 'plant_classifier_model.pkl'))
    joblib.dump(encoder, os.path.join(base_dir, 'plant_encoder.pkl'))
    print("Model and encoder trained and saved successfully!")

# --- Load the trained model and encoder ---
def load_plant_classifier():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, 'plant_classifier_model.pkl')
    encoder_path = os.path.join(base_dir, 'plant_encoder.pkl')
    try:
        model = joblib.load(model_path)
        encoder = joblib.load(encoder_path)
        return model, encoder
    except FileNotFoundError:
        print("Trained model or encoder not found. Please train the model first by running ml_model.py directly.")
        return None, None

# --- Evaluate using the trained model ---
def evaluate_plant_ml(answers: dict):
    model, encoder = load_plant_classifier()
    if model is None or encoder is None:
        return "Error: ML model not loaded", 0, ["ML model not available. Please ensure the model is trained."]

    feature_columns = ['sunlight', 'watering', 'leaf_color', 'soil_moisture', 'growth', 'pests']
    input_data = {k: answers[k] for k in feature_columns if k in answers}
    input_df = pd.DataFrame([input_data])

    # Encode input features
    input_encoded = encoder.transform(input_df[feature_columns])  # Ensure order
    input_encoded_df = pd.DataFrame(input_encoded, columns=encoder.get_feature_names_out(feature_columns))

    # Predict label
    predicted_label = model.predict(input_encoded_df)[0]

    # Generate score and advice
    if predicted_label == "Thriving 🌱":
        score = 90
        advice = [
            "Your plant is doing great! Keep up the good work.",
            "Maintain the current watering and sunlight schedule.",
            "Monitor leaf color to ensure it stays healthy green.",
            "Keep the soil slightly moist but not waterlogged.",
            "Rotate the pot occasionally for even sunlight exposure.",
            "Regularly remove dead leaves to promote fresh growth."
        ]

    elif predicted_label == "Okay 🌤️":
        score = 70
        advice = [
            "Your plant is okay, but there's room for improvement.",
            "Check soil moisture to avoid over or under watering.",
            "Ensure it gets sufficient indirect sunlight daily.",
            "Wipe leaves gently to remove dust and improve photosynthesis.",
            "Add organic fertilizer once in a while for growth boost.",
            "Keep an eye on pests or small discolorations in leaves."
        ]

    elif predicted_label == "Weak 🌿":
        score = 40
        advice = [
            "Your plant is weak, it needs extra care.",
            "Check its watering routine — too much or too little can harm.",
            "Move it to a brighter spot with indirect sunlight.",
            "Consider adding a balanced liquid fertilizer.",
            "Look for signs of root rot or pest infestation.",
            "Prune weak or yellowing leaves to encourage new growth."
        ]

    elif predicted_label == "Sick 🤒":
        score = 10
        advice = [
            "Your plant is sick. Immediate action is needed!",
            "Check for overwatering or fungal infections in the soil.",
            "Inspect leaves and stems for visible pests or diseases.",
            "Isolate the plant if you have others nearby to prevent spread.",
            "Use a suitable pesticide or fungicide if pests/disease are detected.",
            "Repot with fresh, sterile soil if root rot or poor soil is suspected."
        ]

    else:
        score = 0
        advice = [
            "Unable to determine plant health.",
            "Please double-check your input values.",
            "Try capturing a clearer plant image for prediction.",
            "Make sure the model is trained with enough plant data.",
            "Consider retraining the model with more samples.",
            "Consult a gardening expert if the problem persists."
        ]

    return predicted_label, score, advice

# --- Run training if executed as main ---
if __name__ == "__main__":
    train_plant_classifier()
