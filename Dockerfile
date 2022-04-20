FROM python:3.10.4

WORKDIR /app

RUN pip install websockets && pip install requests

COPY . .

CMD ["python", "main.py"]
 
