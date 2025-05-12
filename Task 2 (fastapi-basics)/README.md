# FastAPI Basics

This project is designed to help you learn the basics of FastAPI by building simple web APIs. It includes creating basic GET routes, handling path parameters, and query parameters.

## Project Overview

The project provides the following two basic endpoints:
1. **GET `/`**: Returns a greeting message.
2. **GET `/items/{item_id}`**: Takes a path parameter `item_id` and an optional query parameter `query`, then returns them in a JSON response.

---

## Installation Guide

### Step 1: Install `uv` (Universal Virtual Environment)

First, install `uv` (a tool for managing Python environments). Run the following command in **PowerShell** (for Windows):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

This will install the `uv` tool, which simplifies managing Python environments and dependencies.

---

### Step 2: Create a Project Directory and Navigate to It

1. **Create the Project Directory**:

   ```bash
   uv init fastapi-basics
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd fastapi-basics
   ```

---

### Step 3: Create and Activate the Virtual Environment

1. **Create the Virtual Environment**:

   ```bash
   uv venv
   ```

2. **Activate the Virtual Environment**:
   On **Windows**, activate the virtual environment using:

   ```bash
   .venv\Scripts\activate
   ```

---

### Step 4: Install Dependencies

1. **Install FastAPI and Uvicorn** (ASGI server):

   ```bash
   uv add "fastapi[standard]"
   ```

2. **Install Development Dependencies** for testing (e.g., `pytest` and `pytest-asyncio`):

   ```bash
   uv add --dev pytest pytest-asyncio
   ```

After running the above commands, the `pyproject.toml` file will be updated with the following content:

```toml
[project]
name = "fastapi-basics"
version = "0.1.0"
description = "FastAPI project for learning HTTP routes and parameters."
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "fastapi[standard]>=0.115.12",
]

[dependency-groups]
dev = [
    "pytest>=8.3.5",
    "pytest-asyncio>=0.26.0",
]
```

---

### Step 5: Run the FastAPI Application

1. **Start the FastAPI Development Server** with `uvicorn`:

   ```bash
   uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

   * **Explanation**:

     * `main:app` specifies the location of the FastAPI instance.
     * `--reload` enables automatic reloading for development.

2. Alternatively, if you have the `fastapi` CLI available, you can run it with the following command:

   ```bash
   fastapi dev main.py
   ```

   This will run the FastAPI application in development mode.

---

### API Endpoints

#### 1. **GET `/`** - Root Endpoint

* **Description**: Returns a greeting message with your name.
* **Request**: `GET http://localhost:8000/`
* **Response**:

  ```json
  {
    "Hello": "Muhammad Mubashir Saeedi"
  }
  ```

#### 2. **GET `/items/{item_id}`** - Item Endpoint

* **Description**: Takes an `item_id` (integer) as a path parameter and an optional `query` (string) as a query parameter.
* **Path Parameter**:

  * `item_id` (int): The ID of the item.
* **Query Parameter** (optional):

  * `query` (str): Optional query string.
* **Example Request**:

  ```http
  GET http://localhost:8000/items/5?query=test
  ```
* **Response**:

  ```json
  {
    "item_id": 5,
    "query": "test"
  }
  ```

#### Request Without `query`:

```http
GET http://localhost:8000/items/7
```

**Response**:

```json
{
  "item_id": 7,
  "query": null
}
```

---

### Testing the API

You can test the API by navigating to the following URLs:

* **Root Endpoint**: `http://localhost:8000/`
* **Item Endpoint**: `http://localhost:8000/items/{item_id}?query={query}`

#### Interactive API Documentation

FastAPI automatically generates interactive API documentation that you can use to test and explore the API:

* **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
* **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

These interactive tools allow you to test API endpoints directly from the browser.

---

### Project Structure

* **main.py**: Contains the FastAPI application and route definitions.
* **README.md**: Project description and setup instructions.
* **pyproject.toml**: Python project configuration and dependencies.

---

## Conclusion

This is a simple FastAPI project designed to teach you the basics of API development using FastAPI. You learned how to set up a project, define basic routes, and interact with your API using path and query parameters.

---
