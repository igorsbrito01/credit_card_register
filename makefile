run_server:
	@python manage.py run_server

makemigrations:
	@python manage.py makemigrations

migrate:
	@python manage.py migrate

build_server_image:
	@docker-compose build server

docker_run_server:
	@docker-compose up -d

docker_migrate:
	@docker exec credit_card_register-server-1 python manage.py migrate

docker_makemigrations:
	@docker exec credit_card_register-server-1 python manage.py makemigrations

docker_run_tests:
	@docker exec credit_card_register-server-1 python manage.py test payments.tests
