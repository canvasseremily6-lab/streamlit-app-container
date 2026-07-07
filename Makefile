# Makefile for the dockerized streamlit movie sentiment app

# Define variables for the review 
REVIEW := sentiment-app

build:
	@echo "Building Docker image: $(REVIEW)"
	docker build -t $(REVIEW) .

run: 
	@echo "Running Docker container..."
	docker run --rm -p 8501:8501 $(REVIEW)

clean: 
	@echo "Removing Docker image: $(REVIEW)"
	docker rmi $(REVIEW) || true  
