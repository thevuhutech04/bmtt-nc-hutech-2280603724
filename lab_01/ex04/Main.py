from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:
    print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("************************************************************")
    print("**  1. Nhập sinh viên                                     **")
    print("**  2. Cập nhật sinh viên theo ID                         **")
    print("**  3. Xóa sinh viên theo ID                              **")
    print("**  4. Tìm kiếm sinh viên theo tên                        **")
    print("**  5. Sắp xếp sinh viên theo điểm trung bình             **")
    print("**  6. Hiển thị danh sách sinh viên                       **")
    print("**  0. Thoát chương trình                                 **")
    print("************************************************************")

    key = int(input("Nhập lựa chọn của bạn: "))

    if key == 1:
        qlsv.nhapSinhVien()
        print("Thêm sinh viên thành công.")
    elif key == 2:
        ID = int(input("Nhập ID sinh viên: "))
        qlsv.updateSinhVien(ID)
    elif key == 3:
        ID = int(input("Nhập ID sinh viên cần xóa: "))
        qlsv.deleteByID(ID)
    elif key == 4:
        name = input("Nhập tên sinh viên cần tìm: ")
        searchResult = qlsv.findByName(name)
        qlsv.showSinhVien(searchResult)
    elif key == 5:
        qlsv.sortByDiemTB()
        qlsv.showSinhVien(qlsv.listSinhVien)
    elif key == 6:
        qlsv.showSinhVien(qlsv.listSinhVien)
    elif key == 0:
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại.")
