# API-Security-Tool
# API Security Tool

## Overview

API Security Tool is a Python-based application developed using FastAPI to demonstrate basic API security concepts. The tool acts as a middleware layer that inspects incoming HTTP requests before they reach the API endpoints. It detects common attack patterns, validates authentication tokens, enforces rate limiting, and applies security headers to responses.

This project is intended for educational purposes and as a portfolio project to demonstrate API security, secure software development, and backend programming skills.

---

# Features

* FastAPI-based REST API
* Custom Security Middleware
* SQL Injection Detection
* Cross-Site Scripting (XSS) Detection
* Path Traversal Detection
* JWT Token Validation
* Basic Rate Limiting
* HTTP Security Headers
* Request Interception
* Swagger API Documentation
* Modular Scanner Architecture

---

# Technology Stack

* Python 3.12+
* FastAPI
* Uvicorn
* Starlette Middleware
* PyJWT
* python-jose

---

# Project Structure

```
api-security-tool/
│
├── app.py
├── requirements.txt
│
├── gateway/
│   ├── __init__.py
│   └── middleware.py
│
├── scanner/
│   ├── __init__.py
│   ├── sqli.py
│   ├── xss.py
│   ├── traversal.py
│   ├── jwt.py
│   ├── headers.py
│   └── rate_limit.py
│
├── README.md
│
└── .gitignore
```

---

# Working Principle

1. Client sends an HTTP request.
2. The request passes through the Security Middleware.
3. The middleware performs:

   * SQL Injection detection
   * XSS detection
   * Path Traversal detection
   * JWT validation
   * Rate limiting
4. If a malicious request is detected, the request is blocked.
5. If the request is safe, it is forwarded to the API endpoint.
6. Security headers are added to the response before it is returned to the client.

---

# Security Checks

## SQL Injection Detection

Detects common SQL injection payloads such as:

* ' OR 1=1 --
* UNION SELECT
* DROP TABLE
* INSERT
* DELETE

---

## XSS Detection

Detects JavaScript injection attempts including:

* <script>

* javascript:
* onload=
* onerror=

---

## Path Traversal Detection

Detects directory traversal attempts including:

* ../
* ..\
* /etc/passwd
* windows/system32

---

## JWT Validation

Checks whether:

* JWT exists
* Signature is valid
* Token is correctly formatted

---

## Rate Limiting

Limits the number of requests from a single client within a fixed time window to help reduce brute-force and abuse attempts.

---

## Security Headers

Automatically adds:

* X-Frame-Options
* X-Content-Type-Options
* Content-Security-Policy

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/api-security-tool.git
```

Move into the project directory:

```bash
cd api-security-tool
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m uvicorn app:app --reload
```

---

# API Endpoints

GET /

Returns the application status.

GET /users

Returns a sample list of users.

POST /login

Accepts a JSON request body and returns the submitted data.

---

# API Documentation

FastAPI automatically generates interactive documentation.

Swagger UI:

http://127.0.0.1:8000/docs

OpenAPI JSON:

http://127.0.0.1:8000/openapi.json

---

# Sample SQL Injection Test

```
GET /users?id=' OR 1=1--
```

Expected Response:

```
403 Forbidden
```

---

# Sample XSS Test

```
GET /?name=<script>alert(1)</script>
```

Expected Response:

```
403 Forbidden
```

---

# Sample Path Traversal Test

```
GET /?file=../../etc/passwd
```

Expected Response:

```
403 Forbidden
```

---

# Current Limitations

* Pattern-based detection only
* No database logging
* No dashboard
* No machine learning
* No API discovery
* No report generation
* No OpenAPI scanning
* No distributed rate limiting

---

# Future Enhancements

* SQLite/PostgreSQL logging
* Web dashboard
* PDF and HTML report generation
* Machine Learning anomaly detection
* API inventory
* OpenAPI/Swagger scanning
* GraphQL security testing
* OAuth 2.0 support
* Docker deployment
* Kubernetes deployment
* CI/CD integration
* Email alerts
* Role-Based Access Control (RBAC)
* API risk scoring

---

# Learning Objectives

This project demonstrates:

* Python backend development
* REST API development
* FastAPI framework
* Middleware implementation
* API request inspection
* Authentication validation
* Secure coding practices
* Basic API security testing
* Modular software architecture

---

# License

This project is intended for educational and research purposes.
