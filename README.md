## Setup Instructions

### Installing Required Packages
Make sure to have the necessary packages installed by executing the following commands:

```bash
pip3 install flask
pip3 install json
```

### Project Directory Preparation
First, place your images and labels folder into a folder called "dataset" in the root of the project directory. Ensure that both the images and their corresponding labels share the same filenames. For example:

- dataset
  - images
    - 001.png
    - 002.png
    - ...
  - labels
    - 001.json
    - 002.json
    - ...

### Launching the Application
Navigate into the project directory and start the labelling tool by executing the following commands:

```bash
cd path/to/project/directory
python3 ./labeller.py
```

Now, open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your preferred web browser to access the application.

## Usage Guidelines

### Navigation
- Use the arrow icons located beneath the image to move between images, or select a specific image from the dropdown menu.
- Click on an existing bounding box to remove it.
- To create a new bounding box, click the "Add Bounding Box" button and drag to define the boundaries.
- Click "Save Picture" to save the modifications made to the image.