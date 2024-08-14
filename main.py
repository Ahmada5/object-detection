from flask import Flask, request, jsonify
from base64_deconverter import save_base64_image
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Define the upload folder path
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'foto')

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_image():
    data = request.get_json()
    base64_image = data.get('image')

    # Check if the image is provided in the request
    if not base64_image:
        return jsonify({'error': 'No image provided'}), 400

    try:
        # Save the base64 image to the upload folder
        filename = save_base64_image(base64_image, UPLOAD_FOLDER)
        
        # Construct the feedback message
        feedback = f"this image '{filename}' uploaded successfully to '{UPLOAD_FOLDER}'"

        # Return a success response with feedback
        return jsonify({'message': feedback, 'filename': filename}), 200
    except Exception as e:
        # Return an error response with the exception message
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

