update-deps:
	docker compose exec api python -m piptools compile -o requirements.txt pyproject.toml

install-deps:
	docker compose exec api pip-sync requirements.txt

local-up:
	docker compose up -d

local-test:
	echo "Implement me!"
