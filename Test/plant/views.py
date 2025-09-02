# FileName: MultipleFiles/views.py
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from PIL import Image # Import Pillow for image processing

from .ml_model import evaluate_plant_ml # Import the existing ML function

# --- Simulated Image Analysis Function ---
def analyze_plant_image(image_path):
    """
    This function simulates image analysis. In a real project, you would
    load a deep learning model (e.g., TensorFlow/Keras, PyTorch) here
    to classify the plant's health from the image.

    For demonstration:
    - It opens the image using Pillow.
    - It checks the image dimensions or filename to simulate a prediction.
    - Returns a label, score, and advice based on the simulated analysis.
    """
    try:
        img = Image.open(image_path)
        # You might resize the image for your model here
        # img = img.resize((224, 224)) # Example resize

        # --- SIMULATED PREDICTION LOGIC ---
        # Replace this with your actual ML model inference
        # For example, if you had a model:
        # from tensorflow.keras.models import load_model
        # model = load_model('path/to/your/image_model.h5')
        # processed_img_array = preprocess_image_for_model(img)
        # prediction = model.predict(processed_img_array)
        # label, score, advice = interpret_prediction(prediction)

        # Simple simulation based on image properties or name
        width, height = img.size
        filename = os.path.basename(image_path).lower()

        if "sick" in filename or (width < 300 and height < 300): # Example condition
            return "Sick 🤒 (Image Analysis)", 15, [
                "Image analysis suggests severe issues.",
                "Leaves appear discolored or withered.",
                "Consider checking for pests or fungal infections."
            ]
        elif "healthy" in filename or (width > 800 and height > 600): # Example condition
            return "Thriving 🌱 (Image Analysis)", 98, [
                "Image analysis confirms a very healthy plant!",
                "Vibrant color and robust growth observed.",
                "Keep up the excellent care!"
            ]
        elif "weak" in filename or (width > 300 and width < 800): # Example condition
             return "Weak 🌿 (Image Analysis)", 45, [
                "Image analysis suggests the plant is weak.",
                "Some yellowing or drooping leaves detected.",
                "Review watering and light conditions."
            ]
        else:
            # If image analysis is inconclusive, return None to fall back to form data
            return None, None, None

    except Exception as e:
        print(f"Error during image analysis simulation: {e}")
        return None, None, None # Indicate failure to analyze image

def plant_form(request):
    uploaded_image_url = None
    label = "No Data"
    score = 0
    advice = ["Please provide input to check plant health."]

    if request.method == "POST":
        # Handle form data
        answers = {
            "sunlight": request.POST.get("sunlight"),
            "watering": request.POST.get("watering"),
            "leaf_color": request.POST.get("leaf_color"),
            "soil_moisture": request.POST.get("soil_moisture"),
            "growth": request.POST.get("growth"),
            "pests": request.POST.get("pests"),
        }

        # Flag to check if form data was actually provided
        form_data_provided = any(value for value in answers.values())

        image_analysis_performed = False
        image_label, image_score, image_advice = None, None, None

        # Handle image upload
        if 'plant_image' in request.FILES:
            uploaded_file = request.FILES['plant_image']
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            uploaded_image_url = fs.url(filename) # Get the URL for the saved image
            image_path = os.path.join(settings.MEDIA_ROOT, filename) # Full path to the saved image

            # Attempt to analyze the image
            image_label, image_score, image_advice = analyze_plant_image(image_path)
            if image_label: # If image analysis returned a valid result
                image_analysis_performed = True

        # Determine the final result based on image analysis and form data
        if image_analysis_performed:
            label = image_label
            score = image_score
            advice = image_advice
            if form_data_provided:
                advice.append("Note: Image analysis was prioritized over form data.")
        elif form_data_provided:
            # Fallback to form-based ML if image analysis is inconclusive or not performed
            label, score, advice = evaluate_plant_ml(answers)
            if uploaded_image_url: # Add a note if an image was uploaded but not analyzed
                advice.append("Note: Image uploaded but could not be analyzed or analysis was inconclusive. Result based on form data.")
        else:
            # No image and no form data
            label = "No Input Provided"
            score = 0
            advice = ["Please provide plant details or upload an image to check health."]


        return render(request, "result.html", {
            "label": label,
            "score": score,
            "advice": advice,
            "uploaded_image_url": uploaded_image_url # Pass the image URL to the template
        })

    return render(request, "form.html")

def plant_result(request):
    # This view is now less critical as plant_form handles the POST and renders result.
    # Redirect to the form if result is accessed directly without POST data.
    return redirect('plant_form')
