import numpy as np
import matplotlib.pyplot as plt
half_life, N0=8.0,100.0
lam=np.log(2)/half_life
h,t_end=1.0,40.0
time=np.arange(0,t_end+h, h)
N=np.zeros_like(time)
N[0]=N0

for i in range (len(time)-1):
    N[i+1]=N[i]+h*(-lam*N[i])

exact=N0*np.exp(-lam*time)
print(f"N(40d) Euler: {N[-1]:.4f} mg")
print(f"N(40d) Exact: {exact[-1]:.4f} mg")
print(f"Absolute error: {abs(N[-1]):.4f} mg")

plt.plot(time,N,"o-",label="Euler")
plt.plot(time,exact,label="Exact")
plt.xlabel("Time(days)")
plt.ylabel("Amount remaining (mg))")
plt.title("Radioactive decay (Iodine-131)")
plt.grid(True)
plt.show()