# 📦 Inventory Management System

A web-based Inventory Management System developed using **Python, Flask, and MongoDB** for managing products, suppliers, and inventory reports efficiently. The project demonstrates CRUD operations, MongoDB integration, and Flask-based web application development.

## Overview

The Inventory Management System is a web-based application developed using Python, Flask, and MongoDB to manage inventory operations efficiently. The system provides functionalities for managing products, suppliers, stock updates, and inventory reports through a simple and user-friendly interface.

The application helps reduce manual work and improves the accuracy of inventory management by automating operations such as adding, updating, deleting, and viewing inventory records.

---

# 🚀 Features

* User Login Authentication
* Dashboard with inventory summary
* Add and view products
* Update product details
* Delete products
* Manage supplier information
* Generate inventory reports
* Low stock detection
* Real-time database updates

---

# 🛠️ Technologies Used

## Frontend

* HTML
* CSS

## Backend

* Python
* Flask

## Database

* MongoDB

## Database Connector

* PyMongo

---

# 📂 Project Structure

```text
InventoryManagementSystem/
│
├── app.py
├── static/
│   └── style.css
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── products.html
│   ├── suppliers.html
│   ├── update.html
│   ├── delete.html
│   └── report.html
└── README.md
```

---

# 📑 Modules

## Login Module

The login module authenticates users using username and password stored in MongoDB.

## Dashboard Module

The dashboard displays total products, supplier count, and low stock items.

## Product Management Module

This module allows users to add and view products in the inventory.

## Update Module

The update module allows users to modify existing product details.

## Delete Module

The delete module allows users to remove products from the inventory.

## Supplier Module

This module manages supplier details such as supplier name and contact information.

## Report Module

The report module generates inventory reports including total products, quantity, and low stock items.

---

# 🗄️ Database Design

## Database Name

```text
inventory_db
```

## Collections

### users

Stores login credentials.

Example:

```json
{
  "username": "admin",
  "password": "123"
}
```

### products

Stores product details.

Example:

```json
{
  "name": "Mouse",
  "price": 500,
  "qty": 20
}
```

### suppliers

Stores supplier information.

Example:

```json
{
  "name": "ABC Traders",
  "phone": "9876543210"
}
```

---

# ⚙️ Installation & Setup

## Step 1: Install Python

Download and install Python 3.x.

## Step 2: Install MongoDB

Download and install MongoDB Community Server.

Start MongoDB service:

```bash
net start MongoDB
```

## Step 3: Install Required Libraries

```bash
pip install flask pymongo
```

## Step 4: Run the Application

```bash
python app.py
```

## Step 5: Open in Browser

```text
http://127.0.0.1:5000/
```

---

# 🔄 CRUD Operations

## Insert Data

```python
products.insert_one({
    "name": "Keyboard",
    "price": 1200,
    "qty": 15
})
```

## Retrieve Data

```python
products.find()
```

## Update Data

```python
products.update_one(
    {"_id": ObjectId(id)},
    {"$set": {"qty": 10}}
)
```

## Delete Data

```python
products.delete_one({"_id": ObjectId(id)})
```

---

# ✅ Advantages

* Simple and user-friendly interface
* Real-time inventory management
* Flexible MongoDB database
* Efficient CRUD operations
* Reduced manual errors

---

# 🔮 Future Enhancements

* Password encryption
* Barcode scanning
* Graphical reports and analytics
* Cloud deployment
* Mobile application support

---

# 📌 Conclusion

The Inventory Management System successfully demonstrates the integration of Flask and MongoDB for efficient inventory management. The system automates inventory operations, reduces manual effort, and ensures accurate data handling. It provides a scalable and reliable solution suitable for small and medium-scale inventory management applications.

---

# 📚 References

* MongoDB Documentation
* Flask Documentation
* Python Documentation
* PyMongo Documentation

