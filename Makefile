# Define the message variable for commit messages
MESSAGE ?= "Default commit message"

# Build the Docker containers without starting them
build:
	docker-compose build

# Run the Docker containers
run:
	docker-compose up

# Build and then run the Docker containers
build_run: build run

# Pull the latest changes, commit, and push to the repository
push:
	git pull
	git commit -am $${MESSAGE}
	git push