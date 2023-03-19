from flask import Flask, jsonify, request
from utils import get_location, get_estimated_price

app = Flask(__name__)


@app.route('/hello')
def hello():
    return "hi"


@app.route('/get-location')
def get_location_names():
    response = jsonify({
        'locations': get_location()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get-prediction', methods=['POST'])
def predict_home_price():
    location = (request.form['location'])
    total_sqft = float(request.form['total_sqft'])
    bhk = float(request.form['bhk'])
    bath = float(request.form['bath'])
    response = jsonify({
        'estimated_price': get_estimated_price(location,total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print("Starting Python Flask Server For Home Pricing Prediction...")
    app.run()
