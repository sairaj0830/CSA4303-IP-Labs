from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Mock Database: In-memory flight inventory
MOCK_FLIGHTS = [
    {"id": 101, "airline": "AeroGlobal", "flight_no": "AG-10", "origin": "NYC", "destination": "LON", "time": "08:00 AM", "price": 450},
    {"id": 102, "airline": "SkyWays", "flight_no": "SW-44", "origin": "NYC", "destination": "LON", "time": "11:30 AM", "price": 380},
    {"id": 103, "airline": "Quantum Air", "flight_no": "QA-02", "origin": "SFO", "destination": "TOK", "time": "01:00 PM", "price": 890},
    {"id": 104, "airline": "AeroGlobal", "flight_no": "AG-12", "origin": "LON", "destination": "NYC", "time": "09:00 AM", "price": 460},
    {"id": 105, "airline": "Nimbus Express", "flight_no": "NE-99", "origin": "NYC", "destination": "LON", "time": "06:00 PM", "price": 310}
]

@app.route('/')
def home():
    # Serves the frontend UI
    return render_template('index.html')

@app.route('/api/flights', methods=['GET'])
def search_flights():
    # Retrieve search parameters from the URL
    origin = request.args.get('origin', '').strip().upper()
    dest = request.args.get('dest', '').strip().upper()
    
    results = MOCK_FLIGHTS
    
    # Filter logic
    if origin:
        results = [f for f in results if f['origin'] == origin]
    if dest:
        results = [f for f in results if f['destination'] == dest]
        
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
