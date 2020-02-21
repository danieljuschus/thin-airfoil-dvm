import timeit
import numpy as np
import matplotlib.pyplot as plt
from thin_airfoil_dvm.thin_airfoil_dvm_main import thin_airfoil_dvm

airfoilname = "naca1408"
alpha = 15
q_inf = 5  # original: 162 fps
n_panels = np.logspace(1, 3, 25)
rho = 1.225

times = []
for n in n_panels:
    print("Computing " + str(n) + " panels")
    t0 = timeit.default_timer()
    thin_airfoil_dvm(airfoilname, alpha, q_inf, int(n), rho)
    times.append(timeit.default_timer()-t0)

plt.plot(n_panels, times)
plt.gca().set_xscale("log")
plt.grid()
plt.xlabel("Number of panels")
plt.ylabel("Execution time in s")
plt.savefig("assignment_script_images/panel_density_timing.pdf")
