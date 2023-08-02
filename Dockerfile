FROM python:3.10

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get -y install postgresql

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "./app.py" ]