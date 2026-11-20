import numpy as np
from scipy.linalg import lu_factor, lu_solve

Stiffness= np.array([[4.0, -1.0, 0.0],
                     [-1.0, 4.0, -1.0],
                     [0.0, -1.0, 3.0]
                     ])
load_cases={
    "walking": np.array([100.0, 50.0, 20.0]),
    "running": np.array([150.0, 80.0, 30.0]),
    "jumping": np.array([200.0, 100.0, 40.0]),
}

lu, piv = lu_factor(Stiffness)
for name, F in load_cases.items():
    d = lu_solve((lu, piv), F)
    res=np.linalg.norm(F -Stiffness@d)
    print(f"{name:8s} displacement = {np.round(d, 4)}, residual ={res:.2e} ")

print("Direct solve for comparison:", np.round(np.linalg.solve(Stiffness, load_cases["walking"]), 4))