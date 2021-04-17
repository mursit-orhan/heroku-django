FROM python:3.8.9-alpine

RUN pip install --upgrade pip

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app

COPY . .

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "core.wsgi:application" ]
