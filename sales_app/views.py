from django.shortcuts import render
import joblib
import numpy as np

model = joblib.load('ml_models/sales_model.pkl')  # trained sales prediction model

def index(request):
    return render(request, 'sales_app/index.html')

def predict(request):
    if request.method == 'POST':
        tv = float(request.POST['tv'])
        radio = float(request.POST['radio'])
        newspaper = float(request.POST['newspaper'])

        features = np.array([[tv, radio, newspaper]])
        prediction = model.predict(features)
        result = f"📈 Predicted Sales: {prediction[0]:.2f} units"

        return render(request, 'sales_app/result.html', {'result': result})

    return render(request, 'sales_app/index.html')
