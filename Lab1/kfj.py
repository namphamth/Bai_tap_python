import xml.etree.ElementTree as ET

class XMLReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_xml(self):
        tree = ET.parse(self.file_path)
        self.data = tree.getroot()

    def display_data(self):
        if self.data:
            company_name = self.data.find('name').text
            print(f"Company Name: {company_name}")

            staff_members = self.data.findall('staff')
            for staff in staff_members:
                staff_id = staff.get('id')
                name = staff.find('name').text
                salary = staff.find('salary').text
                print(f"Staff ID: {staff_id}, Name: {name}, Salary: {salary}")

# Sử dụng lớp XMLReader để đọc và hiển thị dữ liệu
xml_reader = XMLReader("sample.xml")
xml_reader.read_xml()
xml_reader.display_data()