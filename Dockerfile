# syntax=docker/dockerfile:1
FROM python:3.9.9-slim-bullseye
WORKDIR /home
COPY . .
RUN pip install -r requirements.txt
RUN python manage.py migrate
EXPOSE 8000
CMD ["/usr/local/bin/python3", "manage.py", "runserver","0.0.0.0:8000"]



