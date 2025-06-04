import requests
import os
from dotenv import load_dotenv

load_dotenv()

MED_SERVICE_URI = os.getenv("MED_SERVICE_URI")

def get_response(message, image_path=None):
    # Prepare the form data
    data = {"message": message}

    files = None
    if image_path is not None:
        if not os.path.exists(image_path):
            return {"error": f"Image file not found at {image_path}"}
        files = {"image": open(image_path, "rb")}

    try:
        response = requests.post(MED_SERVICE_URI, data=data, files=files)

        if files:
            files["image"].close()

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Error from API: {response.status_code} - {response.text}"}

    except Exception as e:
        return {"error": str(e)}