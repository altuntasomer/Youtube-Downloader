FROM python:3.8-slim-buster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg -y
# add app
ADD . /usr/src/app

CMD [ "python3", "downloader.py"]