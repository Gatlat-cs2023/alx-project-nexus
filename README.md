# Job Board Backend

# 🧰 Job Board Backend API

This is the backend REST API for a Job Board Platform built with **Django** and **PostgreSQL**, featuring:

- Job posting & filtering
- Role-based authentication
- Job application system
- JWT Auth
- API documentation via Swagger

---

## 🚀 Features

- ✅ Post and filter job listings
- ✅ Apply to jobs (authenticated users)
- ✅ Admin dashboard for job management
- ✅ Role-based permissions
- ✅ JWT Authentication
- ✅ Swagger & ReDoc API docs

---

## 🛠️ Tech Stack

| Layer            | Technology       |
|------------------|------------------|
| Backend Framework | Django REST Framework |
| Database         | PostgreSQL       |
| Auth             | JWT (SimpleJWT)  |
| Docs             | Swagger (drf-yasg) |
| DevOps           | Pipenv or venv + PostgreSQL |
| ORM              | Django ORM       |

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/job-board-backend.git
cd job-board-backend
```

### 2. Create a virtual environment and activate it

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup PostgreSQL database
Create a PostgreSQL database and set the following in `.env` file:

```ini
SECRET_KEY=secret-key
DEBUG=True

DB_NAME=db_name
DB_USER=db_user
DB_PASSWORD=db_password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

---

## 🔐 Authentication

- Uses JWT Auth (`/api/token/`, `/api/token/refresh/`)
- Include token in headers as:

```h
Authorization: Bearer <your_access_token>
```

---

## 📂 API Endpoints

| Feature           | Endpoint             | Method | Auth Required |
| ----------------- | -------------------- | ------ | ------------- |
| List Jobs         | `/api/jobs/`         | GET    | ❌             |
| Create Job        | `/api/jobs/`         | POST   | ✅ Admin only  |
| Apply to Job      | `/api/applications/` | POST   | ✅             |
| List Applications | `/api/applications/` | GET    | ✅ Admin/User  |

---

## 📑 API Documentation

available at:
- [Swagger UI](http://localhost:8000/api/docs/)
- [ReDoc](http://localhost:8000/api/redoc/)

---

## ✅ Git Commit Workflow
```bash
# Initial Setup
feat: set up Django project with PostgreSQL

# Feature Development
feat: implement job posting and filtering APIs
feat: add role-based authentication for admins and users

# Optimization
perf: optimize job search queries with indexing

# Documentation
feat: integrate Swagger for API documentation
docs: update README with usage details
```

---

## ✍️ Contributing

Pull requests are welcome. For major changes, please open an issue first.
