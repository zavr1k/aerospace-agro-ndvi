compose:
	docker-compose up -d

compose-down:
	docker-compose down || true

compose-build:
	docker-compose build

compose-logs:
	docker-compose logs -f

lint:
	poetry run flake8 --exclude .venv .

prepare:
	cp -n .env.example .env || true

