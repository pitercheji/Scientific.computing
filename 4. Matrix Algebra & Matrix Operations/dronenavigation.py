import numpy as np

waypoints=np.array([
    [1.0, 0.0, 0.0],
    [2.0, 1.0, 0.5],
    [3.0, 1.5, 1.0]  
])

def yaw(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s, 0],[s, c, 0],[0, 0, 1]])

def pitch(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, 0, s],[0, 1, 0],[-s, 0, c]])

Rotation = pitch(np.deg2rad(30))@yaw(np.deg2rad(90))
world_points= waypoints@ Rotation.T

print("Body-frame waypoints:\n", waypoints)
print("Combined rotation matrix:\n", np.round(Rotation, 3))
print("World-frame waypoints:\n",np.round(world_points, 3))
print("Determinant(1 for pure rotation):",round(np.linalg.det(Rotation),6))