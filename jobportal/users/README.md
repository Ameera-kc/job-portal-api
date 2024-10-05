This is a RESTful API built with Django REST Framework (DRF) that manages job listings, applications, and user roles (Candidates, Employers, Admins). The API features JWT authentication and role-based access control.

Features

1.User registration with roles (Candidate, Employer)
2.JWT-based authentication and role-based access control
3.CRUD operations for job listings and applications
4.Search and filter job listings
5.File upload (resume) for job applications

Requirements

1.Python 3.12+
2.Django 5.1+
3.Django REST Framework
4.Simple JWT (for JWT Authentication)
5.PostgreSQL (optional, can be SQLite for development)

Setup Instructions

git clone <repository-url>
cd jobportal

virtualenv

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

dependencies

pip install -r requirements.txt

env variables

SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=your_database_url  # If using PostgreSQL or other databases

migrations 

python manage.py migrate

superuser

python manage.py createsuperuser

run server

python manage.py runserver

JWT Token Endpoint

POST /auth/jwt/create/

Request body:
json

{
  "username": "your_username",
  "password": "your_password"
}