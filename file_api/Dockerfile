FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]