import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("results", exist_ok=True)

# Simple 2-DOF planar arm (for visualization)
L1, L2 = 10.0, 8.0  # link lengths (arbitrary units)

# Key poses (deg): pick -> transit -> place -> home
key_poses = [
    (20, 30),
    (40, 60),
    (80, 40),
    (15, 20)
]

def slerp(a, b, steps=20):
    a, b = np.deg2rad(a), np.deg2rad(b)
    return np.rad2deg(np.linspace(a, b, steps))

traj = []
for i in range(len(key_poses)-1):
    a1, a2 = key_poses[i]
    b1, b2 = key_poses[i+1]
    th1 = slerp(a1, b1, 25)
    th2 = slerp(a2, b2, 25)
    for t1, t2 in zip(th1, th2):
        traj.append((t1, t2))

traj = np.array(traj)
# Forward kinematics to end-effector path
def fk(theta1_deg, theta2_deg):
    t1 = np.deg2rad(theta1_deg)
    t2 = np.deg2rad(theta2_deg)
    x = L1*np.cos(t1) + L2*np.cos(t1+t2)
    y = L1*np.sin(t1) + L2*np.sin(t1+t2)
    return x, y

xy = np.array([fk(t1, t2) for t1, t2 in traj])
x, y = xy[:,0], xy[:,1]

# Plot motion profile (angles vs step)
plt.figure()
plt.plot(traj[:,0], label="Joint 1 (deg)")
plt.plot(traj[:,1], label="Joint 2 (deg)")
plt.xlabel("Step")
plt.ylabel("Angle (deg)")
plt.title("Robotic Arm Motion Profile")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.4)
plt.savefig("results/motion_profile.png", bbox_inches="tight")
plt.close()

# Plot trajectory
plt.figure()
plt.plot(x, y, marker=".", linestyle="-")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("End-Effector Trajectory (Planar 2-DOF)")
plt.axis("equal")
plt.grid(True, linestyle="--", alpha=0.4)
plt.savefig("results/trajectory.png", bbox_inches="tight")
plt.close()

print("Generated results in ./results")