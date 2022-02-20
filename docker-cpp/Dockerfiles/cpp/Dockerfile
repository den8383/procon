FROM gcc

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt upgrade -y 

RUN apt install sudo -y


ARG DOCKER_UID=1000
ARG DOCKER_USER=docker
ARG DOCKER_PASSWORD=docker
RUN useradd -m --uid ${DOCKER_UID} --groups sudo ${DOCKER_USER} && echo ${DOCKER_USER}:${DOCKER_PASSWORD} | chpasswd

USER ${DOCKER_USER}



#WORKDIR /home/docker
