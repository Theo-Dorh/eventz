# 🎉 Eventz – Event Management System

Eventz is a Django-based event management system that allows users with different roles (Admin, Organizer, Regular User) to create, manage, and register for events. It includes JWT-based authentication, role-based access, and a booking system.

---

## 🚀 Features

### 👤 User Management
- Register, login, logout using JWT
- Roles: **Admin**, **Organizer**, **User**
- Role-based access to events and bookings

### 📅 Event Management
- Create, edit, delete events (Organizer/Admin only)
- View all upcoming events
- View detailed event info

### 📝 Booking System
- Register/book for events
- Cancel a booking
- View personal booking history

### 📊 Admin Dashboard
- Manage users (via Django Admin)
- Monitor event bookings and cancellations

### 🔍 Search & Filtering (Planned)
- Filter events by name, location, date, category
- Filter by availability and organizer

---

## 🧱 Technology Stack

- **Backend Framework**: Django, Django REST Framework
- **Database**: SQLite (default, switchable)
- **Authentication**: JWT via `djangorestframework-simplejwt`
- **API Testing**: Browsable API / Postman / Django Admin

---

## 🗃 Database Models

### **User**
| Field       | Type          | Notes                  |
|-------------|---------------|------------------------|
| id          | AutoField     | Primary Key            |
| username    | CharField     | Unique                 |
| email       | EmailField    | Unique                 |
| password    | CharField     | Hashed                 |
| role        | CharField     | Admin, Organizer, User |
| created_at  | DateTimeField | Auto now add           |
| updated_at  | DateTimeField | Auto now               |

### **Event**
| Field       | Type          | Notes                  |
|-------------|---------------|------------------------|
| id          | AutoField     | Primary Key            |
| title       | CharField     |                        |
| description | TextField     |                        |
| location    | CharField     |                        |
| date        | DateField     |                        |
| time        | TimeField     |                        |
| organizer   | ForeignKey    | Linked to User         |
| created_at  | DateTimeField | Auto now add           |
| updated_at  | DateTimeField | Auto now               |

### **Booking**
| Field       | Type          | Notes                        |
|-------------|---------------|------------------------------|
| id          | AutoField     | Primary Key                  |
| user        | ForeignKey    | Linked to User               |
| event       | ForeignKey    | Linked to Event              |
| status      | CharField     | Pending, Confirmed, Canceled |
| created_at  | DateTimeField | Auto now add                 |

---

## 🔌 API Endpoints

### 🧾 Authentication
| Method | Endpoint           | Description              |
|--------|--------------------|--------------------------|
| POST   | `/api/register/`   | Register new user        |
| POST   | `/api/login/`      | Login & receive token    |
| POST   | `/api/logout/`     | (Optional) Logout        |

### 📅 Events
| Method | Endpoint               | Description                       |
|--------|------------------------|-----------------------------------|
| GET    | `/api/events/`         | List all events                   |
| POST   | `/api/events/`         | Create event (Organizer/Admin)    |
| GET    | `/api/events/{id}/`    | View event details                |
| PUT    | `/api/events/{id}/`    | Update event (Organizer/Admin)    |
| DELETE | `/api/events/{id}/`    | Delete event (Organizer/Admin)    |

### 📝 Bookings
| Method | Endpoint               | Description                       |
|--------|------------------------|-----------------------------------|
| POST   | `/api/bookings/`       | Book an event                     |
| GET    | `/api/bookings/`       | List user bookings                |
| DELETE | `/api/bookings/{id}/`  | Cancel a booking                  |

---

## ⚙️ Setup Instructions

1. **Clone the project**
```bash
git clone https://github.com/your-username/eventz.git
cd eventz

