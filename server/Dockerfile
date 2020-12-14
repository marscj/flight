FROM python:latest
ENV PYTHONUNBUFFERED 1
ENV REDIS_HOST "redis"
ENV DB_HOST "postgres"
RUN mkdir /server
WORKDIR /server
COPY . /server
RUN pip install --upgrade pip && pip install -r requirements.txt
# EXPOSE 8000
# CMD ["gunicorn", "--chdir", "server", "--bind", ":8000", "server.wsgi:application"]