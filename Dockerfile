FROM python:3.8.8-alpine3.13

WORKDIR /app

EXPOSE 5000

COPY requirements.txt requirements.txt

CMD ["pip", "install", "--upgrade", "pip"]

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m" , "flask", "run"]