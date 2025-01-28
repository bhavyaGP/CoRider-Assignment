
FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENV FLASK_APP=app.py

EXPOSE 3002

CMD ["python", "app.py"]
