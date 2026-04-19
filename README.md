# 📚 Student Result Management System

A complete Django web application for managing student results with CRUD operations, search functionality, analytics dashboard, authentication, export features, and pagination.

## ✨ Features

- ✅ **Authentication System** - Login/Logout functionality
- ✅ **CRUD Operations** - Create, Read, Update, Delete students
- ✅ **Result Management** - Add/view results with automatic grade calculation
- ✅ **Search Functionality** - Search students by name, roll no, or class
- ✅ **Dashboard** - View top students and class-wise statistics
- ✅ **Export Data** - Download students/results as Excel files
- ✅ **Pagination** - 10 students per page
- ✅ **Responsive UI** - Bootstrap 5 design
- ✅ **Admin Panel** - Django admin interface

## 🛠️ Tech Stack

- **Backend:** Django 5.x
- **Database:** SQLite3
- **Frontend:** Bootstrap 5, HTML, CSS
- **Additional:** openpyxl (Excel export), Django Pagination

## 🚀 Installation

### Prerequisites
- Python 3.8+
- pip
- virtualenv

### Step 1: Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/student-result-management.git
cd student-result-management

### **Step 2: Create virtual environment**
# Windows
python -m venv env
env\Scripts\activate

# Mac/Linux
python3 -m venv env
source env/bin/activate

Step 3: Install dependencies
pip install -r requirements.txt

Step 4: Run migrations
python manage.py makemigrations
python manage.py migrate

Step 5: Create superuser
python manage.py createsuperuser

Step 6: Run the server
python manage.py runserver

Step 7: Open browser
http://127.0.0.1:8000/

📊 Sample Login
Username: Ayat
Password: Ayat123@
