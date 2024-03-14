import numpy as np

def ray(o, v, t):
    return o + t * (v - o)

if __name__ == '__main__':
    O = np.array((0,0,0))
    V = np.array((0,0,10))
    for t in (0, 0.5, 1, 1.5, 2):
        print('P =', ray(O,V,t))
    
    O = np.array((0,0,0))
    V = np.array((200,300,40))
    for t in (0, 0.5, 1, 1.5, 2):
        print('P =', ray(O,V,t))
    
    O = np.array((50,50,-10))
    V = np.array((200,300,40))
    for t in (0, 0.5, 1, 1.5, 2):
        print('P =', ray(O,V,t))

# Output
# P = [0 0 0]
# P = [0. 0. 5.]
# P = [ 0  0 10]
# P = [ 0.  0. 15.]
# P = [ 0  0 20]
# P = [0 0 0]
# P = [100. 150.  20.]
# P = [200 300  40]
# P = [300. 450.  60.]
# P = [400 600  80]
# P = [ 50  50 -10]
# P = [125. 175.  15.]
# P = [200 300  40]
# P = [275. 425.  65.]
# P = [350 550  90]