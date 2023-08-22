from flask import Flask, render_template, request
import os
from flask import request, jsonify
import json

app = Flask(__name__, static_url_path='', static_folder=os.path.join(os.path.dirname(__file__), '..'))

@app.route('/')
def home():
    image_index = int(request.args.get('image_index', 0))
    image_index = max(0, min(99, image_index))

    # Load bounding boxes from the corresponding JSON file
    json_path = os.path.join(os.path.dirname(__file__), '..', 'labels', '%03d.json' % image_index)
    with open(json_path, 'r') as file:
        labels = json.load(file)
        bboxes = labels.get('bboxes', [])

    return render_template('index.html', image_index=image_index, bboxes=bboxes)

@app.route('/save_bboxes/<int:image_index>', methods=['POST'])
def save_bboxes(image_index):
    try:
        data = request.json
        bboxes = data['bboxes']
        filename = os.path.join('../labels', '%03d.json' % image_index)
        print(f"Saving to {filename} with bboxes {bboxes}")  # Debug print

        with open(filename, 'w') as file:
            json.dump({'bboxes': bboxes}, file)

        return jsonify(success=True)
    except Exception as e:
        print(f"Error: {e}")  # Logging the error can help in debugging
        return jsonify(success=False), 500

if __name__ == "__main__":
    app.run(debug=True)