import numpy as np
import matplotlib.pyplot as plt
# 5 node network
A=np.array([
    [4, -1, 0, 0, 0],
    [-1, 4, -1, 0, 0],
    [0, -1, 4, -1, 0],
    [0, 0, -1, 4, -1],
    [0, 0, 0, -1, 4]
])

pressure = np.array([200.0, 150.0, 0.0, 150.0, 100.0])

def jacobi(A, pressure, tol=1e-8, max_iter=1000):
    D = np.diag(A); R =A -np.diagflat(D)
    x = np.zeros_like(pressure); errs=[]
    for _ in range(max_iter):
        x_new =(pressure- R@ x)/D
        err = np.linalg.norm(x_new - x, np.inf);errs.append(err)
        if err < tol: return x_new, errs
        x = x_new
def gauss_seidel(A, pressure, tol=1e-8, max_iter=1000):
    x = np.zeros_like(pressure); errs =[]
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(pressure)):
            x[i] = (pressure[i] - A[i, :i] @ x[:i] - A[i, i+1:]@ old[i+1:])/ A[i, i]
            err = np.linalg.norm(x - old, np.inf); errs.append(err)
            if err < tol: return x, errs
        return x, errs

x_j, e_j = jacobi(A, pressure)
x_gs, e_gs = gauss_seidel(A, pressure)
x_exact = np.linalg.solve(A, pressure)

print("Jacobi pressures:", np.round(x_j, 4))
print("Gauss-Seidel pressures:",np.round(x_gs, 4))
print("Exact solution:", np.round(x_exact, 4))
print(f"Jacobi iter: {len(e_j)}, Gauss_Seidel iter: {len(e_gs)}")

plt.semilogy(e_j, label ="Jacobi")
plt.semilogy(e_gs, label="Gauss_Seidel")
plt.xlabel("Iteration"); plt.ylabel("Max change (pressure)")
plt.title("Convergence of pipe_network solution")
plt.legend();plt.grid(True);plt.show()