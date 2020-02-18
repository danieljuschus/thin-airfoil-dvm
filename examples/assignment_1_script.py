import matplotlib.pyplot as plt
import numpy as np
from thin_airfoil_dvm.thin_airfoil_dvm_main import thin_airfoil_dvm
from scipy.interpolate import UnivariateSpline, interp1d

# =================================================================================================
# 2. Validation using results from literature
# =================================================================================================
airfoilname = "NACA4408"
alpha = 15
q_inf = 5  # original: 162 fps
n_panels = 1000
rho = 1.225

cp_calc = thin_airfoil_dvm(airfoilname, alpha, q_inf, n_panels, rho)[0]
cp_exp = np.genfromtxt("../data/wind_tunnel_data/naca4408alpha15.csv", delimiter=",")


spl_up = interp1d(cp_exp[8:22, 0], cp_exp[8:22, 1], fill_value="extrapolate")
spl_lo = interp1d(np.hstack((cp_exp[22:, 0], cp_exp[:4, 0], cp_exp[8, 0])),
                  np.hstack((cp_exp[22:, 1], cp_exp[:4, 1], cp_exp[8, 1])), fill_value="extrapolate")
x_spl = np.linspace(0.002, 1, 100)
cp_exp_dif = spl_lo(x_spl) - spl_up(x_spl)
plt.plot(np.linspace(0, 1, n_panels, endpoint=False)+1/(n_panels*4.), cp_calc, label="Calculated data")
plt.plot(x_spl, cp_exp_dif, "kx", label="Wind tunnel data")
plt.xlabel("Fraction of chord")
plt.ylabel(r"$\Delta c_p$")
plt.grid(True)
plt.legend()
plt.show()

"""
# =================================================================================================
# 3. Comparison Cambered airfoil (e553) with Symmetrical airfoil (flat plate)
# =================================================================================================

# -------------------------------------------------------------------------------------------------
# NACA4408 pressure distribution
# -------------------------------------------------------------------------------------------------

airfoilname = "NACA4408"
alpha = 5.
q_inf = 5.
n_panels = 50
rho = 1.225

NACA_cp = thin_airfoil_dvm(airfoilname, alpha, q_inf, n_panels, rho)[0]

# -------------------------------------------------------------------------------------------------
# Flat plate pressure distribution
# -------------------------------------------------------------------------------------------------

airfoilname = "flat_plate"
# alpha = 5. * np.pi / 180.
# q_inf = 5.
# n_panels = 50
# rho = 1.225

flat_plate_cp = thin_airfoil_dvm(airfoilname, alpha, q_inf, n_panels, rho)[0]

plt.figure()
plt.title(r" NACA 4408 vs Flat plate pressure distribution, $\alpha =$ " + str(alpha) + r"$ ^{\circ} $")
plt.plot(np.linspace(0, 1, n_panels), NACA_cp, 'o',  label='NACA 4408')
plt.plot(np.linspace(0, 1, n_panels), flat_plate_cp, 'x', label='Flat plate')
plt.xlabel(r'$ \frac{x}{c}$')
plt.ylabel(r'$\Delta C_p$')
plt.legend()

# -------------------------------------------------------------------------------------------------
# Inputs (Lift polar)
# -------------------------------------------------------------------------------------------------


alphas = np.linspace(-5., 15., 100)
N_panels = 50

# -------------------------------------------------------------------------------------------------
# NACA4408 lift polar
# -------------------------------------------------------------------------------------------------

airfoilname = "NACA4408"
Cls_NACA = []

for i in alphas:

    Cl = thin_airfoil_dvm(airfoilname, i, q_inf, n_panels, rho)[1]
    Cls_NACA.append(Cl)

# -------------------------------------------------------------------------------------------------
# Flat plate lift polar
# -------------------------------------------------------------------------------------------------

airfoilname = "flat_plate"
Cls_flat = []

for i in alphas:

    Cl = thin_airfoil_dvm(airfoilname, i, q_inf, n_panels, rho)[1]
    Cls_flat.append(Cl)

# -------------------------------------------------------------------------------------------------
# Lift polar plots
# -------------------------------------------------------------------------------------------------

plt.figure()
plt.title("Lift polar comparison: NACA 4408 vs Flat plate")
plt.plot(alphas, Cls_NACA, label='NACA 4408')
plt.plot(alphas, Cls_flat, label='Flat plate')
plt.xlabel(r"Angle of attack $[^{\circ}]$")
plt.ylabel(r"$C_l [-]$")
plt.legend()

# =================================================================================================
# 4. Effect of panel density
# =================================================================================================
# -------------------------------------------------------------------------------------------------
# Inputs
# -------------------------------------------------------------------------------------------------

q_inf = 5.
alpha = 5.
rho = 1.225
airfoilname = "NACA4408"

# -------------------------------------------------------------------------------------------------
# Low and high density data sets
# -------------------------------------------------------------------------------------------------
n_low = 5
cp_low = thin_airfoil_dvm(airfoilname, alpha, q_inf, n_low, rho)[0]

n_high = 50
cp_high = thin_airfoil_dvm(airfoilname, alpha, q_inf, n_high, rho)[0]

# -------------------------------------------------------------------------------------------------
# Lift polar plots
# -------------------------------------------------------------------------------------------------
plt.figure()
plt.title(r" Effect of panel density on NACA 4408 pressure distribution, $\alpha =$ " + str(alpha) + r"$ ^{\circ} $")
plt.plot(np.linspace(0, 1, n_low), cp_low, 'o',  label='N_panels = {}'.format(n_low))
plt.plot(np.linspace(0, 1, n_high), cp_high, 'x', label='N_panels ={}'.format(n_high))
plt.xlabel(r'$ \frac{x}{c}$')
plt.ylabel(r'$\Delta C_p$')
plt.legend()
"""