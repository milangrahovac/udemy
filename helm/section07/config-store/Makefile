.PHONY: run
run: stop ## Stop server on port 3000 if running then run npm server on port 3000.
	sleep 1
	npm run dev

.PHONY: stop
stop: ## Stop the server on port 3000.
	sh stop_server.sh

.PHONY: build
build: ## Stop the server on port 3000.
	docker compose up --build --watch