<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:ss="urn:schemas-microsoft-com:office:spreadsheet">
    <xsl:output method="xml" indent="yes"/>
    <xsl:template match="/">
        <Workbook xmlns="urn:schemas-microsoft-com:office:spreadsheet">
            <Worksheet ss:Name="Sheet1">
                <Table>
                    <Row>
                        <Cell><Data ss:Type="String">IF Serial</Data></Cell>
                        <Cell><Data ss:Type="String">LB Serial</Data></Cell>
                        <Cell><Data ss:Type="String">Manu IF Serial</Data></Cell>
                        <Cell><Data ss:Type="String">Manu LB Serial</Data></Cell>
                    </Row>
                    <xsl:for-each select="Records/Record">
                        <Row>
                            <Cell><Data ss:Type="String"><xsl:value-of select="if_serial"/></Data></Cell>
                            <Cell><Data ss:Type="String"><xsl:value-of select="lb_serial"/></Data></Cell>
                            <Cell><Data ss:Type="String"><xsl:value-of select="manu_if_serial"/></Data></Cell>
                            <Cell><Data ss:Type="String"><xsl:value-of select="manu_lb_serial"/></Data></Cell>
                        </Row>
                    </xsl:for-each>
                </Table>
            </Worksheet>
        </Workbook>
    </xsl:template>
</xsl:stylesheet>