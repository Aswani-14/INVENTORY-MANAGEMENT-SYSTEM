from flask import Flask, render_template, request, redirect, session
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = "secret123"

client = MongoClient("mongodb://localhost:27017/")
db = client["inventory_db"]

users = db["users"]
products = db["products"]
suppliers = db["suppliers"]

# ---------- LOGIN ----------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = users.find_one({"username": username, "password": password})

        if user:
            session["user"] = username
            return redirect("/dashboard")
        else:
            return "Invalid login"

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    all_products = list(products.find())

    product_count = len(all_products)
    supplier_count = suppliers.count_documents({})
    low_stock_list = [p for p in all_products if int(p["qty"]) < 5]
    low_stock = len(low_stock_list)

    return render_template(
        "dashboard.html",
        product_count=product_count,
        supplier_count=supplier_count,
        low_stock=low_stock,
        low_stock_list=low_stock_list,
        products = all_products 
    )


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")


# ---------- PRODUCTS ----------
@app.route("/products", methods=["GET", "POST"])
def product():
    if request.method == "POST":
       products.insert_one({
    "name": request.form["name"],
    "price": int(request.form["price"]),
    "qty": int(request.form["qty"])
})

    data = list(products.find())
    return render_template("products.html", products=data)


# ---------- SUPPLIERS ----------
@app.route("/suppliers", methods=["GET", "POST"])
def supplier():
    if request.method == "POST":
        suppliers.insert_one({
            "name": request.form["name"],
            "phone": request.form["phone"]
        })

    data = list(suppliers.find())
    return render_template("suppliers.html", suppliers=data)


# ---------- REPORT ----------
@app.route("/report")
def report():
    all_products = list(products.find())

    total_products = len(all_products)

    total_quantity = sum(int(p["qty"]) for p in all_products)

    total_value = sum(int(p["price"]) * int(p["qty"]) for p in all_products)

    low_stock_items = [p for p in all_products if int(p["qty"]) < 5]

    return render_template(
        "report.html",
        products=all_products,
        total_products=total_products,
        total_quantity=total_quantity,
        total_value=total_value,
        low_stock=low_stock_items
    )

# ---------- UPDATE ----------
@app.route("/update/", defaults={"id": None}, methods=["GET", "POST"])
@app.route("/update/<id>", methods=["GET", "POST"])
def update_product(id):
    all_products = list(products.find())

    product = None
    if id:
        product = products.find_one({"_id": ObjectId(id)})

    if request.method == "POST" and id:
        products.update_one(
            {"_id": ObjectId(id)},
            {
                "$set": {
                    "name": request.form["name"],
                    "price": int(request.form["price"]),
                    "qty": int(request.form["qty"])
                }
            }
        )
        return redirect("/update")

    return render_template("update.html", products=all_products, product=product)
# ---------- DELETE ----------
@app.route("/delete/", defaults={"id": None}, methods=["GET", "POST"])
@app.route("/delete/<id>", methods=["GET", "POST"])
def delete_product(id):
    all_products = list(products.find())

    product = None
    if id:
        product = products.find_one({"_id": ObjectId(id)})

    if request.method == "POST" and id:
        products.delete_one({"_id": ObjectId(id)})
        return redirect("/delete")

    return render_template("delete.html", products=all_products, product=product)
app.run(debug=True)