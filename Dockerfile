FROM python:3.8-alpine

WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt

EXPOSE 3000
CMD ["python", "/app/app.py"]