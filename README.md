# Fast_API_App
# FastAPI Task Manager

This repository contains a simple task management API built using [FastAPI](https://fastapi.tiangolo.com/). The API allows you to create, read, update, and delete tasks. Each task has a unique identifier, title, description, and a status indicating whether it has been completed.

## Features

- **Create Task**: Add a new task with a title, optional description, and completion status.
- **Read Tasks**: Retrieve a list of all tasks.
- **Read Single Task**: Retrieve a specific task by its unique ID.
- **Update Task**: Modify an existing task's title, description, or completion status.
- **Delete Task**: Remove a task by its unique ID.

## Project Structure

- **main.py**: The main application file that contains the FastAPI app and all route definitions.

## Endpoints

### Create a Task

- **POST /tasks/**
- Request Body:
  ```json
  {
    "title": "Task Title",
    "description": "Optional task description",
    "completed": false
  }
Getting Started
Prerequisites
** Python 3.8+
** FastAPI
** Uvicorn
## installation
 ``git clone https://github.com/RkanGen/fastapi_App.git ``<br>
 ``cd fastapi_App ``<br>
# Install the dependencies:
 ``pip install fastapi uvicorn``<br>
**Running the Application**<br>
`` uvicorn main:app --reload ``


