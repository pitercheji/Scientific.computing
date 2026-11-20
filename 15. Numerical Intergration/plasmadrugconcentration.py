import numpy as np
from scipy.integrate import simpson
time_h=np.array([0,0.5,1,2,4,6,8,12,24])
conc=np.array([0.0,1.8,3.2,4.5,3.9,2.8,1.9,0.8,0.1])
auc_trap=np.trapezoid(conc, time_h)
auc_simp=simpson(conc, x=time_h)
print(f"AUC (trapesoidal) {auc_trap:.3f} mgh/l")
print(f"AUC (Simpson): {auc_simp:.3f} mgh/l")
print(f"Difference: {abs(auc_trap-auc_simp):.3f} mgh/l")