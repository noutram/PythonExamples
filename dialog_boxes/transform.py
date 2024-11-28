
from lxml import etree

# Load the XML and XSLT files
xml_file = '/home/noutram/git/PythonExamples/dialog_boxes/serials.xml'
xslt_file = '/home/noutram/git/PythonExamples/dialog_boxes/transform.xslt'

xml = etree.parse(xml_file)
xslt = etree.parse(xslt_file)

# Apply the transformation
transform = etree.XSLT(xslt)
result = transform(xml)

# Save the result to a new file
output_file = '/home/noutram/git/PythonExamples/dialog_boxes/output.xml'
with open(output_file, 'wb') as f:
    f.write(etree.tostring(result, pretty_print=True))