import sqlite3
from lxml import etree

# ----------- 1. Parse XML và XSD -----------
xml_file = "catalog.xml"
xsd_file = "catalog.xsd"

xml_doc = etree.parse(xml_file)
xsd_doc = etree.parse(xsd_file)
schema = etree.XMLSchema(xsd_doc)

# ----------- 2. Validate -----------
try:
    schema.assertValid(xml_doc)
    print("✅ XML hợp lệ theo XSD, bắt đầu ghi vào SQLite...")
except etree.DocumentInvalid as e:
    print("❌ XML không hợp lệ:", e)
    exit()

# ----------- 3. Kết nối SQLite -----------
conn = sqlite3.connect("catalog.db")
cursor = conn.cursor()

# ----------- 4. Tạo bảng nếu chưa có -----------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Categories (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL
)
""")

cursor.execute("""
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

# ----------- 5. Dùng XPath để lấy dữ liệu -----------
root = xml_doc.getroot()

# Categories
for cat in root.xpath("//category"):
    cid = cat.get("id")
    cname = cat.text
    cursor.execute("""
        INSERT INTO Categories (id, name)
        VALUES (?, ?)
        ON CONFLICT(id) DO UPDATE SET name=excluded.name
    """, (cid, cname))

# Products
for prod in root.xpath("//product"):
    pid = prod.get("id")
    categoryRef = prod.get("categoryRef")
    name = prod.findtext("name")
    price = prod.findtext("price")
    currency = prod.find("price").get("currency")
    stock = prod.findtext("stock")

    cursor.execute("""
        INSERT INTO Products (id, name, price, currency, stock, categoryRef)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(id) DO UPDATE SET
            name=excluded.name,
            price=excluded.price,
            currency=excluded.currency,
            stock=excluded.stock,
            categoryRef=excluded.categoryRef
    """, (pid, name, price, currency, stock, categoryRef))

# ----------- 6. Commit và đóng kết nối -----------
conn.commit()
print("✅ Dữ liệu đã được chèn/cập nhật vào catalog.db thành công.")
cursor.close()
conn.close()
