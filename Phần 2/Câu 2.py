from sympy import symbols, Eq, solve

def giai_he_phuong_trinh(a, b, c, d, e, f, g, h, j, k, l, m):
    x, y, z = symbols('x y z')
    pt1 = Eq(a * x + b * y + c * z, d)
    pt2 = Eq(e * x + f * y + g * z, h)
    pt3 = Eq(j * x + k * y + l * z, m)
    answer = solve((pt1, pt2, pt3), (x, y, z))
    print("Giải hệ phương trình : ", answer)

from sympy import *
def gioi_han(x, f, a):
  answer = limit(f, x, a)
  print('Kết quả giới hạn: ', answer)

def tinh_dao_ham(x, f):
  answer = diff(f, x)
  print('Kết quả đạo hàm: ', answer)

def nguyen_ham(x, f):
  answer = integrate(f, x)
  print('Kết quả nguyên hàm: ', answer)

def tich_phan(x, f, a, b):
  answer = integrate(f, (x, a, b))
  print('Kết quả tích phân: ', answer)

def main():
    giai_he_phuong_trinh(2, -5, 1, -5, 4, 2, -2, 2, 1, 1, -1, 0)
    x = symbols('x')
    gioi_han(x, (x * 3 - 3 * x ** 2) ** 1 / 3 + (x ** 2 - 2 * x) ** 1 / 2, +00)
    tinh_dao_ham(x, (2 * x - 1) / (x + 2))
    nguyen_ham(x, (x / (x ** 2 + 1)))
    tich_phan(x, (1 - (x ** 2 * tan(x)) / (x ** 2 + cos(x) + x)), pi, (2 * pi / 3))

if __name__=='__main__':
    main()


