FROM python:3.11.11-slim

COPY requirements.txt requirements.txt
COPY startup.sh startup.sh

RUN apt-get update && apt-get install -y git
RUN apt-get update && apt-get install -y curl && curl https://huggingface.co
RUN apt-get update && apt-get install -y wget

RUN pip install --upgrade pip
RUN bash startup.sh

RUN mkdir -p /root/.cache/huggingface/hub/models--microsoft--llava-med-v1.5-mistral-7b/snapshots/

EXPOSE 8000

COPY . /app
WORKDIR /app

# CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
CMD ["python", "-m", "backend.load_model"]