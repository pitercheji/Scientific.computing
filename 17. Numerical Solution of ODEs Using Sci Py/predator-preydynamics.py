import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

alpha, beta, delta, gamma= 1.1,0.4,0.1,0.4

def lotka(t,y):
    prey,pred=y
    return[alpha*prey - beta* prey*pred,
           delta*prey*pred- gamma*pred]
sol=solve_ivp(lotka,(0,50),[10.0,5.0],
              t_eval=np.linspace(0,50,1000),
              rtol=1e-9,atol=1e-11)

print(f"solver suceess:{sol.success}")
print(f"final prey: {sol.y[0,-1]:.3f}")
print(f"final predator: {sol.y[1,-1]:.3f}")
print(f"prey range: {sol.y[0].min():.2f}-{sol.y[0].max():.2f}")
print(f"predator range: {sol.y[1].min():.2f}-{sol.y[1].max():.2f}")


plt.plot(sol.t,sol.y[0],label="prey")
plt.plot(sol.t,sol.y[1],label="predator")
plt.xlabel("Time")
plt.ylabel("population")
plt.title("predator-prey dynamics")
plt.grid(True)
plt.show()