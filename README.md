# 🛍️ E-Commerce Platform Architecture Overview

A full-stack e-commerce application built using Django, PostgreSQL, React, HTML, CSS, and JavaScript. This platform supports both vendor and customer sides, with features like product management, cart functionality, authentication, and checkout flow.



## ⚙️ Tech Stack

| Layer       | Technology                    | Description                                   |
|-------------|-------------------------------|-----------------------------------------------|
| Frontend    | React, HTML, CSS (Tailwind/Bootstrap) | Dynamic UI, cart interactions, vendor dashboard |
| Backend     | Django + Django REST Framework | APIs, business logic, data processing         |
| Database    | PostgreSQL                    | Persistent storage for products, users, orders|
| Auth        | DRF Token Auth or JWT         | Login, signup, protected views                |
| Media       | Django Media Files / S3 Bucket| Product image hosting                         |
| Hosting     | Render / Heroku + Vercel/Netlify| Deployment for backend and frontend           |

---

## 🧱 Database Models

### 👤 `User`  
Uses Django’s built-in user model with authentication support.

### 🧑‍💼 `Vendor`  
One-to-one with User.  
Fields:
- `store_name`
- `bio`
- `joined_at`

### 🛒 `Product`  
Each product belongs to a vendor.  
Fields:
- `title`
- `description`
- `price`
- `image` (uploaded file)
- `vendor` (ForeignKey)

### 🧺 `CartItem`  
Temporarily stores items selected by a user.  
Fields:
- `product`
- `quantity`
- `user` (or session ID)

### 📦 `Order`  
Stores completed orders.  
Fields:
- `items`
- `total`
- `user`
- `timestamp`

---

## 📐 Frontend Components (React)

| Component         | Role                                                   |
|-------------------|--------------------------------------------------------|
| `ProductList`     | Displays all available products                        |
| `ProductDetail`   | View single product info and add to cart               |
| `Cart`            | View items added to cart, update/remove                |
| `Checkout`        | Place final order, view summary                        |
| `AuthForm`        | Login / signup for both customers and vendors          |
| `VendorDashboard` | Vendor-only portal to manage product listings          |
| `Navbar`          | Navigation bar for switching between pages             |

Routing via `react-router-dom`

---

## 🔐 Authentication

- `POST /api/token-auth/` — get token with credentials
- `Authorization: Token <token>` — used for protected POST/PUT requests
- Permissions:
  - Customers: Can browse, add to cart, checkout
  - Vendors (admin/staff): Can create/manage products

---

## 🚀 Hosting Plan

| Role        | Platform     | Notes                          |
|-------------|--------------|--------------------------------|
| Backend     | Render / Heroku | Supports PostgreSQL + Django  |
| Frontend    | Vercel / Netlify | Fast React hosting            |
| Media       | Render or S3 Bucket | Stores uploaded product images  |

---

## 📚 Future Improvements

- Product categories and filters
- Review & rating system
- Bank or simulated payment flow
- Email confirmations for orders
- Admin analytics dashboard (orders/sales)

---

## 🎨 Styling Strategy

- 📦 CSS Framework: Tailwind CSS (preferred for component-based design)
- 🎨 Optional: Bootstrap or custom SCSS
- 🛠️ Responsive UI with mobile-first breakpoints

---

## 🗂️ Folder Structure Suggestion (Frontend)
