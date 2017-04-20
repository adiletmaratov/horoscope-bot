FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src
ADD requirements.txt /src/
RUN mkdir /src/logs
RUN pip install -r /src/requirements.txt
ADD . /src/
