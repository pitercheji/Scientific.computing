import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
time_h=np.array([0,1,2,3,4,5,6,7,8])
pop=np.array([1.0,1.5,2.4,3.8,5.9,9.1,13.2,13.2,18.0,23.5])
def logistic(t,K,r,t0):
    return K/(1 +np.exp(-r*(t-t0)))
params,cov=curve_fit(logistic,time_h,pop,p0=[30,0.8,4])
K,r,t0=params
pred=logistic(time_h,K,r,t0)
rmse=np.sqrt(np.mean((pop-pred)**2))
print(f"Carrying capacity K = {K:.2f} thousand")
print(f"Growth rate r = {r:.3f}/h")
print(f"Infection t0 = {t0:.2f}h")
print(f"RMSE = {rmse:.2f} thousand")

t_20 =t0 +np.log(20/(K-20))/r
print(f"Predicted time to 20k: {t_20:.2f} h")
tt=np.linspace(0,12,300)
plt.plot(time_h,pop,"o",label="measured")
plt.plot(tt,logistic(tt,K,r,t0),label="fitted logistic")
plt.xlabel("Time(hours)")
plt.ylabel("Population (thousands)")
plt.title("Bacterial growth")
plt.legend()
plt.grid(True)
plt.show()