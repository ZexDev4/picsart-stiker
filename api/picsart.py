from flask import Flask, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/picsart', methods=['GET'])
def get_picsart_data():
    overlay = request.args.get('overlay')
    next_url = request.args.get('next')

    if next_url:
        url = next_url
    elif overlay:
        url = f'https://api.picsart.com/stickers/mixed/freetoedit/search.json?q={overlay}'
    else:
        return jsonify({'error': 'Missing parameters'}), 400

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return jsonify(response.json())
        return jsonify({'error': 'Failed to fetch data from PicsArt'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500
