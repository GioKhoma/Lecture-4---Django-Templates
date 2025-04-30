# 🧱 Django Sidebar Profile App

This is a simple Django web project with:

✅ A reusable base template and sidebar navigation  
✅ A custom Profile model managed via Django admin  
✅ Dynamic pages for Home, About, Posts, and Profile List  
✅ Use of {% extends %}, {% include %}, {% for %}, {% if %}, and static files  
✅ Visual user blocks (avatars with initials or icons)  

## 📁 Project Structure

templates_project/  
├── templates_app/  
│   ├── templates/  
│   │   └── templates_app/  
│   │       ├── base.html  
│   │       ├── home.html  
│   │       ├── about.html  
│   │       ├── posts.html  
│   │       └── profiles.html  
│   ├── static/  
│   │   └── templates_app/  
│   │       └── css/  
│   │           └── style.css  
│   ├── models.py  
│   ├── views.py  
│   ├── urls.py  
│   └── admin.py  
└── manage.py

## 🚀 Setup Instructions

Clone this repository:

git clone https://github.com/GioKhoma/Lecture-4---Django-Templates

Create and activate a virtual environment:

python -m venv env  
source env/bin/activate    # Windows: env\Scripts\activate

Install dependencies:

pip install django

Run migrations:

python manage.py makemigrations  
python manage.py migrate

Create a superuser:

python manage.py createsuperuser

Start the development server:

python manage.py runserver

Then go to: http://127.0.0.1:8000/

## 🛠 Features

🔁 Template inheritance with {% extends %}  
🔗 Reusable blocks with {% include %}  
🎨 Centralized styling with style.css  
🧍 Profile model rendered dynamically  
👤 Emoji/initial avatars instead of image uploads  
👨‍💼 Admin panel integration

## ✍️ Author

Made with ❤️ using Django.  
Feel free to fork, remix, and improve.

## 📃 License

MIT License — use freely for personal or commercial projects.
