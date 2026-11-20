import numpy as np
import matplotlib.pyplot as plt
time=np.array([0,1,2,3,4,5,6,7,8])
speed=np.array([0.0,3.0,6.5,10.2,13.8,17.0,19.5,21.3,22.5])
accel=np.zeros_like(speed)
accel[0]=(speed[1])-speed[0]/(time[1]-time[0])
for i in range(1, len(time)-1):
    accel[i]=(speed[i+1]-speed[i-1]/time[i+1]-time[i-1])
accel[-1]=(speed[-1]-speed[-2]/(time[-1]-time[-2]))
for t,v,a in zip(time,speed,accel):
    print(f"t={t:.0f}s v={v:5.1f}m/s a={a:.2f}m/s^2")
plt.plot(time,accel,marker="o")
plt.xlabel("Time(s)")
plt.ylabel("Acceleration (m/s^2)")
plt.title("Acceleration from radar speed data")
plt.grid(True)
plt.show()
