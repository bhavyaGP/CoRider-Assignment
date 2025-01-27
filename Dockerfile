FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 3002

#ENV NAME venv

CMD ["python", "app.py"]