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
	@docker credit_card_register-server-1 exec python manage.py migrate

docker_makemigrations:
	@docker credit_card_register-server-1 exec python manage.py migrate