# Base image
FROM python:3.11-slim

# Set work directory
RUN mkdir "code"
WORKDIR "code"

# Install dependencies
COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt


#copy files
ADD . /code/
ADD .env.docker /code/.env


## Migrate
#RUN python manage.py migrate

COPY . /code/
CMD gunicorn VPNSite.wsgi:application -b 0.0.0.0:8000

