class SinhVien:
    def __init__(self, id, name, sex, major, diemTB):
        self._id = id
        self._name = name
        self._sex = sex
        self._major = major
        self._diemTB = diemTB
        self._hocLuc = ""

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_sex(self):
        return self._sex

    def get_major(self):
        return self._major

    def get_diemTB(self):
        return self._diemTB

    def get_hocLuc(self):
        return self._hocLuc

    def set_hocLuc(self, hocLuc):
        self._hocLuc = hocLuc
