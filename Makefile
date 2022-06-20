compose:
	docker-compose up -d

compose-down:
	docker-compose down || true

lint:
	poetry run flake8 --exclude .venv,migrations .

install:
	poetry install
