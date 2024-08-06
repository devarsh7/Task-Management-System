# Task-Management-System

## Overview
This is a simple Task Management System which is a web application designed to streamline task management processes. It is developed in Python using Django framework and uses SQLite database, which provides users with a robust platform to create, update, and manage tasks efficiently. The system includes REST API endpoints for seamless integration, a user-friendly dashboard and user authentication.

## Dashboard
Here is a screenshot of the dashboard that I have designed for the user.

![image](https://github.com/user-attachments/assets/3cf7b654-392e-438f-9fea-190f59e2dbad)

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

## Docker Setup

  ### Build Docker
  
- docker-compose build

### Run the docker containers

- docker-compose up

## REST API Endpoints
 ### To perform operations on Tasks
 
1. ### To Create a new task
  
- Endpoint: POST /api/tasks/
- Description: Creates a new task with the provided details.
- Request Body: A JSON object containing the task details (title, description, status, due date).
- Response: Returns the created task object with its assigned ID.
  
2. ### To Retrieve all tasks

- Endpoint: GET /api/tasks/
- Description: Retrieves a list of all tasks.
- Response: Returns a JSON array of task objects, each containing task details such as ID, title, description, status, and due date.
  
3. ### To Retrieve a task by ID

- Endpoint: GET /api/tasks/<id>/
- Description: Retrieves details of a specific task by its ID.
- Response: Returns a JSON object with the task details.

4. ### To Update a task

- Endpoint: PUT /api/tasks/<id>/
- Description: Updates the details of an existing task by its ID.
- Request Body: A JSON object containing the updated task details (title, description, status, due date).
- Response: Returns the updated task object.
  
5. ### To Delete a task

- Endpoint: DELETE /api/tasks/<id>/
- Description: Deletes a specific task by its ID.
- Response: Returns a success message upon successful deletion.

 ### For registeration of users 

6. ### Register a new user

- Endpoint: POST /api/users/
- Description: Registers a new user with the provided details.
- Request Body: A JSON object containing the user details (username, email, password).
- Response: Returns the created user object with its assigned ID.

7. ### Login a user

- Endpoint: POST /api/users/login/
- Description: Authenticates a user and provides a token for accessing protected endpoints.
- Request Body: A JSON object containing the login details (username, password).
- Response: Returns a token upon successful authentication.

## License

- This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

- For any issues or queries, please contact Devarsh Shah at devarsh.shahs07@gmail.com.



