FROM python:3.9

WORKDIR /api_gateway

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/api_gateway

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
