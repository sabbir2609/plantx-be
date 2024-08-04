# base image
FROM python:3.12.4-slim

# options
ENV PYTHONUNBUFFERED 1

# Set working directory
RUN mkdir app
# set the working directory
COPY . /app/
# coppy commands 
WORKDIR /app

# update docker-iamage packages
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y netcat-openbsd gcc && \
    apt-get clean

# update pip 
RUN pip install --upgrade pip
# install psycopg for connect to pgsql
RUN pip install psycopg2-binary
# install python packages 
RUN pip install -r requirements.txt
# create static directory
# RUN mkdir staticfiles
# RUN python manage.py collectstatic --no-input
EXPOSE 8000
CMD ["gunicorn","--bind", ":8000", "core.wsgi:application"]