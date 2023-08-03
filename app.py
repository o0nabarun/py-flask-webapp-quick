from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_data():
    data = {
        'name': 'Mickey',
        'age': 20,
        'city': 'Noneville'
    }
    return jsonify(data)
  
