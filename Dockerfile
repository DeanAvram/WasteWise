# syntax=docker/dockerfile:1

FROM python:3.11
LABEL authors="Daniel Ben-Avi, Dean Avram"

WORKDIR /wastewise

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
