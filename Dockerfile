FROM python:3.6.15-slim-buster

WORKDIR /app

EXPOSE 80

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=80"]