# Build kml with eTree

# https://github.com/GeospatialPython/Learning/raw/master/broken_data.gpx

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
root = ET.Element("kml")
root.attrib["xmlns"] = "http://www.opengis.net/kml/2.2"
placemark = ET.SubElement(root, "Placemark")
office = ET.SubElement(placemark, "name")
office.text = "Office"
point = ET.SubElement(placemark, "Point")
coordinates = ET.SubElement(point, "coordinates")
coordinates.text = "-89.3462521, 30.396190"
tree = ET.ElementTree(root)
tree.write("placemark.kml", xml_declaration=True,
           encoding='utf-8', method="xml")
ET.dump(tree.getroot())