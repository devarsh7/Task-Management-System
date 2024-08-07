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
- python manage.py makemigrations
- python manage.py sqlmigrate
- python manage.py migrate

5. ### Create a Superuser (Here I have already created one)
- Username: devarsh
- Password: admin123
- python manage.py createsuperuser (no need for this as I have created already)

6. ### Run the development server
- python manage.py runserver

7. ### Access the application
- Click on 'http://127.0.0.1:8000' to navigate to browser

## Deploy application using Docker

  ### Build Docker
  
- docker-compose build

### Run the docker containers

- docker-compose up

## REST API Endpoints
 ### To perform operations on Tasks
 
1. ### To Create a new task
  
- Endpoint: http://127.0.0.1:8000/api/tasks/?Content-Type=application/json
- Description: Creates a new task with the provided details.
- Request Body: A JSON object containing the task details (title, description, status, due date).
- Response: Returns the created task object with its assigned ID.

![image](https://github.com/user-attachments/assets/7e1144d1-9d2e-4f4f-a81e-2e84c8f2b7fa)

  
2. ### To Retrieve all tasks

- Endpoint: http://127.0.0.1:8000/api/tasks/
- Description: Retrieves a list of all tasks.
- Response: Returns a JSON array of task objects, each containing task details such as ID, title, description, status, and due date.
  
![image](https://github.com/user-attachments/assets/124f2ddd-d3a6-4811-bf2a-fad70b5485c3)

  
3. ### To Retrieve a task by ID

- Endpoint: http://127.0.0.1:8000/api/tasks/18/
- Description: Retrieves details of a specific task by its ID.
- Response: Returns a JSON object with the task details.

![image](https://github.com/user-attachments/assets/9388ac92-b757-4880-b00c-dd258e3df18e)


4. ### To Update a task

- Endpoint: http://127.0.0.1:8000/api/tasks/18/
- Description: Updates the details of an existing task by its ID.
- Request Body: A JSON object containing the updated task details (title, description, status, due date).
- Response: Returns the updated task object.
  
![image](https://github.com/user-attachments/assets/d7a46713-ac40-4df9-8788-9622ff0894eb)

  
5. ### To Delete a task

- Endpoint: http://127.0.0.1:8000/api/tasks/18/
- Description: Deletes a specific task by its ID.
- Response: Returns a success message upon successful deletion.
  
![image](https://github.com/user-attachments/assets/cdb66055-938a-4534-a084-baed743a106c)

## JWT Authentication for API endpoints using Postman 
Here are the steps to check JWT authentication using Postman :
  1. ### Obtain a JWT Token
       - Open Postman.
       - Create a new request.
       - Set the request type to **POST**.
       - Enter the URL: http://127.0.0.1:8000/api/token/.
       - Navigate to the "**Body**" tab.
       - Select "**x-www-form-urlencoded**".
       - Add the following key-value pairs:
             **username:** your_username
             **password:** your_password
       - Click "Send".
       - Copy the "access" token from the response.

         ![image](https://github.com/user-attachments/assets/8141834f-c8c8-47b5-b563-d137818ac827)
     
  2. ### Access the protected endpoints using the Access Token
       - Create a new request in Postman.
       - Set the request type to **GET**.
       - Enter the URL: http://127.0.0.1:8000/api/tasks/.
       - Navigate to the "**Authorization**" tab.
       - Select **Bearer Token** from the "**Type**" dropdown.
       - Paste the JWT access token into the "**Token**" field.
       - Click "Send" to make the request.
       - Output/Response: List of tasks in the response.
    
         ![image](https://github.com/user-attachments/assets/182d0e85-58c8-4110-9fbf-f61c5acdc6e6)

  3. ### Refresh the Token
       - Create a new request in Postman.
       - Set the request type to **POST**.
       - Enter the URL: http://127.0.0.1:8000/api/token/refresh/.
       - Navigate to the "**Body**" tab.
       - Select "**x-www-form-urlencoded**".
       - Add the following key-value pair:
           **refresh:** the refresh_token (replace the refresh_token with the refresh token we obtained in Step 1)
       - Click "Send".
       - We will receive a new access token in the response.
    
         ![image](https://github.com/user-attachments/assets/a32180d6-1043-4ad7-8398-d798515a4458)
               
## License

- This project is licensed under the MIT License.

## Contact

- For any issues or queries, please contact Devarsh Shah at devarsh.shahs07@gmail.com.
