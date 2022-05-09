FROM python:latest

WORKDIR /app

EXPOSE 5000

COPY requirements.txt requirements.txt

CMD [ "python", "-m", "pip", "install", "--upgrade", "pip", "--user"]

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "-m" , "flask", "run"]