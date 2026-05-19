from flask import Flask, render_template, redirect, session, request
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "intershop_secret"


# =========================
# PRODUCTS DB
# =========================
def get_products():
    conn = sqlite3.connect("products.db")
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    data = c.fetchall()
    conn.close()
    return data


# =========================
# INIT SHOP DB
# =========================
def init_shop_db():
    conn = sqlite3.connect("shop.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        iban TEXT
    )
    """)

    c.execute("SELECT COUNT(*) FROM users")
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO users (name, iban) VALUES (?, ?)",
                  ("User A", "AL47212110090000000235698741"))
        c.execute("INSERT INTO users (name, iban) VALUES (?, ?)",
                  ("User B", "AL35202111090000000001234567"))

    conn.commit()
    conn.close()


init_shop_db()


# =========================
# HOME (SEARCH + FILTER)
# =========================
@app.route("/")
def home():
    search = request.args.get("search")
    year = request.args.get("year")

    products = get_products()

    # search
    if search:
        products = [p for p in products if search.lower() in p[1].lower()]

    # cart count
    cart_count = len(session.get("cart", []))

    return render_template("index.html",
                           products=products,
                           cart_count=cart_count)


# =========================
# ADD TO CART
# =========================
@app.route("/add/<int:id>")
def add_to_cart(id):

    if "cart" not in session:
        session["cart"] = []

    if id not in session["cart"]:
        session["cart"].append(id)

    session.modified = True
    return redirect("/")


# =========================
# REMOVE FROM CART
# =========================
@app.route("/remove/<int:id>")
def remove_from_cart(id):

    if "cart" in session:
        session["cart"] = [x for x in session["cart"] if x != id]
        session.modified = True

    return redirect("/cart")


# =========================
# CART
# =========================
@app.route("/cart")
def cart():

    products = get_products()
    product_map = {p[0]: p for p in products}

    items = []
    total = 0

    for pid in session.get("cart", []):
        if pid in product_map:
            items.append(product_map[pid])
            total += product_map[pid][2]

    return render_template("cart.html",
                           cart=items,
                           total=total)


# =========================
# CHECKOUT
# =========================
@app.route("/checkout")
def checkout():
    return render_template("checkout.html")


# =========================
# PAYMENT
# =========================
@app.route("/pay", methods=["POST"])
def pay():

    iban = request.form["iban"]

    conn = sqlite3.connect("shop.db")
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE iban=?", (iban,))
    user = c.fetchone()

    conn.close()

    if user:
        session.pop("cart", None)
        return redirect("/success")
    else:
        return "<h1>Payment Failed ❌ Invalid IBAN</h1><a href='/cart'>Back</a>"


# =========================
# SUCCESS
# =========================
@app.route("/success")
def success():
    return render_template("success.html")


# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)