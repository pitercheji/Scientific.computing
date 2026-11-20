import numpy as np
from scipy.optimize import minimize

def neg_profit(z):
    x,y=z
    return-(40*x+30*y)
def labour(z):
    return 80-(2*z[0]+z[1])
def machine(z):
    return 100-(z[0]+z[1])

cons=[{"type":"ineq","fun":labour},
      {"type":"ineq","fun":machine}]
sol=minimize(neg_profit,x0=[10,10],method="SLSQP",
             bounds=[(0,None),(0,None)], constraints=cons)

x,y=sol.x
print(f"Optimal A: {x:.3f},B:{y:.3f}")
print(f"Max profit: ${-sol.fun:.2f}")
print(f"Labour used: {2*x +y:.2f}/80")
print(f"Machine used: {x+2*y:.2f}/100")

best=max(((40*a+30*b, a,b)
          for a in range(50)
          for b in range (50)
          if 2*a +b<=80 and a+2*b<=100))
print(f"Best integer plan: A={best[1]},B={best[2]}")