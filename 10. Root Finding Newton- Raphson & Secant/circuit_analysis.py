import numpy as np
from scipy.optimize import root_scalar
Vs,R,Is,nVt=5.0,100.0,1e-12,0.026
def f(Vd):
    Id=Is*(np.exp(Vd/nVt)-1)
    return Id-(Vs-Vd)/R
def df(Vd):
    return Is/nVt * np.exp(Vd/nVt)*1/R
newton =root_scalar(f, fprime=df,x0=0.7,method="newton",xtol=1e-12)
secant=root_scalar(f,x0=0.6,x1=0.75,method="secant",xtol=1e-12)

Id=Is*(np.exp(newton.root/nVt)-1)
print(f"V_D(Newton): {newton.root:.6f} V")
print(f"V_D(Secant): {secant.root:.6f} V")
print("Diode current: {Id*1000:.3f} mA")
print(f"Resistor Volatage drop: {(Vs -newton.root):.4f}")