upbuild: build up

up:
	docker-compose up

build:
	docker-compose build

run:
	docker-compose run $(filter-out $@,$(MAKECMDGOALS))

restart:
	docker-compose restart $(filter-out $@,$(MAKECMDGOALS))

shell:
	docker-compose exec django /entrypoint python manage.py shell_plus

bash:
	docker-compose exec django /entrypoint sh

manage:
	docker-compose run --rm django python manage.py $(filter-out $@,$(MAKECMDGOALS))

startapp:
	docker-compose run --rm django python manage.py startapp $(filter-out $@,$(MAKECMDGOALS))

makemigrations:
	docker-compose run --rm django python manage.py makemigrations $(filter-out $@,$(MAKECMDGOALS))

migrate:
	docker-compose run --rm django python manage.py migrate $(filter-out $@,$(MAKECMDGOALS))

createsuperuser:
	docker-compose run --rm django python manage.py createsuperuser $(filter-out $@,$(MAKECMDGOALS))

collectstatic:
	docker-compose run --rm django python manage.py collectstatic --noinput

makemessages:
	docker-compose run --rm django python manage.py makemessages --no-location -l ar

compilemessages:
	docker-compose run --rm django python manage.py compilemessages

urls:
	docker-compose run django python manage.py show_urls

logs:
	docker-compose logs -f $(filter-out $@,$(MAKECMDGOALS))

test:
	docker-compose run django python manage.py test $(filter-out $@,$(MAKECMDGOALS))

debug:
	docker-compose run --service-ports --rm $(filter-out $@,$(MAKECMDGOALS))

down:
	docker-compose down $(filter-out $@,$(MAKECMDGOALS))

destroy:
	docker-compose down -v

rm_pyc:
	find . -name '__pycache__' -name '*.pyc' | xargs rm -rf
