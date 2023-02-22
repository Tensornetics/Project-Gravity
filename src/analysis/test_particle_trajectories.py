import numpy as np
import scipy.integrate as spi

def integrate_trajectory(gravitational_field, initial_position, initial_velocity):
    """
    Integrates the trajectory of a test particle in the simulated gravitational field.
    
    Parameters:
    gravitational_field: numpy array, shape (n, n, n, 3)
        The components of the gravitational field at each point in the grid.
    initial_position: tuple of floats
        The initial position of the test particle as a tuple (x, y, z).
    initial_velocity: tuple of floats
        The initial velocity of the test particle as a tuple (vx, vy, vz).
    
    Returns:
    trajectory: numpy array, shape (nsteps, 3)
        The position of the test particle at each time step of the integration.
    """
    # Define the function to integrate.
    def f(t, y):
        x, y, z, vx, vy, vz = y
        ax, ay, az = gravitational_field[np.argmin(np.abs(x - X)), 
                                          np.argmin(np.abs(y - Y)), 
                                          np.argmin(np.abs(z - Z))]
        return [vx, vy, vz, ax, ay, az]
    
    # Compute the grid spacing and create the grid.
    dx = x[1] - x[0]
    x = np.linspace(-L/2, L/2, n)
    y = np.linspace(-L/2, L/2, n)
    z = np.linspace(-L/2, L/2, n)
    X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
    
    # Set up the initial conditions and integration parameters.
    y0 = np.array([initial_position[0], initial_position[1], initial_position[2], 
                   initial_velocity[0], initial_velocity[1], initial_velocity[2]])
    t0 = 0
    tf = 10
    nsteps = 1000
    t = np.linspace(t0, tf, nsteps)
    
    # Integrate the trajectory.
    sol = spi.solve_ivp(f, (t0, tf), y0, t_eval=t)
    
    return sol.y[:3].T
