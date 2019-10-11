FROM ubuntu:16.04
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

RUN apt install -y python3 python3-setuptools build-essential python3-dev  
RUN apt install -y python3-pip
RUN apt install -y libpq-dev
RUN pip3 install --upgrade pip

WORKDIR $BACKENDDIR
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

# CMD [ "sh", "-c", "python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py initadmin && python3 manage.py runserver 0.0.0.0:8000"]
