FROM python:3.9

WORKDIR /user_service

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/user_service

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]
