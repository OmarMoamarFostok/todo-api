# 📝 ToDo API with Django REST Framework

A simple task management (ToDo) REST API built using Django REST Framework, featuring user authentication via JWT, full CRUD for tasks, and advanced **Scatter/Gather** batch operations.

---

## 📌 Features

- ✅ User registration and login (with JWT tokens)
- ✅ CRUD operations on personal ToDos
- ✅ Token authentication
- ✅ Protection: users can access only their own tasks
- ✅ Scatter & Gather
- ✅ Interactive API docs via Swagger UI

---

## 🛠️ Tech Stack

- Python 3.x
- Django
- Django REST Framework
- SQLite (or PostgreSQL optional)
- JWT Auth (`djangorestframework-simplejwt`)
- Swagger (`drf-yasg`)
- Pipenv for environment management

---

## 🚀 How to Run

```bash
git clone https://github.com/OmarMoamarFostok/todo-api.git
cd todo_api_project
pipenv install
pipenv shell
python manage.py migrate
python manage.py runserver
