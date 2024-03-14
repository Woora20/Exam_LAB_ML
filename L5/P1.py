import numpy as np

def get_info(data):
    # Convert input data to a numpy array
    arr = np.array(data)
    
    # Create dictionary with shape and dtype information
    info = {'shape': arr.shape, 'dtype': arr.dtype}
    
    return arr, info

if __name__ == '__main__':
    x, info = get_info([1, 2, 3, 4])
    print('x =', x)
    print('info =', info)
    
    x, info = get_info([[1, 2, 3, 4]])
    print('x =', x)
    print('info =', info)
    
    x, info = get_info([[1], [2], [3], [4]])
    print('x =', x)
    print('info =', info)
    
    x, info = get_info([[1., 0], [0, 1.]])
    print('x =', x)
    print('info =', info)
    
    x, info = get_info([[2.5+1j, 1.5, 3j, 3+4.7j]])
    print('x =', x)
    print('info =', info)


# Output
# x = [1 2 3 4]
# info = {'shape': (4,), 'dtype': dtype('int32')}
# x = [[1 2 3 4]]
# info = {'shape': (1, 4), 'dtype': dtype('int32')}
# x = [[1]
#  [2]
#  [3]
#  [4]]
# info = {'shape': (4, 1), 'dtype': dtype('int32')}
# x = [[1. 0.]
#  [0. 1.]]
# info = {'shape': (2, 2), 'dtype': dtype('float64')}
# x = [[2.5+1.j  1.5+0.j  0. +3.j  3. +4.7j]]
# info = {'shape': (1, 4), 'dtype': dtype('complex128')}