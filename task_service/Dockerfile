FROM python:3.9

WORKDIR /task_service

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/task_service

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
