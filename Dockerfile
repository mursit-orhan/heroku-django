FROM python:3.8.9-alpine

RUN pip install --upgrade pip

# install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app

# copy project
COPY . .

# add and run as non-root user
RUN adduser -D orhan
USER orhan

# EXPOSE 8000

# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "core.wsgi:application" ]

CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT