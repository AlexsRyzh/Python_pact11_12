# Base image
FROM python

WORKDIR /usr/src/app


COPY ./pact11_12 ./pact11_12
COPY ./pract_11 ./pract_11
COPY ./pract_12 ./pract_12
COPY ./manage.py ./
COPY requirements.txt ./

# Install project dependencies
RUN pip install -r requirements.txt


CMD ["python manage.py makemigrations", "python manage.py migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]