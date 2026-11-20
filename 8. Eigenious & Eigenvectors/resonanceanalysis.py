import numpy as np

floor_mass= 1000.0
stiffness= 4.0e5

mass_matrix= np.diag([floor_mass, floor_mass, floor_mass])
stiffness_matrix = np.array([
    [2*stiffness, -stiffness, 0],
    [-stiffness, 2*stiffness, - stiffness]
    [0, -stiffness, stiffness]
])

omega_sq, modes = np.linalg.eig(np.linalg.solve(mass_matrix, stiffness_matrix))
order = np.argsort(np.real(omega_sq))
omega_sq = np.real(omega_sq[order])
omega = np.sqrt(omega_sq)
frequency = omega/ (2*np.pi)
modes = np.real(modes[:, order])

print("Natural circular frequency(rad/s):", np.round(omega, 2))
print("Natural frequencies(Hz):", np.round(frequency, 2))
print("Mode shapes (columns = 1st, 2nd, 3rd modes):")
print(np.round(modes, 3))