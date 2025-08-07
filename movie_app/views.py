import pandas as pd
import joblib
import os
from django.shortcuts import render

# Load model
model = joblib.load(os.path.join('ml_models', 'movie_model.pkl'))

# Load dataset
movie_df = pd.read_csv("imdb_indian_movies.csv", encoding='latin1')
movie_df = movie_df[['Genre', 'Director', 'Actor 1', 'Rating']].dropna()

# Get unique dropdown values
GENRES = sorted(movie_df['Genre'].unique().tolist())
DIRECTORS = sorted(movie_df['Director'].unique().tolist())
ACTORS = sorted(movie_df['Actor 1'].unique().tolist())

# Label encode them the same way as during training
from sklearn.preprocessing import LabelEncoder
le_genre = LabelEncoder().fit(GENRES)
le_director = LabelEncoder().fit(DIRECTORS)
le_actor = LabelEncoder().fit(ACTORS)

def index(request):
    return render(request, 'movie_app/index.html', {
        'genres': GENRES,
        'directors': DIRECTORS,
        'actors': ACTORS
    })

def predict(request):
    if request.method == 'POST':
        genre = request.POST['genre']
        director = request.POST['director']
        actor = request.POST['actor']

        # Encode user selections
        genre_encoded = le_genre.transform([genre])[0]
        director_encoded = le_director.transform([director])[0]
        actor_encoded = le_actor.transform([actor])[0]

        features = [[genre_encoded, director_encoded, actor_encoded]]
        prediction = model.predict(features)[0]

        # ✅ Debugging prints (now correctly placed)
        print(f"Inputs: {genre}, {director}, {actor}")
        print(f"Encoded: {features}")
        print(f"Predicted rating: {prediction}")

        return render(request, 'movie_app/result.html', {
            'prediction': round(prediction, 2)
        })

    # Optional fallback for GET requests
    return render(request, 'movie_app/result.html', {
        'prediction': "No prediction made. Please submit the form."
    })


