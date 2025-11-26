# Weapon Detection AI System

![Weapon Detection System Demo](https://github.com/italhachaudhary/weapon_detection_app/blob/main/Screenshot%202025-11-26%20075041.png?raw=true)

## Project Description
The **Weapon Detection AI System** is a specialized computer vision application designed to enhance security and safety measures by automating the identification of dangerous objects—specifically **pistols** and **knives**. This project leverages the power of Deep Learning to perform accurate object detection, providing a technological solution for surveillance analysis and threat assessment.

## Core Technology
At the heart of the system lies a custom-trained **YOLOv8 (You Only Look Once)** model. 
- **Architecture**: YOLOv8 is a state-of-the-art neural network architecture renowned for its speed and accuracy.
- **Training**: The model was fine-tuned using the **[ari-dasci OD-WeaponDetection dataset](https://github.com/ari-dasci/OD-WeaponDetection)**, enabling it to learn the distinct visual features of handguns and bladed weapons across various backgrounds and orientations.
- **Weights**: The training process resulted in a dedicated weights file (`best.pt`) capable of predicting weapon locations with high confidence.

## Web Application Interface
To make this advanced AI model accessible to users, the project features a responsive web interface built using **Flask**, a lightweight Python web framework. 
- **Frontend**: Designed with **HTML5** and **CSS3**, utilizing **Jinja2** templating to dynamically render content.
- **Functionality**: The interface allows users to seamlessly upload images from their local devices for immediate analysis.

## Workflow
1. **Input**: The user uploads an image containing potential threats via the web portal.
2. **Processing**: The Flask backend receives the image and passes it to the loaded YOLOv8 model. The model performs inference, scanning the image for patterns matching its training data (pistols and knives).
3. **Output**: The system generates a new version of the image with bounding boxes drawn around detected objects. This annotated image is displayed side-by-side with the original upload, providing clear, visual verification of the AI's findings.

## Installation and Setup

### Prerequisites
- Python 3.8+
- pip

### Steps
1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd weapon_detection_app
   ```

2. **Install Dependencies**
   It is recommended to use a virtual environment.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python app.py
   ```

4. **Access the Interface**
   Open your web browser and navigate to `http://127.0.0.1:5000/` (or the port specified in the terminal).

## Usage
- Open the web interface.
- Click on the upload button to select an image from your device.
- Submit the image for analysis.
- View the results with detected weapons highlighted by bounding boxes.

## Purpose
This system serves as a robust prototype for automated security monitoring, demonstrating how AI can be deployed to assist in preventing violence and ensuring public safety.





