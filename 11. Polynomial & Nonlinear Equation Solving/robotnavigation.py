import numpy as np
from scipy.optimize import root
def equations(z):
    x,y=z
    return[
        x**2 + y**2 -4,
        ((x-1)/1.5)**2 +((y-0.5)/1.0)**2 -1
    ]

for guess in ([2,0],[-2,0],[0,2],[0,-2]):
    sol = root(equations, guess)
    x,y=sol.x
    res=np.linalg.norm(equations(sol.x))
    print(f"Guess {guess} ---> intersection({x:+.4f},{y:+.4f}),"
          f"residual ={res:.2e}")