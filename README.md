
# ACEest Fitness & Gym — Automated CI/CD Pipeline

## 1. Project Overview

ACEest Fitness & Gym is a simple Flask-based REST API developed to demonstrate DevOps practices, including Git version control, automated testing, Docker containerization, and continuous integration using GitHub Actions and Jenkins.

The application supports basic gym member management operations.

## 2. Technologies Used

- Python 3.9
- Flask
- Pytest
- Flake8
- Git and GitHub
- Docker
- GitHub Actions
- Jenkins

## 3. Project Structure

```text
aceest-devops/
├── .github/
│   └── workflows/
│       └── main.yml
├── tests/
│   └── test_app.py
├── The code versions for DevOps Assignment/
│   └── Original supplied Python versions
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## 4. Application Features

- Welcome endpoint to verify that the API is running.
- Health-check endpoint.
- Retrieve all gym members.
- Add a gym member with a name and membership plan.
- Validate invalid or incomplete requests.
- Return appropriate HTTP status codes.

### API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/health` | Health status |
| GET | `/members` | Retrieve members |
| POST | `/members` | Add a member |

### Example Request

```json
{
  "name": "Chaitanya",
  "plan": "Premium"
}
```

A successful member creation returns HTTP `201 Created`.

**Note:** Member data is stored in memory and is not persisted after the application restarts.

## 5. Run Locally

Clone the repository:

```bash
git clone https://github.com/ChaitanyaKarthik-BITS-2025tm03105/aceest-devops.git
cd aceest-devops
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
python app.py
```

The API runs at `http://localhost:5000`.

## 6. Automated Testing

Run the tests locally:

```bash
python -m pytest -v
```

The test suite covers successful requests, health checks, member creation, and invalid input validation.

## 7. Docker Instructions

Build the Docker image:

```bash
docker build -t aceest-fitness:1.0 .
```

Run the application:

```bash
docker run --rm -p 5000:5000 aceest-fitness:1.0
```

Test the health endpoint:

```bash
curl http://localhost:5000/health
```

Run the tests inside the Docker container:

```bash
docker run --rm --entrypoint python aceest-fitness:1.0 -m pytest -v
```

## 8. GitHub Actions CI Pipeline

The workflow is defined in `.github/workflows/main.yml`.

It runs automatically on pushes and pull requests.

Pipeline stages:

1. **Checkout:** Retrieves the repository source code.
2. **Build and lint:** Sets up Python, installs dependencies, compiles Python files, and checks code style with Flake8.
3. **Docker image assembly:** Builds the application Docker image.
4. **Automated testing:** Executes the Pytest suite inside the Docker container.

A successful workflow confirms that the linting, image build, and automated tests have passed.

## 9. Jenkins CI

Jenkins can be configured to pull this GitHub repository and execute a clean build.

Recommended job configuration:

1. Create a Jenkins Pipeline job.
2. Configure the Git repository URL.
3. Select the `main` branch.
4. Configure the job to check out the source and execute the required build, lint, Docker, and test commands.
5. Review the console output to verify the build result.

The Jenkins job requires Python, Git, Docker, and the necessary permissions on the Jenkins execution environment.

## 10. Assumptions and Limitations

- The application uses in-memory storage instead of a database.
- Member data resets when the application restarts.
- The application is intended as a DevOps assignment demonstration, not a production-ready gym management system.
- Jenkins configuration depends on the available Jenkins environment.

## 11. Repository

GitHub: https://github.com/ChaitanyaKarthik-BITS-2025tm03105/aceest-devops
