# Social Media App Backend with FastAPI

This repository contains a backend for a social media app built using FastAPI. The app provides basic functionality for posts, user management, authentication, and voting (likes). The application is deployed on Google Cloud Platform (GCP) for enhanced scalability and reliability.

## Features

1. **Post Routes**  
   - Create, update, delete, and retrieve posts.

2. **User Routes**  
   - Create users and retrieve users by ID.

3. **Auth Routes**  
   - Manage login and authentication.

4. **Vote Routes**  
   - Upvote posts.

## Installation

To set up and run the application on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AliAfshar7/FastAPI.git
   cd FastAPI
2. **Install dependencies:**

```bash
pip install fastapi[all]
```
3. **Set up the PostgreSQL database and configure environment variables. Create a .env file in the project root with the following content:**

```bash
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=your_password
DATABASE_NAME=name_of_database
DATABASE_USERNAME=your_username
SECRET_KEY=09d25e094faa2556c818166b7a99f6f0f4c3b88e8d3e7
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```
4. **Run the FastAPI server:**

```bash
uvicorn app.main:app --reload
```
## Database Setup
Ensure PostgreSQL is running.

Create a database and configure the environment variables in the .env file.

The server will start at http://127.0.0.1:8000.

## Technologies Used
This project utilizes a variety of technologies and tools to ensure robust development and deployment:

FastAPI: A modern web framework for building APIs quickly.
PostgreSQL: A powerful, open-source relational database management system.
SQLAlchemy: An SQL toolkit and Object-Relational Mapping (ORM) library for Python.
Pydantic: Data validation and settings management using Python type annotations.
Alembic: A lightweight database migration tool for use with SQLAlchemy.
Uvicorn: A lightning-fast ASGI server to run FastAPI applications.
pytest: A framework for testing Python applications.
Docker: For containerizing the application and its dependencies.
GitHub Actions: To automate CI/CD pipelines.
Google Cloud Platform (GCP): The cloud provider for deployment and hosting.
