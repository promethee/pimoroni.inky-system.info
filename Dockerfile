FROM debian:buster-slim
RUN apt-get update
RUN apt-get install -y apt-utils autoconf automake build-essential g++ gcc git make libatlas-base-dev libfreetype6-dev libgl1-mesa-glx libjpeg-dev libopenjp2-7 libportmidi-dev libsdl-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libtiff5 libtool python-numpy python-pil python3 python3-pip
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt
WORKDIR /usr/src/app
COPY ./CODE2000.TTF ./main.py ./
CMD python3 main.py
