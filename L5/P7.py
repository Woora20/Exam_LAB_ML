import numpy as np

def plane3d(Px, Py, n, k):
    nx, ny, nz = n
    return (k - nx * Px - ny * Py) / nz

if __name__ == '__main__':
    # Plane
    n = np.array([0.57735027, 0.57735027, 0.57735027])
    k = 3

    # Points on a plane
    x, y = 0, 0
    z = plane3d(x, y, n, k)
    print(f'p = ({x}, {y}, {z})')

    xs = np.linspace(-2, 2, 3)
    ys = np.linspace(-2, 2, 3)
    X, Y = np.meshgrid(xs, ys)
    Z = plane3d(X, Y, n, k)

    for i in range(3):
        for j in range(3):
            print(f'ps = ({X[i,j]}, {Y[i,j]}, {Z[i,j]})')

# Output
# p = (0, 0, 5.1961524154132634)
# ps = (-2.0, -2.0, 9.196152415413264)
# ps = (0.0, -2.0, 7.1961524154132634)
# ps = (2.0, -2.0, 5.1961524154132634)
# ps = (-2.0, 0.0, 7.1961524154132634)
# ps = (0.0, 0.0, 5.1961524154132634)
# ps = (2.0, 0.0, 3.1961524154132634)
# ps = (-2.0, 2.0, 5.1961524154132634)
# ps = (0.0, 2.0, 3.1961524154132634)
# ps = (2.0, 2.0, 1.1961524154132632)
