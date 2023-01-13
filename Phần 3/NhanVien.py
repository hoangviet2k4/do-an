import pickle
from staff import NhanVien
def nhap_danh_sach_nhan_vien(ds_nhan_vien):
    while True:
        hoten = input("Nhập họ tên nhân viên (nhập 'b' để dừng nhập): ")
        if hoten == 'b':
            break
        tuoi = int(input("Nhập tuổi nhân viên : "))
        luong = input("Nhập lương nhân viên : ")
        nhan_vien = NhanVien(hoten, tuoi, luong)
        ds_nhan_vien.append(nhan_vien)
    return ds_nhan_vien
def hien_thi_danh_sach_nhan_vien(ds_nhan_vien):
    for item in ds_nhan_vien:
        print(item)
    return item
def sap_xep_danh_sach(ds_nhan_vien):
    ds_sinh_vien = sorted(ds_nhan_vien, reverse=True)
    for item in ds_sinh_vien:
        print(item)
    return item
def luu_tap_tin_nhi_phan(ds_nhan_vien, filename):
    with open(filename,'wb') as f:
        pickle.dump(ds_nhan_vien, f)
        print("Lưu tập tin nhị phân")
def doc_tap_tin_nhi_phan(filename):
    with open(filename, 'rb') as f:
        a = f.read()
        print('Đọc tập tin nhị phân', a)
        f.close()
def main():
    ds_nhan_vien = []
    nhap_danh_sach_nhan_vien(ds_nhan_vien)
    print("Danh sách nhân viên: ")
    hien_thi_danh_sach_nhan_vien(ds_nhan_vien)
    print("Sắp xếp danh sách nhân viên: ")
    sap_xep_danh_sach(ds_nhan_vien)
    luu_tap_tin_nhi_phan(ds_nhan_vien, 'NhanVien.dat')
    doc_tap_tin_nhi_phan('NhanVien.dat')
if __name__=='__main__':
    main()
