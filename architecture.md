# Architecture Overview

Project Gravity is a Python library for simulating and analyzing the behavior of gravity using tools from general relativity. It's designed to be modular, extensible, and easy to use, and relies on a tensor-based method for simulating the gravitational field.

## Tensor Calculus

Tensors are mathematical objects that represent physical quantities with respect to different coordinate systems. In the context of general relativity, tensors are used to represent the metric of spacetime, which describes the curvature of space and time due to the presence of matter and energy.

Tensor calculus is the branch of mathematics that deals with the manipulation of tensors. In Project Gravity, we use tensor calculus to calculate the Christoffel symbols, which are intermediate quantities that describe the curvature of spacetime. We also use tensor calculus to calculate the gravitational field at each point in the grid, based on the Einstein field equations.

## Principle of Least Action

The principle of least action is a fundamental principle in physics that states that the path taken by a particle between two points in space and time is the path that minimizes the action, which is a function that describes the particle's motion.

In Project Gravity, we use the principle of least action to calculate the trajectories of particles in the presence of a gravitational field. We start with an action functional that describes the motion of the particle, and then use the calculus of variations to derive the equations of motion.

## Simulation and Analysis

Project Gravity includes modules for simulating the gravitational field, calculating the metric tensor, and analyzing the stress-energy tensor. These modules can be combined to create customized simulations and analyses that suit a wide range of applications.

The `src/simulations` directory contains modules for simulating the gravitational field, including `gravitational_field.py`, `metric_tensor.py`, and `stress_energy_tensor.py`. These modules use numerical methods to compute the Christoffel symbols and the gravitational field at each point in the grid, based on the Einstein field equations.

The `src/analysis` directory contains modules for analyzing the trajectories of test particles and black holes, including `test_particle_trajectories.py` and `black_holes.py`. These modules use the principle of least action to calculate the trajectories of particles in the presence of a gravitational field.

The `notebooks/` directory contains Jupyter notebooks that demonstrate how to use the library and visualize the results. These notebooks provide a user-friendly interface for exploring the behavior of gravity and understanding the underlying mathematics.

## Conclusion

Project Gravity is a powerful tool for simulating and analyzing the behavior of gravity using advanced tensor-based methods. By leveraging the tools and concepts of general relativity, we can gain a deeper understanding of the behavior of matter and energy in the universe. The modular design of the library allows for easy customization and extension, and the Jupyter notebooks make it easy to visualize and explore the results of the simulations and analyses.
