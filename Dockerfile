FROM python:3.9

WORKDIR /app

COPY requirements_docker.txt requirements.txt 
RUN pip3 install -r requirements.txt

COPY . . 

ENV PORT=8000
EXPOSE $PORT

CMD uvicorn main:app --host 0.0.0.0 --port $PORT 
