# Task 1: Flask Backend API for Task Comments (CRUD)

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/) 
[![Flask](https://img.shields.io/badge/Flask-2.3-brightgreen)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-orange)](https://www.sqlite.org/index.html)

---

## **Project Overview**

This project is a **Flask backend API** for managing comments on tasks. It is part of a coding assessment for **Better Software (Associate Software Engineer – Python/React)**. The backend allows you to **add, update, delete, and retrieve comments** for a given task using proper **CRUD principles**, along with automated tests to verify functionality.

---

## **Features**

- **Create Comment**: Add a new comment to a task.
- **Read Comments**: Fetch all comments for a specific task.
- **Update Comment**: Modify the content of an existing comment.
- **Delete Comment**: Remove a comment from a task.
- **Automated Tests**: `pytest` tests for each API endpoint.

---

## **Technologies Used**

- **Backend:** Python 3.11, Flask
- **Database:** SQLite (lightweight file-based database)
- **Testing:** pytest
- **Version Control:** Git & GitHub

---
flask_task_api/
│
├─ app.py # Main Flask application
├─ routes.py # API routes (CRUD operations)
├─ models.py # SQLAlchemy models for Task & Comment
├─ tests.py # Pytest unit tests for APIs
├─ requirements.txt # Python dependencies
└─ README.md # Project documentation


---

## **API Endpoints**

### **1. Create Comment**
POST /tasks/<task_id>/comments
**Request Body:**
```json
{
  "content": "Your comment here"
}

{
  "id": 1,
  "content": "Your comment here",
  "created_at": "2025-11-29T21:00:00"
}

GET /tasks/<task_id>/comments

## **Project Structure**

