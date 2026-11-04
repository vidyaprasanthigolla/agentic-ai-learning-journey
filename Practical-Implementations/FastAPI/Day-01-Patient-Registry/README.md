# Day 01 – Patient Registration System using FastAPI

**Date:** November 4, 2026

## Project Overview
Developed a simple Patient Registration System using FastAPI, Python, HTML, JavaScript, and JSON file storage.

The application allows users to register patients by entering their name and age.

## Technologies Used
- Python
- FastAPI
- Pydantic
- HTML
- JavaScript
- JSON
- Uvicorn

## Concepts Learned
1. Creating REST API endpoints using FastAPI.
2. Handling GET and POST requests.
3. Validating request data using Pydantic models.
4. Reading and writing JSON files in Python.
5. Serving HTML pages using FileResponse.
6. Connecting frontend and backend using JavaScript Fetch API.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Displays homepage |
| GET | `/form-page` | Displays patient registration form |
| POST | `/submit-data` | Saves patient information |

## Project Workflow
1. User opens the homepage.
2. User navigates to the registration form.
3. User enters their name and age.
4. JavaScript sends a POST request to FastAPI.
5. Pydantic validates the submitted data.
6. Patient information is stored in `patients.json`.
7. A success message is displayed.

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
uvicorn main:app --reload
```

Open:

`http://127.0.0.1:8000`

API documentation:

`http://127.0.0.1:8000/docs`

## Key Learnings
- Understood FastAPI fundamentals.
- Learned how Pydantic validates API requests.
- Practiced JSON file handling.
- Connected HTML forms with a Python backend.

## Future Improvements
- Add patient search functionality.
- Implement update and delete operations.
- Integrate SQLite or MySQL.
- Improve validation and error handling.