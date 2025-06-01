FROM python:3.8.20-slim


RUN apt-get update && apt-get install -y git
RUN pip install --upgrade pip
RUN pip install --default-timeout=10000 git+https://github.com/ankan-debnath/histocartography.git

COPY . /app
WORKDIR /app

CMD ["python", "script.py", "check_model.py","test_image.py"]