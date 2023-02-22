import numpy as np

def compute_gravitational_field(metric_tensor, stress_energy_tensor):
    """
    Computes the gravitational field at each point in the grid using numerical methods, based on the Einstein field equations.
    
    Parameters:
    metric_tensor: numpy array, shape (n, n, n, n)
        The components of the metric tensor at each point in the grid.
    stress_energy_tensor: numpy array, shape (n, n, n, n)
        The components of the stress-energy tensor at each point in the grid.
    
    Returns:
    gravitational_field: numpy array, shape (n, n, n, 3)
        The components of the gravitational field at each point in the grid.
    """
    # Compute the Christoffel symbols from the metric tensor.
    n = metric_tensor.shape[0]
    gamma = np.zeros((n, n, n, n, n))
    for alpha in range(n):
        for beta in range(n):
            for mu in range(n):
                for nu in range(n):
                    gamma[alpha, beta, mu, nu, :] = 0.5 * (metric_tensor[alpha, mu, nu, :] + metric_tensor[beta, mu, nu, :] - metric_tensor[mu, nu, alpha, :] - metric_tensor[mu, nu, beta, :])
    
    # Compute the components of the gravitational field.
    gravitational_field = np.zeros((n, n, n, 3))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(3):
                    gravitational_field[i, j, k, l] = -4 * np.pi * np.sum(stress_energy_tensor[i, j, :, :] * gamma[k, l, :, :, j])    
    return gravitational_field
