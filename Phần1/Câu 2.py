import numpy
import random

m = abs(int(input('Nhập m = ')))
def tao_list_sothuc(m, a, b):
    x = [random.uniform(a, b) for i in range(m)]
    print("Sinh list số thực :", x)
    return x
def sap_xep_tang_dan(x):
    x = sorted(x, reverse=False)
    print("Sắp xếp list tăng dần : ", x)
    return x
def sap_xep_giam_dan(x):
    x = sorted(x, reverse=True)
    print("Sắp xếp list giảm dần : ", x)
    return x
def sap_xep_sothuc(x, flag):
    if flag == True:
        return sap_xep_tang_dan(x)
    else:
        return sap_xep_giam_dan(x)
def tim_kiem(x, n):
    hv = []
    for i in range(len(x)):
        if x[i] == n:
            hv.append(i)
    if len(hv) == 0:
        print("Không tìm thấy số n trong list")
    else:
        print("Tìm thấy số n trong list tại các vị trí: ", hv)
def luu_tap_tin_vanban(x, file):
    with open(file, 'w') as f:
        for item in x:
            f.write('%s/n'%item)
    print('Tập tin văn bản: ')
def luu_tap_tin_vanban2(x, file):
    with open(file, 'a+') as f:
        for item in x:
            f.write('%s/n'%item)
    print('Tập tin văn bản: ')
def luu_tap_tin_nhiphan(x, file):
    with open(file, 'wb') as f:
        for item in x:
            chuyendoi = int(item)
            f.write(chuyendoi.to_bytes(8, 'big'))
    print('Tập tin nhị phân: ')
def main():
    x = tao_list_sothuc(m, 2, 16)
    luu_tap_tin_vanban(x, r'D:/Đồ án/doan1.txt')
    f = sap_xep_sothuc(x, False)
    luu_tap_tin_vanban2(f, r'D:/Đồ án/doan1.txt')
    tim_kiem(x, 2)
if __name__ == '__main__':
    main()

