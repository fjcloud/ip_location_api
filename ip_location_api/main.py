## main.py
from flask import Flask, request, jsonify
from ip_location import IPGeolocation, IPGeolocationError
import ipaddress

app = Flask(__name__)

@app.route('/location', methods=['POST'])
def get_location():
    data = request.get_json()
    ip = data.get('ip')
    if not ip:
        return jsonify({'error': 'IP address is required'}), 400

    # Validate IP address
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return jsonify({'error': 'Invalid IP address'}), 400

    try:
        ip_geo = IPGeolocation(ip)
        city = ip_geo.get_location()
        return jsonify({'city': city}), 200
    except IPGeolocationError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
