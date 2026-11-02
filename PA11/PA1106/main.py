# PA1106 - SCRAPING USING LIBRARIES
# reading XML from a file and parsing it using ElementTree library


# Import the required libraries 

import xml.etree.ElementTree as ET
tree = ET.parse("student.xml")
root = tree.getroot()
print("Root element:", root.tag)

for student in root.findall("student"):
    name = student.find("name").text
    course = student.find("course").text
    age = student.find("age").text
    gender = student.find("gender").text
    print("Name:", name)
    print("Course:", course)
    print("Age:", age)
    print("Gender:", gender)