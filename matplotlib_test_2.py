import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12, 12))

for i in range(1, 10):
    ax = fig.add_subplot(3, 3, i, projection='3d')
    
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(i * R)
    
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', linewidth=0, antialiased=False)
    ax.set_title(f'Plot {i}')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_zlim(-1.01, 1.01)
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

plt.tight_layout()
plt.show()