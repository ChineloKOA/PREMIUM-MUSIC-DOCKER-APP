# Define the message variable for commit messages
MESSAGE ?= "Default commit message"

# Build the Docker containers without starting them
build:
	docker-compose up -d --build

# Run the Docker containers
run:
	docker-compose up

# Build and then run the Docker containers
build_run: build run

# Pull the latest changes, commit, and push to the repository
push:
	git pull
	git commit -am $${MESSAGE} # Use double dollar sign to escape the variable in the Makefile
	git push