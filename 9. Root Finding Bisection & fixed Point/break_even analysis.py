import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

def profit(x):
    return 25*x - 0.01 *x **2 - 1000
sol = root_scalar(profit,bracket =[10,100], method="bisect",xtol=1e-8)
print(f"Break-even qty (bisection): {sol.root:.4f} units")
print(f"profit at break-even: ${profit(sol.root):.2e}")

def g(x):
    return (1000 + 0.01 *x **2)/25.0

x= 20.0
hist=[x]
for _ in range(100):
    x_new= g(x); hist.append(x_new)
    if abs(x_new - x)< 1e-10: break
    x = x_new
print(f"Break-even qty (fixed-point): {hist[-1]:.4f} units")
print(f"Fixed-point iterations: {len(hist)-1}")

xs= np.linspace(0,120,400)
plt.plot(xs, profit(xs))
plt.axhline(0, color='k',lw=0.8)
plt.axvline(sol.root, color='r',ls='--',label =f"Break-even = {sol.root:.1f}")
plt.xlabel("Units produced"); plt.ylabel("Profits ($)")
plt.title("Break-even analysis")
plt.legend();plt.grid(True);plt.show()