# GreatKart - Django E-Commerce Application

GreatKart is a **full-featured e-commerce web application (Server-Rendered)** built with
**Django**, enabling users to browse products, manage their cart, place
orders, and manage accounts. Admins can manage products, categories, and
orders through the Django admin panel. 


## Project Structure
GreatKart-Django-E-Commerce/

   ├── accounts/ # User authentication, registration, profiles

   ├── carts/ # Shopping cart models and logic

   ├── category/ # Product categories

   ├── store/ # Product listing, product details

   ├── greatkart/ # Main project settings (settings.py, urls.py, wsgi.py)

   ├── templates/ # HTML templates for frontend (Server-Rendered)

   ├── static/ # CSS, JS, and images

   ├── manage.py # Django project management

   ├── requirements.txt # Python dependencies

   └── .gitignore # Git ignore rules


---


## Features

### User Features
- User registration, login, logout
- Profile management
- Browse products by categories
- Add, update, and remove products in the shopping cart
- Checkout and place orders
- View order history

### Admin Features
- Manage products, categories, and users
- View and manage orders via Django admin panel
- Access statistics (future improvements can include dashboard analytics)

---

## Tech Stack

- **Backend:** Django 4.x, Python 3.x
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default, can switch to PostgreSQL/MySQL)
- **Template Engine:** Django Templates
- **Dependencies:** See `requirements.txt`

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Jayeshm93/GreatKart-Django-E-Commerce.git
   cd GreatKart-Django-E-Commerce


2. **Create a Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate   # macOS/Linux
   # On Windows:
   # env\Scripts\activate

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

4. **Apply Database Migrations**
   ```bash
   python manage.py migrate

5. **Create Superuser (Admin)**
   ```bash
   python manage.py createsuperuser

6. **Run collectstatic**
   ```bash
   python manage.py collectstatic 
   
7. **Run Development Server**
   ```bash
   python manage.py runserver

8. **Access the App**
   ```bash
   # Frontend
   http://127.0.0.1:8000/
   
   # Admin panel
    http://127.0.0.1:8000/admin/

---

## Live Demo Link
   ```bash
   https://greatkart-j4lu.onrender.com/

---


## Usage
- Add categories and products through the admin panel.
- Users can register and login. 
- Users can browse products and add items to the cart. 
- Checkout and place orders to see order details. 
- Admin can view and manage orders and products.


---

## Future Improvements
- Payment gateway integration
- Order email notifications 
- Admin dashboard with analytics


---






