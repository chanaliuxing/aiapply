.PHONY: up down test e2e seed build-ext package-ext dev-api dev-companion dev-ext

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

dev-api:
	uvicorn apps.api.main:app --reload --port 8000

dev-companion:
	uvicorn apps.companion.main:app --reload --port 8765

dev-ext:
	@echo "Start extension dev server (placeholder)"
