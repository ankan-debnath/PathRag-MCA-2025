from flask import Flask, request, jsonify
import os

from .llava_med import model as med_model

app = Flask(__name__)
UPLOAD_FOLDER = 'temp_uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)



@app.route('/response', methods=['POST']) #
def chatbot():
    data = request.form
    message = str(data['message'])
    chat_history = data['chat_history']
    med_responces = []
    input_ids, attention_mask = med_model.create_conversations(message)

    if 'image' in request.files:
        file = request.files['image']
        filename = "image.png"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        for image_name in os.listdir(UPLOAD_FOLDER):
            image_path = os.path.join(UPLOAD_FOLDER, image_name)
            image_tensor = med_model.get_image_tensors(image_path)
            answer = med_model.generate_response(input_ids, attention_mask, image_tensor)
            med_responces.append({image_path : answer})
    else:
        answer = med_model.generate_response(input_ids, attention_mask)
        med_responces.append(answer)

    return jsonify( { 'response' : med_responces } )
