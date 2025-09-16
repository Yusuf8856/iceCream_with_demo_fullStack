# 🍦 Yusuf Ice Cream Website

A Django-based web application for **Yusuf Ice Cream**, featuring cakes, softies, ice creams, and contact forms with WhatsApp & email integration.  
This project is built to demonstrate a **modern responsive design** with multiple product pages.

---

## 🚀 Features
- ✅ Home page with modern UI/UX  
- ✅ About page with attractive thumbnails  
- ✅ Services page (Ice Cream delivery, Custom flavors, Event catering, etc.)  
- ✅ Product pages:
  - 🍰 Cakes (`cake.html`)
  - 🍦 Softies (`softy.html`)
  - 🍨 Ice Creams (`icecream.html`)  
- ✅ WhatsApp integration for direct ordering  
- ✅ Contact form with email support  
- ✅ Admin panel to manage messages  

---

## 📂 Project Structure
## 📂 Project Structure

yusuficecream/             # Main Django Project Root
│── hello/                 # Project settings folder
│   │── __init__.py
│   │── asgi.py
│   │── settings.py        # Django settings
│   │── urls.py            # Project URLs
│   │── wsgi.py
│
│── home/                  # Django app (ice cream website)
│   │── migrations/
│   │── static/            # Static files (CSS, JS, Images)
│   │── templates/         # HTML templates (home, cake, softy, icecream, contact, etc.)
│   │── admin.py
│   │── apps.py
│   │── models.py          # Database models
│   │── urls.py            # App URLs
│   │── views.py           # App views
│
│── static/                # Global static files
│── templates/             # Global templates (base.html, footer, navbar, etc.)
│── db.sqlite3             # Default database
│── manage.py              # Django management script
│── requirements.txt       # Project dependencies
│── README.md              # Project documentation
