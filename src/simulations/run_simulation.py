import numpy as np
from gravitational_field import compute_gravitational_field
from metric_tensor import compute_metric_tensor
from stress_energy_tensor import compute_stress_energy_tensor

def run_simulation(n, L, matter_density, matter_pressure, matter_velocity):
    """
    Sets up and runs a simulation of the gravitational field.
    
    Parameters:
    n: int
        The number of grid points in each dimension.
    L: float
        The size of the grid in each dimension.
    matter_density: numpy array, shape (n, n, n)
        The matter density at each point in the grid.
    matter_pressure: numpy array, shape (n, n, n)
        The matter pressure at each point in the grid.
    matter_velocity: numpy array, shape (n, n, n, 3)
        The matter velocity at each point in the grid.
    
    Returns:
    gravitational_field: numpy array, shape (n, n, n, 3)
        The components of the gravitational field at each point in the grid.
    metric_tensor: numpy array, shape (n, n, n, 4, 4)
        The components of the metric tensor at each point in the grid.
    stress_energy_tensor: numpy array, shape (n, n, n, 4, 4)
        The components of the stress-energy tensor at each point in the grid.
    """
    # Compute the grid spacing and create the grid.
    dx = L / n
    x = np.linspace(-L/2, L/2, n)
    y = np.linspace(-L/2, L/2, n)
    z = np.linspace(-L/2, L/2, n)
    X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
    
    # Compute the stress-energy tensor and metric tensor.
    stress_energy_tensor = compute_stress_energy_tensor(matter_density, matter_pressure, matter_velocity)
    metric_tensor = compute_metric_tensor(np.zeros((n, n, n, 3)), stress_energy_tensor)
    
    # Compute the gravitational field.
    gravitational_field = compute_gravitational_field(metric_tensor, stress_energy_tensor)
    
    return gravitational_field, metric_tensor, stress_energy_tensor
