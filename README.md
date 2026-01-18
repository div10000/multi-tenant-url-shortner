# Multi-Tenant URL Shortener

## Overview

A SaaS-ready, multi-tenant URL shortener built with **Django REST Framework**, supporting multiple white-label frontends running on a single backend.

Each frontend (reseller) is registered as a tenant and is automatically isolated using domain-based tenant resolution, enabling seamless multi-tenant operations without server restarts.

## Features

- ✨ Single backend supporting multiple resellers (tenants)
- 🔐 Domain-based tenant detection and isolation
- 🎨 White-label support (different frontends, same backend)
- 🌍 Dynamic CORS handling per tenant
- 👨‍💼 Admin-managed tenants and URLs
- 🖥️ Lightweight HTML/CSS/JS frontend (easily replaceable with React/Next.js)

## Project Structure

```
url-shortener/
├── backend/                  # Django REST Framework backend
│   ├── backend/              # Django settings & configuration
│   ├── shortener/            # URL shortening app
│   ├── tenants/              # Multi-tenant management app
│   ├── manage.py
│   ├── db.sqlite3
│   └── requirements.txt
├── frontend/                 # Static frontend (HTML/CSS/JS)
│   ├── index.html
│   ├── script.js
│   └── style.css
├── README.md
└── .gitignore
```

## Backend Setup

### 1. Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On macOS/Linux
pip install -r requirements.txt
```

### 2. Run Database Migrations

```bash
python backend/manage.py migrate
```

### 3. Create Superuser (Admin Access)

```bash
python backend/manage.py createsuperuser
```

Follow the prompts to set username, email, and password.

### 4. Start Backend Server

```bash
python backend/manage.py runserver
```

Backend will be available at:
- **API Base URL:** http://127.0.0.1:8000
- **Admin Panel:** http://127.0.0.1:8000/admin

## Tenant Setup

Tenants must be configured before using the application.

### Steps

1. Navigate to the Django Admin Panel at `http://127.0.0.1:8000/admin`
2. Log in with your superuser credentials
3. Create a new Tenant
4. Set the domain **exactly** as used in the browser

### Tenant Domain Examples

| Frontend URL | Tenant Domain |
|---|---|
| http://localhost:5500 | localhost |
| http://127.0.0.1:5500 | 127.0.0.1 |
| https://myreseller.com | myreseller.com |

> **Note:** No migrations or server restart required when adding new tenants.

## Frontend Setup

### 1. Start HTTP Server

The frontend must be served over HTTP (not opened with `file://` protocol):

```bash
python -m http.server 5500 --directory frontend
```

### 2. Access in Browser

Open your browser and navigate to:
- http://127.0.0.1:5500/index.html

## API Endpoints

### 1. Shorten URL

**Endpoint:** `POST /api/shorten/`

**Request Body:**
```json
{
  "original_url": "https://example.com/very/long/url"
}
```

**Response:**
```json
{
  "short_url": "http://localhost:8000/AbC123",
  "original_url": "https://example.com/very/long/url"
}
```

### 2. Retrieve Original URL

**Endpoint:** `GET /api/shorten/{short_code}/`

**Response:**
```json
{
  "short_code": "AbC123",
  "original_url": "https://example.com/very/long/url",
  "created_at": "2026-01-18T10:30:00Z"
}
```

## Technology Stack

| Component | Technology |
|---|---|
| Backend | Django 4.x, Django REST Framework |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Database | SQLite3 (development) |
| Multi-Tenancy | Domain-based tenant resolution |


## Deployment

For production deployment:

1. Use PostgreSQL instead of SQLite
2. Configure environment variables in `.env`
3. Set `DEBUG=False` in settings
4. Use a production WSGI server (Gunicorn, uWSGI)
5. Configure HTTPS/SSL certificates
6. Set up proper CORS origins for your tenants

Chant Hare Krishna and Be Happy  🙇🏻