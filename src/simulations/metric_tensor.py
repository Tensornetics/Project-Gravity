import numpy as np

def compute_metric_tensor(gravitational_field, stress_energy_tensor):
    """
    Computes the metric tensor at each point in the grid using numerical methods, based on the Einstein field equations.
    
    Parameters:
    gravitational_field: numpy array, shape (n, n, n, 3)
        The components of the gravitational field at each point in the grid.
    stress_energy_tensor: numpy array, shape (n, n, n, n)
        The components of the stress-energy tensor at each point in the grid.
    
    Returns:
    metric_tensor: numpy array, shape (n, n, n, n)
        The components of the metric tensor at each point in the grid.
    """
    # Compute the inverse metric tensor from the gravitational field.
    n = gravitational_field.shape[0]
    g_inv = np.zeros((n, n, n, 3, 3))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                g_inv[i, j, k, :, :] = np.eye(3) + 2 * gravitational_field[i, j, k, :] / np.linalg.norm(gravitational_field[i, j, k, :])**2
    
    # Compute the components of the metric tensor.
    metric_tensor = np.zeros((n, n, n, 4, 4))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                metric_tensor[i, j, k, :3, :3] = g_inv[i, j, k, :, :]
                metric_tensor[i, j, k, 3, 3] = -np.sum(stress_energy_tensor[i, j, :, :]) / np.sum(gravitational_field[i, j, k, :]**2)
    return metric_tensor
