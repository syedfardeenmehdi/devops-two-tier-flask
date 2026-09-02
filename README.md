# DevOps Two-Tier Flask Application

A simple two-tier web application built with Flask and MySQL, containerized using Docker and Docker Compose.

## Architecture

The application follows a two-tier architecture:

Browser → Flask Web Application → MySQL Database

- **Web Tier:** Python Flask
- **Database Tier:** MySQL 8.0
- **Containerization:** Docker
- **Orchestration:** Docker Compose
- **Version Control:** Git & GitHub

## Technologies Used

- Python
- Flask
- MySQL 8.0
- Docker
- Docker Compose
- Git
- GitHub

## Project Structure

```text
devops-two-tier-flask/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── README.md
└── venv/