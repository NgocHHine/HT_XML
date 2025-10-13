<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  
  <xsl:output method="html" encoding="UTF-8" indent="yes"/>
  
  <xsl:template match="/">
    <html>
      <head>
        <title>Quản lý bàn ăn</title>
        <style>
          body { font-family: Arial; margin: 20px; background-color: #f9f9f9; }
          h2 { color: darkblue; border-bottom: 2px solid #ccc; padding-bottom: 5px; }
          table { border-collapse: collapse; width: 100%; margin-bottom: 30px; background: white; }
          th, td { border: 1px solid #ccc; padding: 6px 10px; text-align: left; }
          th { background: #dce6f1; }
        </style>
      </head>
      
      <body>
        
        <h2>1. Danh sách tất cả các bàn</h2>
        <table>
          <tr><th>STT</th><th>Số bàn</th><th>Tên bàn</th></tr>
          <xsl:for-each select="QUANLY/BANS/BAN">
            <tr>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="SOBAN"/></td>
              <td><xsl:value-of select="TENBAN"/></td>
            </tr>
          </xsl:for-each>
        </table>
        
        <h2>2. Danh sách nhân viên</h2>
        <table>
          <tr><th>STT</th><th>Mã NV</th><th>Tên NV</th><th>Giới tính</th><th>SDT</th><th>Địa chỉ</th></tr>
          <xsl:for-each select="QUANLY/NHANVIENS/NHANVIEN">
            <tr>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="MANV"/></td>
              <td><xsl:value-of select="TENV"/></td>
              <td><xsl:value-of select="GIOITINH"/></td>
              <td><xsl:value-of select="SDT"/></td>
              <td><xsl:value-of select="DIACHI"/></td>
            </tr>
          </xsl:for-each>
        </table>
        
        <h2>3. Danh sách các món ăn</h2>
        <table>
          <tr><th>STT</th><th>Mã món</th><th>Tên món</th><th>Giá</th><th>Hình ảnh</th></tr>
          <xsl:for-each select="QUANLY/MONS/MON">
            <tr>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="MAMON"/></td>
              <td><xsl:value-of select="TENMON"/></td>
              <td><xsl:value-of select="GIA"/></td>
              <td><xsl:value-of select="HINHANH"/></td>
            </tr>
          </xsl:for-each>
        </table>
        
        <h2>4. Thông tin nhân viên NV02</h2>
        <table>
          <tr><th>Mã NV</th><th>Tên NV</th><th>SDT</th><th>Địa chỉ</th><th>Giới tính</th></tr>
          <xsl:for-each select="QUANLY/NHANVIENS/NHANVIEN[MANV='NV02']">
            <tr>
              <td><xsl:value-of select="MANV"/></td>
              <td><xsl:value-of select="TENV"/></td>
              <td><xsl:value-of select="SDT"/></td>
              <td><xsl:value-of select="DIACHI"/></td>
              <td><xsl:value-of select="GIOITINH"/></td>
            </tr>
          </xsl:for-each>
        </table>
        
        <h2>5. Danh sách món ăn có giá lớn hơn 50,000</h2>
        <table>
          <tr><th>STT</th><th>Mã món</th><th>Tên món</th><th>Giá</th></tr>
          <xsl:for-each select="QUANLY/MONS/MON[GIA &gt; 50000]">
            <tr>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="MAMON"/></td>
              <td><xsl:value-of select="TENMON"/></td>
              <td><xsl:value-of select="GIA"/></td>
            </tr>
          </xsl:for-each>
        </table>
        
        <h2>6. Thông tin hóa đơn HD03</h2>
        <table>
          <tr><th>Tên nhân viên</th><th>Số bàn</th><th>Ngày lập</th><th>Tổng tiền</th></tr>
          <xsl:for-each select="QUANLY/HOADONS/HOADON[SOHD='HD03']">
            <tr>
              <td><xsl:value-of select="/QUANLY/NHANVIENS/NHANVIEN[MANV=current()/MANV]/TENV"/></td>
              <td><xsl:value-of select="SOBAN"/></td>
              <td><xsl:value-of select="NGAYLAP"/></td>
              <td><xsl:value-of select="TONGTIEN"/></td>
            </tr>
          </xsl:for-each>
        </table>
        
        <h2>7. Tên các món ăn trong hóa đơn HD02</h2>
        <table>
          <tr><th>STT</th><th>Tên món</th></tr>
          <xsl:for-each select="QUANLY/HOADONS/HOADON[SOHD='HD02']/CTHDS/CTHD">
            <tr>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="/QUANLY/MONS/MON[MAMON=current()/MAMON]/TENMON"/></td>
            </tr>
          </xsl:for-each>
        </table>
        
        <h2>8. Tên nhân viên lập hóa đơn HD02</h2>
        <table>
          <tr><th>Tên nhân viên</th></tr>
          <xsl:for-each select="QUANLY/HOADONS/HOADON[SOHD='HD02']">
            <tr>
              <td><xsl:value-of select="/QUANLY/NHANVIENS/NHANVIEN[MANV=current()/MANV]/TENV"/></td>
            </tr>
          </xsl:for-each>
        </table>
        
        <h2>9. Tổng số bàn</h2>
        <p><b><xsl:value-of select="count(QUANLY/BANS/BAN)"/></b> bàn</p>
        
        <h2>10. Tổng số hóa đơn lập bởi NV01</h2>
        <p><b><xsl:value-of select="count(QUANLY/HOADONS/HOADON[MANV='NV01'])"/></b> hóa đơn</p>
        
        <h2>11. Danh sách món từng bán cho bàn số 2</h2>
        <table>
          <tr><th>STT</th><th>Tên món</th></tr>
          <xsl:for-each select="QUANLY/HOADONS/HOADON[SOBAN='2']/CTHDS/CTHD">
            <tr>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="/QUANLY/MONS/MON[MAMON=current()/MAMON]/TENMON"/></td>
            </tr>
          </xsl:for-each>
        </table>
        
        <h2>12. Nhân viên từng lập hóa đơn cho bàn số 3</h2>
        <table>
          <tr><th>STT</th><th>Tên nhân viên</th></tr>
          <xsl:for-each select="QUANLY/HOADONS/HOADON[SOBAN='3']">
            <tr>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="/QUANLY/NHANVIENS/NHANVIEN[MANV=current()/MANV]/TENV"/></td>
            </tr>
          </xsl:for-each>
        </table>
        
        <h2>13. Các món ăn được gọi nhiều hơn 1 lần trong các hóa đơn</h2>
        <table>
          <tr><th>STT</th><th>Tên món</th><th>Số lượng</th></tr>
          <xsl:for-each select="QUANLY/HOADONS/HOADON/CTHDS/CTHD[SOLUONG &gt; 1]">
            <tr>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="/QUANLY/MONS/MON[MAMON=current()/MAMON]/TENMON"/></td>
              <td><xsl:value-of select="SOLUONG"/></td>
            </tr>
          </xsl:for-each>
        </table>
        
        <h2>14. Chi tiết hóa đơn HD04</h2>
        <table>
          <tr><th>Mã món</th><th>Tên món</th><th>Đơn giá</th><th>Số lượng</th><th>Thành tiền</th></tr>
          <xsl:for-each select="QUANLY/HOADONS/HOADON[SOHD='HD04']/CTHDS/CTHD">
            <tr>
              <td><xsl:value-of select="MAMON"/></td>
              <td><xsl:value-of select="/QUANLY/MONS/MON[MAMON=current()/MAMON]/TENMON"/></td>
              <td><xsl:value-of select="/QUANLY/MONS/MON[MAMON=current()/MAMON]/GIA"/></td>
              <td><xsl:value-of select="SOLUONG"/></td>
              <td>
                <xsl:value-of select="/QUANLY/MONS/MON[MAMON=current()/MAMON]/GIA * SOLUONG"/>
              </td>
            </tr>
          </xsl:for-each>
        </table>
        
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
