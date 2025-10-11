import sqlite3
import xml.etree.ElementTree as ET

# =============================
# 1️⃣ Đọc và phân tích XML
# =============================
tree = ET.parse("catalog.xml")
root = tree.getroot()

# Lấy danh sách categories
categories = []
for cat in root.find("categories").findall("category"):
    cat_id = cat.get("id")
    cat_name = cat.text.strip()
    categories.append((cat_id, cat_name))

# Lấy danh sách products
products = []
for prod in root.find("products").findall("product"):
    prod_id = prod.get("id")
    cat_ref = prod.get("categoryRef")
    name = prod.find("name").text.strip()
    price = float(prod.find("price").text)
    currency = prod.find("price").get("currency")
    stock = int(prod.find("stock").text)
    products.append((prod_id, name, price, currency, stock, cat_ref))

# =============================
# 2️⃣ Kết nối & tạo bảng SQLite
# =============================
conn = sqlite3.connect("catalog.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Categories (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Products (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL,
    currency TEXT,
    stock INTEGER,
    categoryRef TEXT,
    FOREIGN KEY (categoryRef) REFERENCES Categories(id)
)
""")

# =============================
# 3️⃣ Chèn hoặc cập nhật dữ liệu
# =============================
for cat in categories:
    cur.execute("""
    INSERT INTO Categories (id, name)
    VALUES (?, ?)
    ON CONFLICT(id) DO UPDATE SET
        name = excluded.name
    """, cat)

for prod in products:
    cur.execute("""
    INSERT INTO Products (id, name, price, currency, stock, categoryRef)
    VALUES (?, ?, ?, ?, ?, ?)
    ON CONFLICT(id) DO UPDATE SET
        name = excluded.name,
        price = excluded.price,
        currency = excluded.currency,
        stock = excluded.stock,
        categoryRef = excluded.categoryRef
    """, prod)

conn.commit()

# =============================
# 4️⃣ In kết quả kiểm tra
# =============================
print("=== Categories ===")
for row in cur.execute("SELECT * FROM Categories"):
    print(row)

print("\n=== Products ===")
for row in cur.execute("SELECT * FROM Products"):
    print(row)

conn.close()
