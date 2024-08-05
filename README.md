# Task-Management-System

## Overview
This is a simple Task Management System which is a web application designed to streamline task management processes. It is developed in Python using Django framework and uses SQLite database, which provides users with a robust platform to create, update, and manage tasks efficiently. The system includes REST API endpoints for seamless integration, a user-friendly dashboard and user authentication.

## Features
- **User Authentication**: Secure authentication system with registration and login functionality.
- **Dashboard**: Dashboard displaying tasks with their statuses, deadlines, users and logout option.
- **CRUD Operations**: Full support for Create, Read, Update, and Delete operations on tasks.
- **Containerization**: Docker support for consistent deployment and development environments.
  
## Technologies Used
- **Backend**: Django (Python)
- **Database**: SQLite
- **Frontend**: Django Templates (HTML, CSS, JavaScript)
- **APIs**: RESTful API
- **Containerization**: Docker

## Installation and Setup

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.8 or higher
- Django 3.2 or higher
- SQLite
- Docker
- Docker Compose

### Installation Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/devarsh7/Task-Management-System.git
   cd Task-Management-System

2. ### Create and Activate a virtual Environment
- python -m venv newenv
- source newenv/bin/activate  # On Windows use `newenv\Scripts\activate`

3. ### Install required Packages
- pip install -r requirements.txt

4. ### Database Migrations
- python manage.py migrate

5. ### Create a Superuser
- python manage.py createsuperuser

6. ### Run the development server
- python manage.py runserver

7. ### Access the application
- Click on 'http://127.0.0.1:8000' to navigate to browser

