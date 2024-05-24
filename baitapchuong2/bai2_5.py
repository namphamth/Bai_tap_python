import xml.dom.minidom
def main():
    doc=xml.dom.minidom.parse("sample.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    staff = doc.getElementsByTagName("staff")
    print("%d staff :" % staff.length)
    for skill in staff :
      print(skill.getAttribute("id"))   
if __name__=="__main__" :
    main() 