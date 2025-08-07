import pandas as pd
import joblib
from django.shortcuts import render

# Load the trained model with Averaged_V — make sure filename matches saved model
model = joblib.load("ml_models/fraud_model_with_avg.pkl")

def fraud_view(request):
    return render(request, "fraud/index.html", {
        "numbers": range(1, 29)  # For looping V1 to V28
    })

def fraud_predict(request):
    if request.method == "POST":
        # Extract and convert all V1 to V28
        v_values = [float(request.POST.get(f'v{i}', 0)) for i in range(1, 29)]
        
        # Calculate Averaged_V
        averaged_v = sum(v_values) / len(v_values)

        # Prepare input in order: Time, V1–V28, Amount, Averaged_V
        input_values = [
            float(request.POST.get("time", 0))
        ] + v_values + [
            float(request.POST.get("amount", 0)),
            averaged_v
        ]

        # Define column names exactly as in training (Amount before Averaged_V)
        features = ["Time"] + [f"V{i}" for i in range(1, 29)] + ["Amount", "Averaged_V"]

        # Wrap input in DataFrame with correct column names
        input_df = pd.DataFrame([input_values], columns=features)

        # Make prediction
        prediction = model.predict(input_df)[0]

        result_text = "Fraud Detected ✅" if prediction == 1 else "No Fraud Detected ❌"

        # Send back inputs + result
        return render(request, "fraud/result.html", {
            "inputs": zip(features, input_values),
            "result": result_text,
        })

    # For GET requests, just show the form
    return render(request, "fraud/index.html", {
        "numbers": range(1, 29)
    })
