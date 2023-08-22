from flask import Flask, render_template, request
import os
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

if __name__ == "__main__":
    app.run(debug=True)