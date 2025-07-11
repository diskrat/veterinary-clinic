# Veterinary Clinic API

This project is a FastAPI-based backend for a veterinary clinic, using PostgreSQL as the database and Docker for easy setup.

## Prerequisites
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/diskrat/veterinary-clinic.git
   cd veterinary-clinic
   ```

2. **Configure environment variables:**
   - Copy `.env.sample` to `.env` and adjust values if needed:
     ```bash
     cp .env.sample .env
     ```

3. **Build and run the containers:**
   ```bash
   docker-compose up --build
   ```
   This will start both the PostgreSQL database and the FastAPI application.

4. **Access the API docs:**
   - Open [http://localhost:8000/docs](http://localhost:8000/docs) in your browser for interactive documentation (Swagger UI).

## Useful Commands
- **Stop the containers:**
  ```bash
  docker-compose down
  ```
- **Rebuild the containers after code changes:**
  ```bash
  docker-compose up --build
  ```

## Database
- Data is persisted in a Docker volume (`pgdata`).
- You can connect to the database using any PostgreSQL client with the credentials in your `.env` file.

## Migrations
- Alembic is used for database migrations. To run migrations manually:
  ```bash
  docker-compose exec app alembic upgrade head
  ```

## Troubleshooting
- Make sure ports 5432 (Postgres) and 8000 (API) are free on your machine.
- Check `.env` for correct database credentials.
- Use `docker-compose logs` to view container logs for debugging.

