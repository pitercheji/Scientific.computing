import numpy as np
# A: 26 g protein and 210 kcal per serving
# B: 9 g protein and 390 kcal per serving
# Target per day: 100g protein and 2200 kcal 
A= np.array([[26.0, 9.0],
             [210.0, 390.0]
             ])
B = np.array([100.0, 2200.0])

solution=np.linalg.solve(A, B)
residual= B - A @solution

print(f"Food A servings: {solution[0]:.2f}")
print(f"Food B servings: {solution[1]:.2f}")
print("verification A @ x:", A @ solution)
print("Residual norm:", np.linalg.norm(residual))