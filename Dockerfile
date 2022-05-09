FROM python:3.6.15-slim-buster

WORKDIR /app

EXPOSE 5000

COPY requirements.txt requirements.txt

CMD [ "python", "-m", "pip", "install", "--upgrade", "pip"]

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "-m" , "flask", "run"]