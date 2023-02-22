import numpy as np

def identify_black_holes(metric_tensor):
    """
    Identifies the locations and masses of black holes in the simulated gravitational field.
    
    Parameters:
    metric_tensor: numpy array, shape (n, n, n, 4, 4)
        The components of the metric tensor at each point in the grid.
    
    Returns:
    black_holes: list of tuples
        A list of tuples containing the position and mass of each identified black hole.
    """
    # Compute the Ricci curvature tensor from the metric tensor.
    n = metric_tensor.shape[0]
    R = np.zeros((n, n, n, 4, 4))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for a in range(4):
                    for b in range(4):
                        for c in range(4):
                            R[i, j, k, a, b] += (np.gradient(metric_tensor[i, j, k, a, c], axis=c)[b] 
                                                - 0.5*np.sum([metric_tensor[i, j, k, d, c] * 
                                                              (np.gradient(metric_tensor[i, j, k, a, d], axis=c)[b] + 
                                                               np.gradient(metric_tensor[i, j, k, b, d], axis=c)[a] - 
                                                               np.gradient(metric_tensor[i, j, k, a, b], axis=d)[c]) 
                                                              for d in range(4)], axis=0))
    
    # Identify the locations and masses of black holes using the Ricci curvature tensor.
    black_holes = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if np.abs(R[i, j, k, 0, 0]) > 1e-10:
                    mass = np.abs(R[i, j, k, 0, 0]) * (dx ** 3)
                    position = (x[i], y[j], z[k])
                    black_holes.append((position, mass))
    return black_holes
