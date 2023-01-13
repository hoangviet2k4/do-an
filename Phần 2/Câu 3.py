import numpy as np
import matplotlib.pyplot as plt

def dao_ham_y1(a, b, c, x):
    y1 = a*x**4 - b*x**2 - c
    return y1
def dao_ham_y2(a, b, c, x):
    y2 = (a*4*x**3) - (b*2*2*x) - (c*0)
    return y2
def dao_ham_y3(a, b, c, x):
    y3 = (a*4*3*x**2) - (b*2*2*0) - (c*0)
    return y3
def dao_ham_y4(a, b, c, x):
    y4 = (a*4*3*2*x) - (b*2*2*0) - (c*0)
    return y4
def main():
    fig, ax = plt.subplots()
    x = np.linspace(start=-10.0, stop=10.0, num=50)
    y1 = dao_ham_y1(1, -2, 3, x)
    y2 = dao_ham_y2(1, -2, 3, x)
    y3 = dao_ham_y3(1, -2, 3, x)
    y4 = dao_ham_y4(1, -2, 3, x)
    ax.plot(x, y1)
    ax.plot(x, y2)
    ax.plot(x, y3)
    ax.plot(x, y4)
    ax.plot(x,y1, label=r'$y=x^{4}-2x^{2}-3$', marker='o', markersize=5)
    ax.plot(x,y2, label=r'$y=4x^{3} - 4x$', marker='.', markersize=5)
    ax.plot(x,y3, label=r'$y=12x^{2}-4$', marker='*', markersize=5)
    ax.plot(x,y4, label=r'$y=24x $', marker='+', markersize=5)
    ax.set_title("Đồ thị phương trình")
    ax.legend()
    plt.show()
if __name__=='__main__':
    main()







