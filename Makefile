up:
	docker compose up --build

down:
	docker compose down

re: down up

lint:
	docker compose run --rm --build --no-deps app bash scripts/lint.sh

test:
	docker compose run --rm --build app bash scripts/test.sh

clean:
	find . -path ./.venv -prune -o -type d -name __pycache__ -prune -exec rm -rf {} +
	rm -rf .pytest_cache .ruff_cache .coverage htmlcov

prune: clean
	docker compose down --volumes --remove-orphans --rmi all
	docker builder prune --force --filter type=exec.cachemount

.PHONY: up down re lint test clean prune
