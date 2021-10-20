FROM python:3

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt upgrade -y 

RUN apt install sudo -y
RUN apt install python3-pip python3-tk -y
RUN pip3 install --upgrade pipenv


ARG DOCKER_UID=1000
ARG DOCKER_USER=docker
ARG DOCKER_PASSWORD=docker
RUN useradd -m --uid ${DOCKER_UID} --groups sudo ${DOCKER_USER} && echo ${DOCKER_USER}:${DOCKER_PASSWORD} | chpasswd

USER ${DOCKER_USER}



#WORKDIR /home/docker
