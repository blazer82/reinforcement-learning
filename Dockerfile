FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y python-pip python3-opengl zlib1g-dev libjpeg-dev patchelf cmake swig libboost-all-dev libsdl2-dev libosmesa6-dev xvfb ffmpeg

RUN pip install --upgrade pip
RUN pip install numpy scipy pillow
RUN pip install tensorflow
RUN pip install gym
RUN pip install gym[atari]
