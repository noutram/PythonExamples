<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="text" encoding="UTF-8"/>
    
    <!-- Root template -->
    <xsl:template match="/">
        <!-- Header row -->
        <xsl:text>IF Serial,LB Serial,MF Serial,MF Serial</xsl:text>
        <xsl:text>&#10;</xsl:text>
        
        <!-- Data rows -->
        <xsl:for-each select="root/Records">
            <xsl:value-of select="if_serial"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="lb_serial"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="manu_if_serial"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="manu_lb_serial"/>
            <xsl:text>&#10;</xsl:text>            
        </xsl:for-each>
    </xsl:template>
</xsl:stylesheet>