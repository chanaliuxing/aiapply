.PHONY: up down test e2e seed build-ext package-ext

up:
@echo "Start services with docker-compose (placeholder)"

down:
@echo "Stop services (placeholder)"

test:
pytest

e2e:
pytest apps/e2e || true

seed:
@echo "Seed database (placeholder)"

build-ext:
@echo "Build extension (placeholder)"

package-ext:
@echo "Package extension (placeholder)"
