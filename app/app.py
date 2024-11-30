# app.py

from flask import Flask, render_template, request
import sys
import os

# Import custom modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from models.model_services import ModelService

# Initialize Flask app
app = Flask(__name__)

# Load the model
ml_svc = ModelService()
ml_svc.load_model()


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            # Collect input data
            area = float(request.form["area"])
            year = int(request.form["year"])
            bedrooms = int(request.form["bedrooms"])
            garden = float(request.form["garden"])
            balcony = int(request.form["balcony"])
            storage = int(request.form["storage"])
            parking = int(request.form["parking"])
            furnished = int(request.form["furnished"])
            garage = int(request.form["garage"])

            # Make prediction
            prediction = ml_svc.predict(
                [
                    area,
                    year,
                    bedrooms,
                    garden,
                    balcony,
                    storage,
                    parking,
                    furnished,
                    garage,
                ]
            )
            prediction = f"${prediction[0]:,.2f}"

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
