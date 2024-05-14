from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

def date_ranges_overlap(start1, end1, start2, end2):
    return start1 <= end2 and start2 <= end1

@app.route('/check_overlap', methods=['POST'])
def check_overlap():
    data = request.get_json()
    if 'start1' in data and 'end1' in data and 'start2' in data and 'end2' in data:
        start1 = datetime.strptime(data['start1'], '%Y-%m-%d')
        end1 = datetime.strptime(data['end1'], '%Y-%m-%d')
        start2 = datetime.strptime(data['start2'], '%Y-%m-%d')
        end2 = datetime.strptime(data['end2'], '%Y-%m-%d')

        overlap = date_ranges_overlap(start1, end1, start2, end2)
        return jsonify({'overlap': overlap})
    else:
        return jsonify({'error': 'Invalid input data'}), 400

if __name__ == '__main__':
    app.run(debug=True)
