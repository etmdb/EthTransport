# Version: 1.0
# Dockerfile
FROM python:3.6
MAINTAINER Dawit Nida <dchonch@gmail.com>

ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
WORKDIR /guzo
COPY /guzo guzo
COPY manage.py requirements.pip /app/
RUN pip install -r requirements.pip && \
        python manage.py collectstatic --noinput
EXPOSE 8001
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
