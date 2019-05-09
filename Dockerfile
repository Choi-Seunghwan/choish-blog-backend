FROM ubuntu:18.04
MAINTAINER Choi Seunghwan <choiseunghwan.tech@gmail.com>

ENV HOMEDIR=/home
ENV PROJECTDIR=/home/blog
ENV BACKENDDIR=/home/blog/backend

EXPOSE 8000

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN apt-get install -y netcat
RUN add-apt-repository ppa:ubuntu-toolchain-r/ppa
RUN apt-get update

RUN apt install -y python3.7 python3-pip python3-dev libpq-dev build-essential
RUN apt-get install -y git

# update pip
RUN pip3 install --upgrade pip

WORKDIR $BACKENDDIR
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# CMD [ "sh", "-c", "python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py initadmin && python3 manage.py runserver 0.0.0.0:8000"]
