<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
      xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="html" encoding="UTF-8" indent="yes"/>

  <xsl:template match="/">
    <html>
      <head>
        <title>Danh sách sinh viên</title>
        <style>
          body { font-family: Arial, sans-serif; margin: 20px; }
          table { border-collapse: collapse; width: 60%; margin-bottom: 30px; }
          th, td { border: 1px solid #333; padding: 8px; text-align: left; }
          th { background-color: #f2f2f2; }
          h2 { color: #003366; margin-bottom: 10px; }
        </style>
      </head>
      <body>
                
        <h2>1. Liệt kê thông tin của tất cả sinh viên (Mã và Họ tên)</h2>
        <table>
          <tr><th>Mã sinh viên</th><th>Họ tên</th></tr>
          <xsl:apply-templates select="school/student" mode="cau1"/>
        </table>

        <h2>2. Liệt kê danh sách sinh viên gồm mã, tên, điểm (sắp xếp theo điểm giảm dần)</h2>
        <table>
          <tr><th>Mã sinh viên</th><th>Họ tên</th><th>Điểm</th></tr>
          <xsl:for-each select="school/student">
            <xsl:sort select="grade" data-type="number" order="descending"/>
            <tr>
              <td><xsl:value-of select="id"/></td>
              <td><xsl:value-of select="name"/></td>
              <td><xsl:value-of select="grade"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <h2>3. Danh sách sinh viên sinh tháng gần nhau</h2>
        <table>
          <tr><th>STT</th><th>Họ tên</th><th>Ngày sinh</th></tr>
          <xsl:for-each select="school/student">
            <xsl:sort select="substring(date,6,2)" data-type="number"/>
            <tr>
              <td><xsl:value-of select="position()"/></td>
              <td><xsl:value-of select="name"/></td>
              <td><xsl:value-of select="date"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <h2>4. Danh sách các khóa học có sinh viên học (sắp xếp theo khóa học)</h2>
        <table>
          <tr><th>Mã khóa học</th><th>Tên khóa học</th></tr>
          <xsl:for-each select="school/course">
            <xsl:sort select="name"/>
            <xsl:variable name="cid" select="id"/>
            <xsl:if test="/school/enrollment[courseRef=$cid]">
              <tr>
                <td><xsl:value-of select="id"/></td>
                <td><xsl:value-of select="name"/></td>
              </tr>
            </xsl:if>
          </xsl:for-each>
        </table>

        <h2>5. Danh sách sinh viên đăng ký khóa học "Hóa học 201"</h2>
        <table>
          <tr><th>Mã sinh viên</th><th>Họ tên</th></tr>
          <xsl:variable name="hoaHocId" select="/school/course[name='Hóa học 201']/id"/>
          <xsl:for-each select="/school/enrollment[courseRef=$hoaHocId]">
            <xsl:variable name="sid" select="studentRef"/>
            <tr>
              <td><xsl:value-of select="$sid"/></td>
              <td><xsl:value-of select="/school/student[id=$sid]/name"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <h2>6. Danh sách sinh viên sinh năm 1997</h2>
        <table>
          <tr><th>Mã sinh viên</th><th>Họ tên</th><th>Ngày sinh</th></tr>
          <xsl:for-each select="school/student[substring(date,1,4)='1997']">
            <tr>
              <td><xsl:value-of select="id"/></td>
              <td><xsl:value-of select="name"/></td>
              <td><xsl:value-of select="date"/></td>
            </tr>
          </xsl:for-each>
        </table>

        <h2>7. Thống kê danh sách sinh viên họ “Trần”</h2>
        <table>
          <tr><th>Mã sinh viên</th><th>Họ tên</th></tr>
          <xsl:for-each select="school/student[starts-with(name,'Trần')]">
            <tr>
              <td><xsl:value-of select="id"/></td>
              <td><xsl:value-of select="name"/></td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="student" mode="cau1">
    <tr>
      <td><xsl:value-of select="id"/></td>
      <td><xsl:value-of select="name"/></td>
    </tr>
  </xsl:template>

</xsl:stylesheet>
