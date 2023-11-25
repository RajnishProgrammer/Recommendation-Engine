from flask import Flask, render_template, request, jsonify
import requests
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

GEONAMES_USERNAME = 'akatsuki_geo'  # Replace with your username
SEARCH_API = "http://api.geonames.org/searchJSON"

df = pd.read_excel('Modified_GARE_Data.xlsx')
numeric_features = ['MinProjectSize', 'Ratings']  
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())])
preprocessor = ColumnTransformer(transformers=[('num', numeric_transformer, numeric_features)])


def recommend_agencies(user_preferences):
    
    filtered_df = df[(df['TypeOfAgency'] == user_preferences['TypeOfAgency']) & 
                     (df['City'] == user_preferences['Location'])]
    agency_profile = preprocessor.fit_transform(filtered_df)

    # Process user preferences
    user_df = pd.DataFrame([{'MinProjectSize': user_preferences['MinProjectSize'], 'Ratings': user_preferences['Ratings']}])
    user_profile = preprocessor.transform(user_df)

    # Calculate cosine similarity
    similarity_scores = cosine_similarity(user_profile, agency_profile)
    
    # Rank agencies and select top 5
    ranked_agencies_indices = np.argsort(similarity_scores.flatten())[::-1]
    mm_agencies_indices = ranked_agencies_indices[:5]
    mm_agencies = filtered_df.iloc[mm_agencies_indices]

    return mm_agencies

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        type_ = request.form.get('type_of_project') or ""
        location_ = request.form.get('location') or ""
        budget_ = request.form.get('budget') or 0
        ratings_ = request.form.get('ratings') or 0

        user_input = {
            'TypeOfAgency': type_,
            'Location': location_,
            'MinProjectSize': budget_,
            'Ratings': ratings_,
        }
        recommended_agencies = recommend_agencies(user_input)
        return render_template('result.html', recommendations=recommended_agencies.to_dict(orient='records'))
    
    return render_template('index.html')

@app.route('/search_location', methods=['GET'])
def search_location():
    query = request.args.get('q', '')
    response = requests.get(SEARCH_API, params={
        'q': query,
        'username': GEONAMES_USERNAME,
        'maxRows': 10,
        'type': 'json'
    })
    
    if response.status_code != 200:
        return jsonify([])

    data = response.json()
    cities = [entry['name'] for entry in data.get('geonames', [])]

    return jsonify(cities)

if __name__ == '__main__':
    app.run(debug=True)
