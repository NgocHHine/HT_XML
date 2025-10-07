from lxml import etree

# ===== Đọc file XML =====
tree = etree.parse("school.xml")
root = tree.getroot()

# Namespace trong XML
ns = {"lib": "http://example.com/library"}

# ===== Đọc tất cả truy vấn từ file queries.xpath =====
xpath_file = "queries.txt"
queries = []

with open(xpath_file, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#"):  # bỏ dòng trống và chú thích
            queries.append(line)

# ===== Thực thi từng XPath =====
# for i, xp in enumerate(queries, start=1):
#     try:
#         result = root.xpath(xp, namespaces=ns)
#         # Chuyển các phần tử XML thành chuỗi
#         if isinstance(result, list):
#             values = []
#             for r in result:
#                 if isinstance(r, etree._Element):
#                     values.append(etree.tostring(r, encoding='unicode').strip())
#                 else:
#                     values.append(str(r))
#         else:
#             values = [str(result)]
#         print(f"\n[{i}] XPath: {xp}")
#         print("→ Kết quả:", values)
#     except Exception as e:
#         print(f"\n[{i}] XPath lỗi: {xp}")
#         print("→ Lỗi:", e)
for i, q in enumerate(queries, start=1):
    try:
        result = tree.xpath(q, namespaces=ns)

        print(f"[{i}] {q}")
        # Trường hợp count() trả về float
        if isinstance(result, float):
            print("→", int(result))

        # Trường hợp substring trả về str
        elif isinstance(result, str):
            print("→", result)

        # Trường hợp list
        elif isinstance(result, list):
            if not result:
                print("→ Không có kết quả.")
            else:
                # Loại bỏ trùng lặp kết quả (set)
                seen = set()
                for r in result:
                    if isinstance(r, etree._Element):
                        xml_str = etree.tostring(r, pretty_print=True, encoding="unicode")
                        if xml_str not in seen:
                            print(xml_str)
                            seen.add(xml_str)
                    else:
                        if r not in seen:
                            print("→", r)
                            seen.add(r)
        print()
    except Exception as e:
        print(f"[{i}] Lỗi XPath: {q}")
        print("→", e, "\n")