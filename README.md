# Django CI/CD AWS Deployment Demo

A minimal containerized Django application with automated CI/CD pipeline for AWS deployment.

## Project Structure

```
django_aws/
├── .github/
│   └── workflows/
│       └── deploy.yml          # Coming in next step
├── backend/                  # Django project
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                      # Django app
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── templates/
│   └── home.html
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── README.md
```

## Local Development Setup

### Prerequisites
- Python 3.11+
- Docker and Docker Compose
- Git

### Step 1: Clone and Setup Virtual Environment

```bash
# Clone the repository
git clone <your-repo-url>
cd django-aws-cicd

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Run Locally (Without Docker)

```bash
# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

Visit http://localhost:8000 to see your app!

### Step 3: Run with Docker

```bash
# Build the Docker image
docker build -t django-app .

# Run with docker-compose
docker-compose up -d

# View logs
docker-compose logs -f

# Stop containers
docker-compose down
```

Visit http://localhost to see your containerized app!

## Application Endpoints

- `/` - Homepage
- `/health/` - Health check endpoint (returns JSON)
- `/admin/` - Django admin panel

## Testing the Application

```bash
# Test health endpoint
curl http://localhost/health/

# Expected response:
# {"status": "healthy", "hostname": "container_id"}
```

## Environment Variables

Create a `.env` file for local development:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
```

For production (AWS), these will be set in the docker-compose file or EC2.

## Next Steps

1. ✅ Django application created
2. ⏳ AWS infrastructure setup (EC2, ECR, IAM)
3. ⏳ GitHub Actions CI/CD pipeline
4. ⏳ Deployment automation

## Docker Commands Reference

```bash
# Build image
docker build -t django-app .

# Run container
docker run -p 8000:8000 django-app

# View running containers
docker ps

# View logs
docker logs <container_id>

# Stop container
docker stop <container_id>

# Remove container
docker rm <container_id>
```

## Useful Django Commands

```bash
# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run tests
python manage.py test
```

## Troubleshooting

**Port already in use:**
```bash
# Find process using port 8000
lsof -i :8000
# Kill the process
kill -9 <PID>
```

**Docker permission denied:**
```bash
# Add user to docker group (Linux)
sudo usermod -aG docker $USER
# Logout and login again
```

## License

MIT