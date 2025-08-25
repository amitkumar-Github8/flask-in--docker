
# Flask in Docker

This project demonstrates a minimal Flask application running inside a Docker container.

## Project Structure

- `app.py`: Simple Flask app with a single route (`/`).
- `Dockerfile`: Instructions to build the Docker image.
- `requirements.txt`: Python dependencies (Flask).
- `.dockerignore`: (Recommended) Ignore files/folders from Docker build context.

## Getting Started

### Prerequisites
- Docker installed on your system

### Build the Docker Image
```bash
docker build -t flask-in-docker .
```

### Run the Container
```bash
docker run -p 5000:5000 flask-in-docker
```

Visit [http://localhost:5000](http://localhost:5000) in your browser. You should see:
```
Hello from Flask in Docker!
```

## Development

To run locally without Docker:
```bash
pip install -r requirements.txt
python app.py
```

## Notes
- For production, consider using a WSGI server like Gunicorn.
- Update `.dockerignore` to exclude unnecessary files (e.g., `__pycache__/`, `.git/`).
