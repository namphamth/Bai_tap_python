import xml.etree.ElementTree as ET

class xml_reader:
    def __init__(self,file_path):
        self.file_path = file_path
        self.data = None
# nghĩa là ban đầu, đối tượng của lớp XMLReader không chứa bất kỳ dữ liệu nào từ tệp XML
    def read_xml(self):
        tree = ET.parse(self.file_path)
        self.data = tree.getroot()
    def display_data(self):
        if self.data:
                #self.data.findall('company'): Tìm tất cả các phần tử có tên là 'sample' trong cây cú pháp.
            name_company = self.data.find('name').text
            print("Name Company",name_company)
            name_staff = self.data.findall('staff')
            for staff in name_staff :
                staff_id = staff.get('id')
                name = staff.find('name').text
                salary = staff.find('salary').text
                
                print(f"Staff_Id: {staff_id},Name Staff: {name},Salary:{salary}")

# chạy thử
path = 'sample.xml'
reader = xml_reader(path)
reader.read_xml()
reader.display_data()