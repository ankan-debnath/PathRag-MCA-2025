import os

import nest_asyncio
from pyngrok import ngrok
import threading
import subprocess
from dotenv import load_dotenv

load_dotenv()

AUTH_TOKEN = os.getenv("NGROK_AUTH_TOKEN")

nest_asyncio.apply()
ngrok.set_auth_token(AUTH_TOKEN)

def run_gunicorn():
    # Run gunicorn for your Flask app
    subprocess.run([
        "gunicorn",
        "app:app",
        "--bind", "0.0.0.0:5000"
    ])

threading.Thread(target=run_gunicorn, daemon=True).start()

# Start ngrok tunnel to port 5000
public_url = ngrok.connect(5000)
print("🔗 Public URL:", public_url)