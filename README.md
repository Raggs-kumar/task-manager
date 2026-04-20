# 🚀 Task Manager App

A full-stack Task Manager application built with:

* **Frontend:** React (Vite + TypeScript)
* **Backend:** FastAPI (Python)
* **Database:** SQLite (can be upgraded to PostgreSQL)
* **Auth:** JWT-based authentication

---

## 📌 Project Overview

This application allows users to:

* Register and login securely
* Create, update, and delete tasks
* Mark tasks as completed or pending
* Filter tasks based on status

It demonstrates a complete **frontend + backend integration** using modern technologies.

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Raggs-kumar/task-manager.git
cd task-manager
```

---

### 2. Backend Setup (FastAPI)

```bash
cd backend

# create virtual environment
python -m venv venv

# activate (Windows)
venv\Scripts\activate

# install dependencies
pip install -r requirements.txt
```

---

### 3. Frontend Setup (React)

```bash
cd taskflow-buddy

# install dependencies
npm install
```

---

## 🔐 Environment Variables

Create a `.env` file in the **backend** folder:

```env
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## ▶️ How to Run Locally

### Run Backend

```bash
cd backend
python -m uvicorn main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

### Run Frontend

```bash
cd taskflow-buddy
npm run dev
```

Frontend runs at:

```
http://localhost:8081
```

---

## 🌐 API Integration

Frontend connects to backend via:

```
http://127.0.0.1:8000
```

Make sure CORS is enabled in FastAPI.

---

## 📦 requirements.txt

Create this file inside `backend/`:

```txt
fastapi
uvicorn
sqlalchemy
pydantic
python-jose
passlib[bcrypt]
bcrypt
```

---

## 🚀 Deployment

🔗 Deployment Link: *(Add after hosting)*

You can deploy using:

* Frontend: Vercel / Netlify
* Backend: Render / Railway

---

## 📁 Project Structure

```
task-manager/
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── auth.py
│   └── routes/
│
├── taskflow-buddy/
│   ├── src/
│   ├── components/
│   ├── routes/
│   └── lib/
│
└── README.md
```

---

## ✨ Features

* JWT Authentication 🔐
* CRUD Operations for Tasks 📋
* Task Filtering (Pending / Completed) 🎯
* Responsive UI ⚡
* Full-stack integration 🌐

---

## 🧑‍💻 Author

**Ragavan Kumar**

---

## ⭐ Future Improvements

* Add task deadlines & reminders
* Use PostgreSQL database
* Deploy with Docker
* Add role-based access

---
