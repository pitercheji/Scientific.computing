import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt
distance_km=np.array([0,1,2,3,4,5,6,7])
elevation_m=np.array([500,620,850,1050,980,800,720,650])
linear=interp1d(distance_km, elevation_m,kind="linear")
cubic=CubicSpline(distance_km, elevation_m)

for d in (3.5, 6.2):
    print(f"At {d} km--> linear {float(linear(d)):.1f} m,"
          f"cubic {float(cubic(d)):.1f} m")

dense=np.linspace(0,7,1000)
peak=np.argmax(cubic(dense))
print(f"peak: {cubic(dense)[peak]:.1f} m at {dense[peak]:.2f} km")

plt.plot(dense,cubic(dense),label="cubic spline")
plt.plot(distance_km, elevation_m,"o",label="waypoints")
plt.plot(dense, linear(dense),"--", label="linear")
plt.xlabel("Distance (km)")
plt.ylabel("Elevation(m)")
plt.title("Trail elevation profile")
plt.legend()
plt.grid(True)
plt.show()