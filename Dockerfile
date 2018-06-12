FROM    python:3.6-jessie
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 8080

CMD gunicorn -b :8080 docker_demo.wsgi
