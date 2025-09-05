# 🌱 Plant Whisperer – Plant Health Prediction App  

**The project is deployed using python anywhere** Visit : https://atharva75.pythonanywhere.com

## 📌 Overview  
**Plant Whisperer** is a Django-based web application that helps users check the health of their plants using:  
- **Form Inputs** (e.g., sunlight, watering, leaf color, pests, etc.)  
- **Image Uploads** (basic simulated analysis using Pillow, extendable with deep learning)  

The app predicts whether a plant is **Thriving 🌱, Okay 🌤️, Weak 🌿, or Sick 🤒** and provides a **health score** along with **actionable care advice**.  

---

## ✨ Features  
- ✅ User-friendly form with Bootstrap-styled UI  
- ✅ Machine Learning model (Decision Tree Classifier with sklearn)  
- ✅ Categorical feature encoding using `OneHotEncoder`  
- ✅ Optional image upload with simulated analysis (extendable to CNNs)  
- ✅ Personalized plant care tips based on prediction  
- ✅ Elegant result display with health score, tips, and uploaded image preview  

---

## 🛠️ Tech Stack  
- **Backend:** Django 5.x, Python 3.10+  
- **Frontend:** HTML5, CSS3, Bootstrap 5  
- **Machine Learning:** scikit-learn, pandas, joblib  
- **Image Handling:** Pillow  
- **Storage:** Django FileSystemStorage for uploaded images  

---

## 📂 Project Structure 
PlantWhisperer/
│
├── MultipleFiles/
│ ├── ml_model.py # ML training, evaluation & prediction
│ ├── views.py # Django views for form & results
│ ├── templates/
│ │ ├── form.html # Plant health input form
│ │ ├── result.html # Result display with score & tips
│ └── static/
│ ├── background.jpg # Background image
│ └── plant.jpg # GIF/illustration on results page
│
├── db.sqlite3 # Default database (if used)
├── manage.py # Django project manager
└── requirements.txt # Dependencies


---

## ⚡ Installation & Setup  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/yourusername/plant-whisperer.git
cd plant-whisperer

2️⃣ Create & activate virtual environment
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Train ML model

Before running the app, train the plant health ML classifier:

python MultipleFiles/ml_model.py


This will generate:

plant_classifier_model.pkl

plant_encoder.pkl

inside the project folder.

5️⃣ Run migrations & start server
python manage.py migrate
python manage.py runserver

6️⃣ Open in browser

Go to 👉 http://127.0.0.1:8000/

📊 Example Predictions

Thriving 🌱 → Deep green leaves, moist soil, no pests

Okay 🌤️ → Normal growth, partial sun, occasional yellow leaves

Weak 🌿 → Stunted growth, dry soil, pest issues

Sick 🤒 → Brown/yellow leaves, cracked soil, multiple pests

🚀 Future Improvements

Replace simulated image analysis with a CNN model (TensorFlow/PyTorch)

Add multi-plant history tracking for users

Improve advice system with AI-generated suggestions

Deploy on Heroku/AWS/Render for public access

👨‍💻 Contributors

Atharva Nathe

Yash Raut

Utkarsha Hadole

Rutuja Yeotkar

Mentor: Saurabh Sir
