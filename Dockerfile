FROM python:3.7
RUN mkdir /app
ADD . /app/
WORKDIR /app
RUN pip install -r requirements.txt --upgrade
RUN python manage.py migrate
EXPOSE 8000
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
