from django.shortcuts import render
import joblib
import numpy as np

model = joblib.load('ml_models/iris_model.pkl')  # Make sure this path is valid

def index(request):
    return render(request, 'iris_app/index.html')

def predict(request):
    if request.method == 'POST':
        sepal_length = float(request.POST['sepal_length'])
        sepal_width = float(request.POST['sepal_width'])
        petal_length = float(request.POST['petal_length'])
        petal_width = float(request.POST['petal_width'])

        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = model.predict(features)

        species = {
            0: "Setosa 🌺",
            1: "Versicolor 🌸",
            2: "Virginica 🌼"
        }.get(prediction[0], "Unknown")

        return render(request, 'iris_app/result.html', {'result': species})

    return render(request, 'iris_app/index.html')
