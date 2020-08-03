FROM python:3.7

EXPOSE 80

COPY ./app /app
WORKDIR /app

RUN pip install -r requirements.txt


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]