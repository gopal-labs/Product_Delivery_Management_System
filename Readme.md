# Product Delivery Management System

A web-based Product Delivery Management System developed using:

- Python Flask
- PostgreSQL
- HTML/CSS
- VS Code

This project demonstrates core and intermediate DBMS concepts including:

- Relational database design
- Primary & Foreign Keys
- CRUD Operations
- JOIN Queries
- Triggers
- Dynamic Web Pages
- Inventory Management

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Flask | Backend Framework |
| PostgreSQL | Database |
| pgAdmin | Database Management |
| HTML/CSS | Frontend |
| VS Code | Development Environment |
| psycopg2 | PostgreSQL Driver |

---

# Project Structure

```text
product_delivery_system/
│
├── app.py
├── database.py
├── templates/
│   ├── index.html
│   ├── customers.html
│   ├── orders.html
│   └── order_items.html
│
├── static/
│   └── style.css
│
└── sql/
```

---

# Features Implemented

## 1. Product Management

- Add products
- View products
- Store product stock
- Product pricing

### Product Fields

- Product ID
- Product Name
- Price
- Stock

---

## 2. Customer Management

- Add customers
- View customer details

### Customer Fields

- Customer ID
- Name
- Email
- Phone

---

## 3. Order Management

- Create orders
- Assign orders to customers
- Track order type
- Track order status

### Order Types

- Normal
- Express

### Order Status

- Pending
- Paid
- Shipped
- Out For Delivery
- Delivered

---

## 4. Order Item Management

- Add products to orders
- Select quantity
- Automatic subtotal calculation

### Order Item Fields

- Order ID
- Product ID
- Quantity
- Subtotal

---

## 5. Inventory Management

Automatic stock reduction using PostgreSQL Trigger.

When a product is added to an order:

```text
Product stock decreases automatically
```

---

# Database Tables

## Customers

```sql
CREATE TABLE Customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15)
);
```

---

## Products

```sql
CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10,2),
    stock INT
);
```

---

## Orders

```sql
CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES Customers(customer_id),
    order_type VARCHAR(30),
    order_status VARCHAR(30),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Order_Items

```sql
CREATE TABLE Order_Items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES Orders(order_id),
    product_id INT REFERENCES Products(product_id),
    quantity INT,
    subtotal DECIMAL(10,2)
);
```

---

# Trigger Implementation

## Trigger Function

```sql
CREATE OR REPLACE FUNCTION reduce_stock()
RETURNS TRIGGER AS $$

BEGIN

    UPDATE Products
    SET stock = stock - NEW.quantity
    WHERE product_id = NEW.product_id;

    RETURN NEW;

END;

$$ LANGUAGE plpgsql;
```

---

## Trigger

```sql
CREATE TRIGGER stock_trigger

AFTER INSERT ON Order_Items

FOR EACH ROW

EXECUTE FUNCTION reduce_stock();
```

---

# DBMS Concepts Used

| Concept | Implemented |
|---|---|
| Primary Keys | ✅ |
| Foreign Keys | ✅ |
| One-to-Many Relationship | ✅ |
| Many-to-Many Relationship | ✅ |
| JOIN Queries | ✅ |
| CRUD Operations | ✅ |
| Triggers | ✅ |
| Dynamic Queries | ✅ |
| Relational Modeling | ✅ |

---

# Workflow

```text
Customer
   ↓
Creates Order
   ↓
Selects Product
   ↓
Adds Quantity
   ↓
Subtotal Calculated
   ↓
Stock Reduced Automatically
```

---

# Screens Implemented

- Product Management Page
- Customer Management Page
- Order Management Page
- Order Items Page

---

# How To Run The Project

## Step 1 — Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## Step 2 — Install Dependencies

```bash
pip install flask psycopg2-binary
```

---

## Step 3 — Run Flask Application

```bash
python app.py
```

---

## Step 4 — Open Browser

```text
http://127.0.0.1:5000
```

---

# Future Enhancements

## Advanced DBMS Features

- Transactions
- Rollback Handling
- ACID Properties
- Deadlock Prevention
- Concurrency Control
- Row Locking
- Isolation Levels
- Payment Module
- Delivery Tracking
- Authentication System

---

# Learning Outcomes

This project helped in understanding:

- Relational Database Design
- Flask + PostgreSQL Integration
- Dynamic Backend Development
- SQL Query Execution
- Trigger-Based Automation
- Inventory Management Systems

---

# Project Status

```text
Current Level: Intermediate DBMS Project
```

Future upgrades will convert this into an advanced enterprise-level DBMS system.
