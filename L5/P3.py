import numpy as np

def normalize(v):
    norm = np.linalg.norm(v)  # Calculate the norm of the vector
    return v / norm  # Return the normalized vector

if __name__ == '__main__':
    v = np.array([3, 4])
    u = normalize(v)
    print('u =', u)
    print('u.T @ v =', u.T @ v)
    print('size u =', np.linalg.norm(u))
    
    v = np.array([3, 4, 2])
    u = normalize(v)
    print('u =', u)
    print('u.T @ v =', u.T @ v)
    print('size u =', np.linalg.norm(u))
    
    v = np.array([3, 4, 2, 5])
    u = normalize(v)
    print('u =', u)
    print('u.T @ v =', u.T @ v)
    print('size u =', np.linalg.norm(u))

# Output
# u = [0.6 0.8]
# u.T @ v = 5.0
# size u = 1.0
# u = [0.55708601 0.74278135 0.37139068]
# u.T @ v = 5.385164807134504
# size u = 1.0
# u = [0.40824829 0.54433105 0.27216553 0.68041382]
# u.T @ v = 7.3484692283495345
# size u = 1.0