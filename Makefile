update-deps:
	docker compose exec age-group-api python -m piptools compile -o requirements.txt pyproject.toml

install-deps:
	docker compose exec age-group-api pip-sync requirements.txt

local-up:
	docker compose up -d

local-test:
	docker compose exec age-group-api pytest
