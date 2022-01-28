FROM python:3.9
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt