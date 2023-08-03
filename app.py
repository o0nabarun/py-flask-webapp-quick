from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_data():
    data = {
        'name': 'Mickey',
        'year': 1928,
        'city': 'Noneville'
    }
    return jsonify(data)
  
