from flask import Flask, request, jsonify
import os

from .utils import Image_Processor, med_model

UPLOAD_FOLDER = 'temp_uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
image_processor = Image_Processor()


@app.route('/response', methods=['POST']) #
def chatbot():
    data = request.form
    message = str(data['message'])
    chat_history = data['chat_history']

    med_responses = []

    if 'image' in request.files:
        file = request.files['image']
        filename = "original.png"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        classification = image_processor.classify_image(filepath)
        if classification == "pathology":
            image_processor.generate_patches(filepath, UPLOAD_FOLDER)

        for image_name in os.listdir(UPLOAD_FOLDER):
            image_path = os.path.join(UPLOAD_FOLDER, image_name)
            answer = med_model.get_response("#", message, image_path)   #not implemented yet
            med_responses.append({image_name: answer})
    else:
        answer = med_model.get_response("#", message)
        med_responses.append(answer)

    # history_str = "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in chat_history])

    # response = get_response(message, history_str)
    # print(response)

    return jsonify( { 'response' : med_responses } )
