from django.shortcuts import render
import joblib
import numpy as np

model = joblib.load('ml_models/titanic_model.pkl')  # Your trained Titanic model

def index(request):
    return render(request, 'titanic_app/index.html')

def predict(request):
    if request.method == 'POST':
        pclass = int(request.POST['pclass'])
        age = float(request.POST['age'])
        sibsp = int(request.POST['sibsp'])
        fare = float(request.POST['fare'])
        gender = request.POST['gender']

        gender_encoded = 1 if gender.lower() == 'male' else 0

        features = np.array([[pclass, age, sibsp, fare, gender_encoded]])
        prediction = model.predict(features)

        result = "🛟 Survived" if prediction[0] == 1 else "⚰️ Did Not Survive"
        return render(request, 'titanic_app/result.html', {'result': result})

    return render(request, 'titanic_app/index.html')
