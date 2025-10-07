from lxml import etree

# Đọc file XML
tree = etree.parse("quanan.xml")
root = tree.getroot()

# Khai báo namespace
ns = {"lib": "http://example.com/library"}

# 1. Lấy tất cả bàn
print("Tất cả bàn:", tree.xpath("//lib:BAN/lib:TENBAN/text()", namespaces=ns))

# 2. Lấy tất cả nhân viên
print("Tất cả nhân viên:", tree.xpath("//lib:NHANVIEN/lib:TENV/text()", namespaces=ns))

# 3. Lấy tất cả tên món
print("Tên món:", tree.xpath("//lib:MON/lib:TENMON/text()", namespaces=ns))

# 4. Lấy tên nhân viên có mã NV02
print("Tên NV02:", tree.xpath("//lib:NHANVIEN[lib:MANV='NV02']/lib:TENV/text()", namespaces=ns))

# 5. Lấy tên và số điện thoại của nhân viên NV03
ten_nv03 = tree.xpath("//lib:NHANVIEN[lib:MANV='NV03']/lib:TENV/text()", namespaces=ns)
sdt_nv03 = tree.xpath("//lib:NHANVIEN[lib:MANV='NV03']/lib:SDT/text()", namespaces=ns)
print("NV03 (tên, sdt):", ten_nv03 + sdt_nv03)


# 6. Lấy tên món có giá > 50,000
print("Món giá có giá lớn hơn 50000:", tree.xpath("//lib:MON[lib:GIA>50000]/lib:TENMON/text()", namespaces=ns))

# 7. Lấy số bàn của hóa đơn HD03
print("Số bàn HD03:", tree.xpath("//lib:HOADON[lib:SOHD='HD03']/lib:SOBAN/text()", namespaces=ns))

# 8. Lấy tên món có mã M02
print("Tên món M02:", tree.xpath("//lib:MON[lib:MAMON='M02']/lib:TENMON/text()", namespaces=ns))

# 9. Lấy ngày lập của hóa đơn HD03
print("Ngày lập HD03:", tree.xpath("//lib:HOADON[lib:SOHD='HD03']/lib:NGAYLAP/text()", namespaces=ns))

# 10. Lấy tất cả mã món trong hóa đơn HD01
print("Mã món HD01:", tree.xpath("//lib:HOADON[lib:SOHD='HD01']//lib:CTHD/lib:MAMON/text()", namespaces=ns))

# 11. Lấy tên món trong hóa đơn HD01
mamon_hd01 = tree.xpath("//lib:HOADON[lib:SOHD='HD01']//lib:CTHD/lib:MAMON/text()", namespaces=ns)
tenmon_hd01 = [tree.xpath(f"//lib:MON[lib:MAMON='{m}']/lib:TENMON/text()", namespaces=ns)[0] for m in mamon_hd01]
print("Tên món HD01:", tenmon_hd01)

# 12. Lấy tên nhân viên lập hóa đơn HD02
manv_hd02 = tree.xpath("//lib:HOADON[lib:SOHD='HD02']/lib:MANV/text()", namespaces=ns)[0]
tennv_hd02 = tree.xpath(f"//lib:NHANVIEN[lib:MANV='{manv_hd02}']/lib:TENV/text()", namespaces=ns)[0]
print("Nhân viên lập HD02:", tennv_hd02)

# 13. Đếm số bàn
print("Số bàn:", len(tree.xpath("//lib:BAN", namespaces=ns)))

# 14. Đếm số hóa đơn lập bởi NV01
print("Số hóa đơn NV01:", len(tree.xpath("//lib:HOADON[lib:MANV='NV01']", namespaces=ns)))

# 15. Lấy tên tất cả món có trong hóa đơn của bàn số 2
mamon_ban2 = tree.xpath("//lib:HOADON[lib:SOBAN='2']//lib:CTHD/lib:MAMON/text()", namespaces=ns)
tenmon_ban2 = [tree.xpath(f"//lib:MON[lib:MAMON='{m}']/lib:TENMON/text()", namespaces=ns)[0] for m in mamon_ban2]
print("Món bàn số 2:", tenmon_ban2)

# 16. Lấy tất cả nhân viên từng lập hóa đơn cho bàn số 3
manv_ban3 = tree.xpath("//lib:HOADON[lib:SOBAN='3']/lib:MANV/text()", namespaces=ns)
tennv_ban3 = [tree.xpath(f"//lib:NHANVIEN[lib:MANV='{m}']/lib:TENV/text()", namespaces=ns)[0] for m in manv_ban3]
print("Nhân viên bàn 3:", set(tennv_ban3))

# 17. Lấy tất cả hóa đơn mà nhân viên nữ lập
nv_nu = tree.xpath("//lib:NHANVIEN[lib:GIOITINH='Nữ']/lib:MANV/text()", namespaces=ns)
hoadon_nvnu = [tree.xpath(f"//lib:HOADON[lib:MANV='{nv}']/lib:SOHD/text()", namespaces=ns) for nv in nv_nu]
print("Hóa đơn nhân viên nữ:", sum(hoadon_nvnu, []))

# 18. Lấy tất cả nhân viên từng phục vụ bàn số 1
manv_ban1 = tree.xpath("//lib:HOADON[lib:SOBAN='1']/lib:MANV/text()", namespaces=ns)
tennv_ban1 = [tree.xpath(f"//lib:NHANVIEN[lib:MANV='{m}']/lib:TENV/text()", namespaces=ns)[0] for m in manv_ban1]
print("Nhân viên bàn 1:", set(tennv_ban1))

# 19. Lấy tất cả món được gọi nhiều hơn 1 lần trong các hóa đơn
mon_more_than_1 = []
for mon in tree.xpath("//lib:MON/lib:MAMON/text()", namespaces=ns):
    total = sum(int(x) for x in tree.xpath(f"//lib:CTHD[lib:MAMON='{mon}']/lib:SOLUONG/text()", namespaces=ns))
    if total > 1:
        ten = tree.xpath(f"//lib:MON[lib:MAMON='{mon}']/lib:TENMON/text()", namespaces=ns)[0]
        mon_more_than_1.append(ten)
print("Món gọi nhiều hơn 1 lần:", mon_more_than_1)

# 20. Lấy tên bàn + ngày lập hóa đơn tương ứng SOHD='HD02'
soban_hd02 = tree.xpath("//lib:HOADON[lib:SOHD='HD02']/lib:SOBAN/text()", namespaces=ns)[0]
tenban_hd02 = tree.xpath(f"//lib:BAN[lib:SOBAN='{soban_hd02}']/lib:TENBAN/text()", namespaces=ns)[0]
ngaylap_hd02 = tree.xpath("//lib:HOADON[lib:SOHD='HD02']/lib:NGAYLAP/text()", namespaces=ns)[0]
print("Bàn và ngày lập hóa đơn:", tenban_hd02, ngaylap_hd02)
