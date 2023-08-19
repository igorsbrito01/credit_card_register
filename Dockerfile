FROM python:3.9-slim-bullseye

COPY requirements.txt ./
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r /requirements.txt

COPY . /server
WORKDIR /server/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080" ]