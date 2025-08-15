# Engagement Post Management System

A Flask + PostgreSQL web application to manage **video reels, stories, products, and collections** for multi-tenant environments.
The system provides APIs and a simple HTML UI for managing engagement posts, mapping them to collections, and tracking video watch durations.

---

## 📌 Features

* **Multi-Tenant Post Management** – Store and retrieve engagement posts (videos, stories) for different tenants.
* **Media & Product Linking** – Map posts to media URLs and associated products.
* **Collection Management** – Group posts into collections with watch-duration tracking.
* **Top Engagement Analytics** – APIs to retrieve top 5 viewed posts and products for each tenant.
* **Role-Based Database Setup** – Ensures proper PostgreSQL role creation before restoring backup data.
* **Responsive UI** – HTML templates styled with Bulma CSS.

---

## 🛠️ Tech Stack

**Backend:** Python (Flask), SQLAlchemy ORM
**Database:** PostgreSQL 13.x
**Frontend:** HTML5, Bulma CSS, Jinja2 Templates
**Tools:** Git, Postman, Docker (optional)

---

## 📂 Project Structure

```
engagement_app/
│
├── app.py                 # Main Flask application
├── config.py              # App configuration (DB connection, settings)
├── models.py              # SQLAlchemy models for all tables
├── templates/             # HTML templates (base.html, forms, listings)
├── static/                # Static assets (CSS, JS)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Prerequisites

* **PostgreSQL 13.x**
* **Python 3.9+**
* Ensure required PostgreSQL roles are created as per the provided reference images.

### 2️⃣ Database Setup

```bash
# Create database
createdb engagement

# Restore backup
psql -U postgres -d engagement -f engagement_backup_training.bak
```

> If you encounter errors during restore, ensure all required roles are created.

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Environment Configuration

Edit `config.py`:

```python
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:root@localhost:5432/engagement"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

---

## 🗄 Database Schema

**Tables:**

* `engagement_post` – Post details per tenant.
* `engagement_post_content` – Media URLs for posts.
* `engagement_post_product_mapping` – Links products to posts.
* `engagement_post_product` – Product details (name, image, SKU).
* `collection` – Named collections of posts.
* `engagement_post_collection` – Mapping of posts to collections with `duration_in_seconds`.

---

## 🔌 API Endpoints

| Method | Endpoint            | Description                                     |
| :----: | ------------------- | ----------------------------------------------- |
|   GET  | `/api/posts`        | Fetch posts, content, and products for a tenant |
|  POST  | `/api/products`     | Create a new product                            |
|  POST  | `/api/collections`  | Create a new collection with posts              |
|   GET  | `/api/top-posts`    | Top 5 viewed posts for a tenant                 |
|   GET  | `/api/top-products` | Top 5 most viewed products for a tenant         |

---

## 💻 HTML UI Pages

| Route                  | Description                                  |
| ---------------------- | -------------------------------------------- |
| `/product/new`         | Create a new product                         |
| `/collection/new`      | Create a new collection                      |
| `/collections`         | View all collections                         |
| `/post-collection/new` | Map posts to collections with watch duration |
| `/top-posts`           | View top 5 posts for a tenant                |

---

## 🧪 Testing

Use Postman or cURL to test the APIs:

```bash
curl -X GET "http://127.0.0.1:5000/api/top-posts?tenant_id=<tenant_uuid>"
```

---

## 🚀 Running the Application

```bash
python app.py
```

Access the app at: [http://127.0.0.1:5000](http://127.0.0.1:5000)
