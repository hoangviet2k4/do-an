import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import cm

def do_thi_yen_ngua(ax):
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = (X/3)**2 - (Y/2)**2
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_title('Đồ thị mặt yên ngựa')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
def do_thi_hyperbolic(ax):
    x = np.linspace(-10, 10, 200)
    y = np.linspace(-10, 10, 200)
    x, y = np.meshgrid(x, y)
    z1 = 2*np.sqrt((x/3)**2 + (y/5)**2 - 1)
    z2 = -2*np.sqrt((x/3)**2 + (y/5)**2 - 1)
    rosen_surf1 = ax.plot_surface(x, y, z1, cmap=cm.viridis, linewidth=0, antialiased=False)
    rosen_surf2 = ax.plot_surface(x, y, z2, cmap=cm.viridis, linewidth=0, antialiased=False)
    ax.set_title('Đồ thị hyperbolic')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    return rosen_surf1, rosen_surf2
def do_thi_mat_cau(ax):
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = (np.outer(np.cos(u), np.sin(v)) * 2) - 2
    y = (np.outer(np.sin(u), np.sin(v)) * 2) + 1
    z = (np.outer(np.ones(np.size(u)), np.cos(v)) * 2) + 4
    ax.plot_surface(x, y, z, cmap='viridis')
    ax.set_title('Đồ thị mặt cầu')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
def main():
    fig = plt.figure(figsize=(12, 4))
    ax1 = fig.add_subplot(131, projection='3d')
    ax2 = fig.add_subplot(132, projection='3d')
    ax3 = fig.add_subplot(133, projection='3d')
    do_thi_yen_ngua(ax1)
    ax1.set_title('Đồ thị mặt yên ngựa')
    rosen_surf1, rosen_surf2 = do_thi_hyperbolic(ax2)
    ax2.set_title('Đồ thị hyperbolic')
    do_thi_mat_cau(ax3)
    ax3.set_title('Đồ thị mặt cầu')
    fig.colorbar(rosen_surf1, shrink=0.5, aspect=5)
    fig.colorbar(rosen_surf2, shrink=0.5, aspect=5)
    plt.show()
if __name__=='__main__':
    main()