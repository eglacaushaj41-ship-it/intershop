import sqlite3

conn = sqlite3.connect("products.db")
cursor = conn.cursor()

# =========================
# TABLE (WITH YEAR)
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    image TEXT,
    year TEXT
)
""")

# =========================
# PRODUCTS (WITH YEAR ADDED)
# =========================
products = [

    ("Inter Milan 1997/98 Third Kit", 79.99, "inter-milan-1997-98-third-kit.jpg", "1997/98"),
    ("Inter Milan 2008/09 Home Kit", 89.99, "inter-milan-2008-09-home-kit.jpg", "2008/09"),
    ("Inter Milan 2009/10 Anthem Jacket", 99.99, "inter-milan-2009-10-anthem-jacket.jpg", "2009/10"),
    ("Inter Milan 2009/10 Champions League Final Kit", 119.99, "inter-milan-2009-10-champions-league-final-kit.jpg", "2009/10"),
    ("Inter Milan 2009/10 Coppa Italia Final Kit", 109.99, "inter-milan-2009-10-coppa-italia-final-kit.jpg", "2009/10"),
    ("Inter Milan 2009/10 Home Kit", 94.99, "inter-milan-2009-10-home-kit.jpg", "2009/10"),
    ("Inter Milan 2024/25 Home Kit", 89.99, "inter-milan-2024-25-home-kit.jpg", "2024/25"),
    ("Inter Milan 2025/26 Away Kit", 89.99, "inter-milan-2025-26-away-kit.jpg", "2025/26"),
    ("Inter Milan 2025/26 Fourth Kit", 99.99, "inter-milan-2025-26-fourth-kit.jpg", "2025/26"),
    ("Inter Milan 2025/26 Home Kit", 89.99, "inter-milan-2025-26-home-kit.jpg", "2025/26"),
    ("Inter Milan 2025/26 Third Kit", 94.99, "inter-milan-2025-26-third-kit.jpg", "2025/26"),
    ("Inter Milan 2026/27 Away Kit", 92.99, "inter-milan-2026-27-away-kit.jpg", "2026/27"),
    ("Inter Milan 2026/27 Home Kit", 92.99, "inter-milan-2026-27-home-kit.jpg", "2026/27"),
    ("Inter Milan 2026/27 Training Shirt", 69.99, "inter-milan-2026-27-training-shirt.jpg", "2026/27"),
    ("Inter Milan 2009/10 GK Kit", 99.99, "inter-milan-2009-10-gk-1-kit.jpg", "2009/10")

]

# =========================
# INSERT
# =========================
cursor.executemany(
    "INSERT INTO products(name, price, image, year) VALUES(?,?,?,?)",
    products
)

conn.commit()
conn.close()

print("Database created successfully with YEAR field!")