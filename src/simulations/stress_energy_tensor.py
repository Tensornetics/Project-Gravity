import numpy as np

def compute_stress_energy_tensor(matter_density, matter_pressure, matter_velocity):
    """
    Computes the stress-energy tensor at each point in the grid using numerical methods, based on the matter distribution.
    
    Parameters:
    matter_density: numpy array, shape (n, n, n)
        The matter density at each point in the grid.
    matter_pressure: numpy array, shape (n, n, n)
        The matter pressure at each point in the grid.
    matter_velocity: numpy array, shape (n, n, n, 3)
        The matter velocity at each point in the grid.
    
    Returns:
    stress_energy_tensor: numpy array, shape (n, n, n, n)
        The components of the stress-energy tensor at each point in the grid.
    """
    # Compute the energy density and pressure from the matter density and pressure.
    n = matter_density.shape[0]
    energy_density = matter_density * (1 + np.sum(matter_velocity**2, axis=-1))
    energy_pressure = matter_pressure + energy_density
    
    # Compute the components of the stress-energy tensor.
    stress_energy_tensor = np.zeros((n, n, n, 4, 4))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                stress_energy_tensor[i, j, k, :3, :3] = energy_pressure[i, j, k] * np.eye(3) + energy_density[i, j, k] * np.outer(matter_velocity[i, j, k, :], matter_velocity[i, j, k, :])
                stress_energy_tensor[i, j, k, :3, 3] = matter_density[i, j, k] * matter_velocity[i, j, k, :]
                stress_energy_tensor[i, j, k, 3, :3] = matter_density[i, j, k] * matter_velocity[i, j, k, :]
                stress_energy_tensor[i, j, k, 3, 3] = energy_density[i, j, k]
    return stress_energy_tensor
