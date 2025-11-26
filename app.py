import os
import cv2
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from ultralytics import YOLO
from werkzeug.utils import secure_filename

# Initialize Flask App
app = Flask(__name__)

# Config
UPLOAD_FOLDER = 'static/uploads'
RESULT_FOLDER = 'static/results'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# Load your custom trained model
# Ensure 'best.pt' is in the same directory as app.py
print("Loading model...")
try:
    model = YOLO('best.pt')
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    print("Make sure 'best.pt' is in the correct folder.")
    exit()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)

        if file:
            # Save the file
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Run Inference
            # save=True saves it to 'runs/detect/predict...', we want to control the save
            results = model.predict(filepath, conf=0.25)
            
            # Plot the results (draw bounding boxes)
            # This returns a numpy array of the image with boxes
            res_plotted = results[0].plot()

            # Save the result image to our static folder
            save_path = os.path.join(app.config['RESULT_FOLDER'], filename)
            cv2.imwrite(save_path, res_plotted)

            return render_template('index.html', uploaded_image=filename, result_image=filename)

    return render_template('index.html')

@app.route('/display/<filename>')
def display_image(filename):
    return send_from_directory(app.config['RESULT_FOLDER'], filename)

if __name__ == '__main__':
    # Run the app locally
    app.run(debug=True, port=5000)