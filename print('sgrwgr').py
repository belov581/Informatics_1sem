import numpy as np
import matplotlib.pyplot as plt
m = 80.0
k = 0.25
g = 9.81
dt = 5.0
T = 20.0

def acceleration(v):
    return g-k/m*v**2
def euler_step (v, dt):
    return v + dt + acceleration(v)
def trapezoidal_step(v, dt):
    alpha=k+dt/(2+m)
    B=v+g+dt-alpha+v**2
    return (-1+np.sqrt(1+4*alpha*B))/(2+alpha)
def integrate(step, t, dt):
    v=np.zeros_like(t)
    for n in range(len(t)-1):
        v[n+1]=step(v[n],dt)
    return v

def analytical_solution(t):
    v_inf = np.sqrt(m * g / k)
    tau = np.sqrt(m / (g * k))
    return v_inf * np.tanh(t / tau)

n_steps = int(T / dt)
t = np.arange(n_steps + 1) * dt
v_euler = integrate(euler_step, t, dt)
v_trap = integrate(trapezoidal_step, t, dt)
v_exact = analytical_solution(t)
a_euler = acceleration(v_euler)
a_trap = acceleration(v_trap)
a_exact = acceleration(v_exact)
plt.figure()
plt.plot(t, v_euler, "o-", label="Euler")
plt.plot(t, v_trap, "o-", label="Trapezoidal")
plt.plot(t, v_exact, label="Analytical", ls="--")
plt.xlabel("t, s")
plt.ylabel("v, m/s")
plt.grid()
plt.legend()
plt.tight_layout()
plt.figure()
plt.plot(t, a_euler, "o-", label="Euler")
plt.plot(t, a_trap, "o-", label="Trapezoidal")
plt.plot(t, a_exact, label="Analytical", ls="--")
plt.xlabel("t, s")
plt.ylabel("a, m/s^2")
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
