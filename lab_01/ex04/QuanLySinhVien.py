from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []

    def generateID(self):
        maxID = 1
        if self.soLuongSinhVien() > 0:
            maxID = max(sv.get_id() for sv in self.listSinhVien) + 1
        return maxID

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính: ")
        major = input("Nhập ngành học: ")
        diemTB = float(input("Nhập điểm trung bình: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv:
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính: ")
            major = input("Nhập ngành học: ")
            diemTB = float(input("Nhập điểm trung bình: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
            print("Cập nhật thành công.")
        else:
            print(f"Sinh viên có ID = {ID} không tồn tại.")

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x.get_id())

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x.get_name())

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x.get_diemTB())

    def findByID(self, ID):
        for sv in self.listSinhVien:
            if sv.get_id() == ID:
                return sv
        return None

    def findByName(self, keyword):
        return [sv for sv in self.listSinhVien if keyword.lower() in sv.get_name().lower()]

    def deleteByID(self, ID):
        sv = self.findByID(ID)
        if sv:
            self.listSinhVien.remove(sv)
            print("Xóa sinh viên thành công.")
            return True
        else:
            print(f"Sinh viên có ID = {ID} không tồn tại.")
            return False

    def xepLoaiHocLuc(self, sv):
        if sv.get_diemTB() >= 8:
            sv.set_hocLuc("Giỏi")
        elif sv.get_diemTB() >= 6.5:
            sv.set_hocLuc("Khá")
        elif sv.get_diemTB() >= 5:
            sv.set_hocLuc("Trung Bình")
        else:
            sv.set_hocLuc("Yếu")

    def showSinhVien(self, listSV):
        if len(listSV) == 0:
            print("Danh sách sinh viên trống.")
            return
        
        print("{:<8} {:<18} {:<10} {:<15} {:<10} {:<10}".format(
            "ID", "Tên", "Giới Tính", "Ngành Học", "Điểm TB", "Học Lực"
        ))
        print("-" * 70)
        for sv in listSV:
            print("{:<8} {:<18} {:<10} {:<15} {:<10} {:<10}".format(
                sv.get_id(), sv.get_name(), sv.get_sex(), sv.get_major(), sv.get_diemTB(), sv.get_hocLuc()
            ))
