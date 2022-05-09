FROM python:3.6.15-slim-buster

WORKDIR /app

EXPOSE 5000

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "-m" , "flask", "run"]