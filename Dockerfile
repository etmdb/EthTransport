FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /EthTransport
WORKDIR /EthTransport
ADD requirements.txt /EthTransport/
RUN pip install -r requirements.txt
ADD . /EthTransport/