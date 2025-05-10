
# Eventopia 🎟️

A full-stack Django web application that allows users to browse, create, and purchase tickets for events.

[Live Site](https://eventopia-4ecefd3eb4a9.herokuapp.com/)

---

## 🔍 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [UX Design](#ux-design)
- [Technologies Used](#technologies-used)
- [Database Models](#database-models)
- [Testing](#testing)
- [Deployment](#deployment)
- [Installation](#installation)
- [Credits](#credits)

---

## 🧭 Overview
Eventopia provides a platform for users to host, discover, and attend events. It includes full CRUD for events, user authentication, Stripe payments, and responsive design.

---

## 💡 Features

### Public Users
- View upcoming and past events
- View event details

### Registered Users
- Register/login/logout
- Create/edit/delete events
- Purchase event tickets
- View profile with ticket history
- Secure checkout with Stripe

---

## 🧑‍🎨 UX Design

### Wireframes
(Wireframes should be restored or replaced with working links)

### UI Notes
- Improved contrast and clear CTAs
- Navigation bar with access to profile/dashboard
- External links open in new tabs

---

## 🛠️ Technologies Used
- Python 3 / Django
- HTML5 / CSS3 / JavaScript
- Bootstrap 5
- Stripe API
- SQLite3 (development)
- Heroku (deployment)
- Git & GitHub

---

## 🧾 Database Models
- `Event`: name, image, date, venue, price, quantity
- `ShoppingCart`: user, event, quantity, total price
- `Payment`: stores Stripe reference
- Related with Django’s `User` model via `ForeignKey`

---

## ✅ Testing

### Manual Testing
Each page and function was manually tested, including:
- Event creation, editing, deletion
- Form validations
- Ticket purchase flow
- URL restriction for non-logged-in users

### Responsive Testing
Tested using:
- [Responsive Design Checker](https://responsivedesignchecker.com)

### Code Validation
- HTML: [W3C Validator](https://validator.w3.org/)
- CSS: [CSS Validator](https://jigsaw.w3.org/css-validator/)
- JavaScript: [JSHint](https://jshint.com)

### Sample Manual Test Case Format:
```
Expected: Clicking 'Buy Ticket' deducts from stock
Testing: Clicked Buy for Event X with 10 tickets
Result: Stock updated to 9
Fix: N/A
```

### Known Issues
- No email confirmation on ticket purchase
- Limited search/filtering for events

---

## 🚀 Deployment

### Hosted On: Heroku

#### Steps:
1. Clone the repo:
```bash
git clone https://github.com/deanwraith24/ems.git
cd ems
```
2. Create `.env` file:
```bash
DEBUG=False
SECRET_KEY=your-secret-key
STRIPE_PUBLIC_KEY=your-stripe-key
STRIPE_SECRET_KEY=your-stripe-secret
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run migrations:
```bash
python manage.py migrate
```
5. Run locally:
```bash
python manage.py runserver
```
6. Push to Heroku with `git push heroku main`

---

## 📦 Installation (Local)
1. Python 3.x installed
2. Virtual environment activated
3. Run `pip install -r requirements.txt`
4. Configure `.env` file

---

## 🙏 Credits
- Stripe Docs
- Django Docs
- Bootstrap Team
- Code Institute community

---

© 2025 Eventopia. All Rights Reserved.



## 🔍 Testing

### 1. Manual Testing of Each Feature

| Feature                | Expected Behavior                                      | Test Result           |
|------------------------|--------------------------------------------------------|------------------------|
| Register/Login         | Users can register/login/logout                        | ✅ Works as expected   |
| Event Creation         | Only future dates allowed, valid price and quantity    | ✅ Works as expected   |
| Purchase Ticket        | Reduces quantity by 1, prevents past/sold out purchases| ✅ Works as expected   |
| Profile Page           | Shows past & upcoming events                           | ✅ Works as expected   |
| Dashboard (CRUD)       | Edit/Delete only visible to event creator              | ✅ Works as expected   |
| Navigation             | Navbar links behave consistently                       | ✅ Works as expected   |
| Stripe Checkout        | Redirects to Stripe, returns confirmation              | ✅ Works as expected   |
| Admin Access           | Admin shows all models including Payments              | ✅ Works as expected   |
| Responsive Design      | Layout adapts on desktop/tablet/mobile                 | ✅ Verified            |

---

### 2. Responsive Design Testing
Tested using [ResponsiveDesignChecker](https://responsivedesignchecker.com) on:
- iPhone 13, iPad, and Desktop screens
- All pages render content and controls responsively

---

### 3. Code Validation

| Type     | Tool Used                      | Validation Result |
|----------|--------------------------------|-------------------|
| HTML     | https://validator.w3.org/      | ✅ Passed         |
| CSS      | https://jigsaw.w3.org/css-validator/ | ✅ Passed  |
| JavaScript | https://jshint.com           | ✅ Minor warnings (unused var), no errors |

---

### 4. Feature Tests (Happy + Exception Paths)

**Event Creation (Valid Input)**  
- Expected: Saves and redirects to dashboard  
- Testing: Submitted valid form  
- Result: Event created  
- Fix: N/A

**Event Creation (Past Date)**  
- Expected: Form throws error  
- Testing: Submitted 2022-01-01  
- Result: Validation error shown  
- Fix: Server-side `clean_date` in form

**Ticket Purchase (Sold Out)**  
- Expected: Redirect and error shown  
- Testing: Tried to buy when quantity = 0  
- Result: Purchase blocked  
- Fix: Validation added in view

---

### 5. Bugs + Fixes Log

| Bug Description                       | Fix Summary                            |
|--------------------------------------|----------------------------------------|
| DEBUG=True in prod                   | Used env var + set `DEBUG=False`       |
| Secret key exposed                   | Moved to `.env`                        |
| Events allowed past dates            | Added form validation                  |
| Negative ticket price                | Added form validation                  |
| Payments not shown in admin          | Registered in `admin.py`               |

---

### 6. Open Bugs or Limitations

- No email confirmation after ticket purchase
- No pagination for large number of events
- No advanced search/filter features yet

---

## 🖼️ Screenshots & Wireframes

### Wireframes
> Replace these links with actual hosted images on GitHub or another service.

- Home Page: ![Home Wireframe](https://via.placeholder.com/600x400?text=Home+Wireframe)
- Dashboard: ![Dashboard Wireframe](https://via.placeholder.com/600x400?text=Dashboard+Wireframe)
- Event Form: ![Event Form](https://via.placeholder.com/600x400?text=Event+Form+Wireframe)

---

### Screenshots of Features

- Landing Page: ![Landing](https://via.placeholder.com/600x400?text=Landing+Page)
- Create Event: ![Create Event](https://via.placeholder.com/600x400?text=Create+Event+Form)
- Purchase Ticket: ![Purchase](https://via.placeholder.com/600x400?text=Purchase+Ticket+Flow)
- User Profile: ![Profile](https://via.placeholder.com/600x400?text=User+Profile+Page)
- Admin Panel: ![Admin](https://via.placeholder.com/600x400?text=Admin+Panel)


---

## 🏷️ Project Badges

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Django](https://img.shields.io/badge/Django-4.2-green)
![License](https://img.shields.io/badge/license-MIT-brightgreen)
![Responsive](https://img.shields.io/badge/Responsive-Yes-blueviolet)
