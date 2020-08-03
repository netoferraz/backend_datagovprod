FROM python:3.7

EXPOSE 8081

COPY ./app /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN python ./models/download.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]