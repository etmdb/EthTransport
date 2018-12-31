# Version: 1.0
# Dockerfile
FROM python:3.4.6
MAINTAINER Dawit Nida <dchonch@gmail.com>

ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true

# Install Python and Package Libraries
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y \
    libffi-dev \
    libssl-dev \
    libxml2-dev \
    libxslt-dev \
    libjpeg-dev \
    libfreetype6-dev \
    zlib1g-dev \
    net-tools \
    vim

# Project Files and Settings
ARG PROJECT=guzo
ARG PROJECT_DIR=/${PROJECT}

RUN mkdir -p ${PROJECT}
WORKDIR ${PROJECT_DIR}
COPY ${PROJECT_DIR} .
COPY manage.py requirements.pip ${PROJECT_DIR}/
RUN pip install --upgrade pip
RUN pip install -r requirements.pip

# Server Setup
EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
