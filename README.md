
# School Management System API

A RESTful API built with **Django REST Framework** and **MySQL** to manage schools, students, and teachers.

---

##  Features

-  CRUD APIs for School, Student, and Teacher models  
-  MySQL database integration  
-  DRF-based serializers and viewsets  
-  JWT authentication  
-   Pagination and searching 
---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/adarsha1426/school-management-api.git
cd school-management-api
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
Windows: venv\Scripts\activate
Other OS: source venv/bin/activate  
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure MySQL Database
Update your `settings.py` :
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Database_Name',
        'USER': 'User',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
Then run:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5. Run the Server
```bash
python manage.py runserver
```

---
---

## API Endpoints

###  School
- `GET /api/schools/` – List all schools  
- `POST /api/schools/` – Add a new school  
- `PUT /api/schools/{id}/` – Update a school  
- `DELETE /api/schools/{id}/` – Delete a school  

### Student
- `GET /api/students/` – List all students  
- `POST /api/students/` – Add a new student  
- `PUT /api/students/{id}/` – Update a student  
- `DELETE /api/students/{id}/` – Delete a student  

### Teacher
- `GET /api/teachers/` – List all teachers  
- `POST /api/teachers/` – Add a new teacher  
- `PUT /api/teachers/{id}/` – Update a teacher  
- `DELETE /api/teachers/{id}/` – Delete a teacher  

---
---

