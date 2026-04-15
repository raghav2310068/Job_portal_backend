# 🧑‍💼 Job Portal Backend (Django + DRF)

A simple backend project built using Django and Django REST Framework that allows recruiters to create and manage job listings.

This project focuses on backend fundamentals like authentication logic, API design, role-based access, and deployment.

---

## 🚀 Features

* Custom user login & registration (without Django auth system)
* Role-based access (only recruiter can create jobs)
* Job CRUD APIs (Create, Read, Update, Delete)
* Ownership protection (users can only modify their own jobs)
* Session-based authentication (learning purpose)
* Django REST Framework browsable API UI
* Deployed on cloud (Render)

---

## 🧠 How it Works

* User registers and logs in
* Session stores the logged-in user ID
* On API request:

  * System checks if user is logged in
  * Verifies if user is a recruiter
  * Allows job creation/update/delete accordingly
* Each job is linked to the creator

---

## 📌 API Endpoints

### 🔹 Jobs

| Method | Endpoint          | Description                 |
| ------ | ----------------- | --------------------------- |
| GET    | `/api/jobs/`      | Get all jobs                |
| POST   | `/api/jobs/`      | Create job (recruiter only) |
| GET    | `/api/jobs/<id>/` | Get single job              |
| PUT    | `/api/jobs/<id>/` | Update own job              |
| DELETE | `/api/jobs/<id>/` | Delete own job              |

---

## 🔐 Access Control

* Only logged-in users can create jobs
* Only recruiter role is allowed
* Users can only edit/delete their own jobs

---

## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework
* SQLite (dev)
* Gunicorn
* Whitenoise (static files)
* Render (deployment)

---

## 🌐 Live Demo

👉 https://your-app.onrender.com/api/jobs/

---

## ⚙️ Setup (Local)

```bash
git clone <your-repo-url>
cd job-portal-backend

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

---

## 📦 Environment Variables

Create a `.env` file:

```
SECRET_KEY=your-secret-key
```

---

## 📁 Project Structure

```
accounts/   → user logic
api/        → job APIs
project/    → main settings
```

---

## 💡 Future Improvements

* JWT Authentication
* Job search & filtering
* Pagination
* PostgreSQL integration
* Frontend integration (React)

---

## 🤝 Author

Made by Raghav 🚀
Learning backend development step by step.
