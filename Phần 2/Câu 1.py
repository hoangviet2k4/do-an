import numpy as np

m = abs(int(input("Nhập số hàng m = ")))
n = abs(int(input("Nhập số cột n = ")))
def tao_ma_tran(m, n):
    x = np.random.randint(1, 5, size = (m ,n))
    y = np.random.randint(1, 5, size = (m, n))
    print("Ma trận A là :",'\n', x)
    print('Ma trận B là: ', '\n', y)
    return x, y
def tich_vector_matran(x, y):
    T = x * y
    print('Kết quả tích vector ma trận: ''\n', T)
def tich_matran(x, y):
    T = np.multiply(x, y)
    print('Kết quả tích ma trận: ', '\n' , T)
def tich_matran_chuyenvi(x, y):
    y_chuyenvi = y.T
    T = np.dot(x, y_chuyenvi)
    print('Kết quả tích ma trận chuyển vị: ', '\n', T)
def main():
    x, y = tao_ma_tran(m, n)
    tich_vector_matran(x, y)
    tich_matran(x, y)
    tich_matran_chuyenvi(x, y)
if __name__=='__main__':
    main()