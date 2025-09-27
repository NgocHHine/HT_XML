from lxml import etree

# Load DTD
with open("order.dtd", "rb") as f:   # đổi đúng tên file DTD của bạn
    dtd = etree.DTD(f)

# Danh sách các file XML cần kiểm tra
xml_files = ["Bai1.xml", "Bai2.xml", "Bai3.xml"]

for file in xml_files:
    print(f"\n🔍 Đang kiểm tra {file} ...")
    xml = etree.parse(file)
    if dtd.validate(xml):
        print("✅ Hợp lệ theo DTD")
    else:
        print("❌ Không hợp lệ")
        print(dtd.error_log.filter_from_errors())
