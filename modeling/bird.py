from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('bird_observation_model.pkl')

# Route to render the home page with the input form
@app.route('/')
def home():
    return render_template('bird.html')

# Route to handle form submission and make predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get latitude and longitude from form submission
    lat = float(request.form['latitude'])
    lon = float(request.form['longitude'])

    # Apply sine/cosine transformation on the input lat/lon
    lat_sin = np.sin(np.radians(lat))
    lat_cos = np.cos(np.radians(lat))
    lon_sin = np.sin(np.radians(lon))
    lon_cos = np.cos(np.radians(lon))

    # Prepare the input data for the model
    X_input = np.array([[lat_sin, lat_cos, lon_sin, lon_cos]])

    # Make the prediction (1 = observation, 0 = no observation)
    prediction = model.predict(X_input)[0]

    # Show the result on the webpage
    result = "Yes, there's a bird observation" if prediction == 1 else "No, there's no bird observation"
    
    return render_template('bird.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)