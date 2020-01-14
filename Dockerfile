FROM docker.io/ubuntu:bionic
RUN apt-get update && apt-get -y install bf python3
RUN apt-get install -y cpp
WORKDIR /mnt
