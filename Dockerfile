FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0

COPY . /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_sm

EXPOSE 5000

CMD ["python", "app.py"]
