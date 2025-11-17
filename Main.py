Import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation 
import FuncAnimation

gamma = 2 * np.pi * 41.58    
B0 = 1.5
omega0 = gamma * B0

T1, T2 = 1.2, 0.1
duration = 2.0
fps = 30
frames = int(duration * fps)
t = np.linspace(0, duration, frames)

M0 = 1.0
Mx0, My0, Mz0 = 0.0, M0, 0.0  # after 90° RF pulse

exp_T2 = np.exp(-t / T2)
exp_T1 = np.exp(-t / T1)
Mx = Mx0 * exp_T2 * np.cos(omega0*t) - My0 * exp_T2 * np.sin(omega0*t)
My = Mx0 * exp_T2 * np.sin(omega0*t) + My0 * exp_T2 * np.cos(omega0*t)
Mz = M0 - (M0 - Mz0) * exp_T1
Mxy = np.sqrt(Mx**2 + My**2)

plt.rcParams["figure.constrained_layout.use"] = True
fig = plt.figure(figsize=(10, 6))

ax3d = fig.add_subplot(2, 2, 1, projection='3d')
ax3d.set_box_aspect([1,1,1])
ax3d.set_xlim([-1, 1])
ax3d.set_ylim([-1, 1])
ax3d.set_zlim([-1, 1])
ax3d.set_title("Bloch Sphere: Magnetization M(t)")
ax3d.set_xlabel("Mx")
ax3d.set_ylabel("My")
ax3d.set_zlabel("Mz")

u, v = np.linspace(0, 2*np.pi, 40), np.linspace(0, np.pi, 20)
x_s, y_s, z_s = np.outer(np.cos(u), np.sin(v)), np.outer(np.sin(u), np.sin(v)), np.outer(np.ones_like(u), np.cos(v))
ax3d.plot_wireframe(x_s, y_s, z_s, linewidth=0.4, alpha=0.2)

ax_m = fig.add_subplot(2, 2, 2)
ax_m.set_title("Mx, My, Mz vs time")
ax_m.set_xlabel("time (s)")
ax_m.set_xlim(0, duration)
ax_m.set_ylim(-1.05*M0, 1.05*M0)
ax_m.grid(True)
line_mx, = ax_m.plot([], [], label='Mx')
line_my, = ax_m.plot([], [], label='My')
line_mz, = ax_m.plot([], [], label='Mz')
ax_m.legend()

ax_sig = fig.add_subplot(2, 1, 2)
ax_sig.set_title("Transverse signal |Mxy|")
ax_sig.set_xlabel("time (s)")
ax_sig.set_xlim(0, duration)
ax_sig.set_ylim(0, 1.05*M0)
ax_sig.grid(True)
line_sig, = ax_sig.plot([], [], lw=2)

vec_line, = ax3d.plot([0, Mx0], [0, My0], [0, Mz0], lw=3)
vec_point, = ax3d.plot([Mx0], [My0], [Mz0], 'o')

def init():
    return line_mx, line_my, line_mz, line_sig, vec_line, vec_point

def update(frame):
    mx, my, mz = Mx[frame], My[frame], Mz[frame]
    vec_line.set_data([0, mx], [0, my])
    vec_line.set_3d_properties([0, mz])
    vec_point.set_data([mx], [my])
    vec_point.set_3d_properties([mz])
    ax3d.view_init(20, (30 + frame*3) % 360)
    t_now = t[:frame+1]
    line_mx.set_data(t_now, Mx[:frame+1])
    line_my.set_data(t_now, My[:frame+1])
    line_mz.set_data(t_now, Mz[:frame+1])
    line_sig.set_data(t_now, Mxy[:frame+1])
    return line_mx, line_my, line_mz, line_sig, vec_line, vec_point

ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=False, interval=1000/fps)
plt.show()
