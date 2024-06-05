FROM python:3.9

WORKDIR /notification_service

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/notification_service

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003"]
