# My FastAPI App

## Overview
This project is a FastAPI application that implements a RESTful API with JWT authentication and SQLAlchemy for database management. It includes a seeded database with fake data for testing purposes.

## API Key
To access the API, you will need an API key. Please ensure you have the key stored securely in your `.env` file.

## Features
- JWT Authentication: Secure your API endpoints with JSON Web Tokens.
- SQLAlchemy: Manage your database with an ORM.
- Pydantic: Validate and serialize data for requests and responses.
- Seeded Database: Pre-populate the database with fake data for development and testing.

## Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-fastapi-app
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Running the Application
To run the FastAPI application, use the following command:
```
uvicorn src.main:app --reload
```

### API Documentation
Once the application is running, you can access the interactive API documentation at:
```
http://127.0.0.1:8000/docs
```

### Endpoints
Refer to the `docs/API_EXPLANATION.md` file for detailed information about the available API endpoints, request/response formats, and usage examples.

## License
This project is licensed under the MIT License.