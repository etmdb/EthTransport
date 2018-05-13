build:
	docker-compose build

up:
	docker-compose up -d

start:
	docker-compose start

stop:
	docker-compose stop

bash-nginx:
	docker exec -it guzo-nginx bash

bash-web:
	docker exec -it guzo-web bash

bash-postgres:
	docker exec -it guzo-postgres bash

bash-redis:
	docker exec -it guzo-redis bash

log-nginx:
	docker-compose logs nginx

log-web:
	docker-compose logs web

log-postgres:
	docker-compose logs postgres

log-redis:
	docker-compose logs redis

collectstatic:
	docker exec guzo-web /bin/sh -c "python manage.py collectstatic --noinput"