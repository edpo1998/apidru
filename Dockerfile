FROM python:3.10.6

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

ENV TZ=America/Guatemala

EXPOSE 9000

RUN mkdir /consumer-dru-back

WORKDIR /consumer-dru-back

COPY requirements/base.txt /consumer-dru-back/

RUN pip install --no-cache-dir -r base.txt

RUN pip install gunicorn

RUN adduser --disabled-password --gecos '' devops

COPY . /consumer-dru-back/ 

RUN chown -R devops:devops /consumer-dru-back/

RUN chmod +x run_api.sh

# gunicorn hello_django.wsgi:application --bind 0.0.0.0:8000
# docker run -it -p 7200:9000 -v $(pwd)"/app simpleapp"
# docker start -a idcontainer
#CMD python manage.py runserver 0.0.0.0:9000
# sudo docker run -d --name discourse_app local_discourse/app