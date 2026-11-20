import numpy as np
import timeit
rng = np.random.default_rng(7)
audio=rng.uniform(-1, 1, 1_000_000)
def loop_rms():
    total=0.0
    for s in audio:
        total += s*s
    return(total/len(audio))**0.5
def vectorized_rms():
    return np.sqrt(np.mean(audio**2))
loop_time=timeit.timeit(loop_rms,number=1)
vec_time=timeit.timeit(vectorized_rms, number=1)

peak=np.max(np.abs(audio))
normalized=audio/peak

print(f"Peak amplitude: {peak:.4f}")
print(f"Vectorized RMS: {vectorized_rms():.6f}")
print(f"Loop time: {loop_time:.4f} s")
print(f"Vectorized time: {vec_time:.4f} s")
print(f"Speed_up: {loop_time/vec_time:.1f} x")
print(f"First 5 normalized samples:",normalized[:5])