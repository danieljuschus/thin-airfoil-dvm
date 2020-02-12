import matplotlib.pyplot as plt
import numpy as np
from thin_airfoil_dvm_main import thin_airfoil_dvm


# =================================================================================================
# 3. Comparison Cambered airfoil (e553) with Symmetrical airfoil (flat plate)
# =================================================================================================

# -------------------------------------------------------------------------------------------------
# Eppler 553 pressure distribution
# -------------------------------------------------------------------------------------------------

airfoilname = "e553"
alpha_deg = 5.
alpha = alpha_deg * np.pi / 180.
q_inf = 5.
n_panels = 50
rho = 1.225

eppler_cp = thin_airfoil_dvm(airfoilname, alpha, q_inf, n_panels, rho)[0]

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
plt.title(r" Eppler 553 vs Flat plate pressure distribution, $\alpha =$ " + str(alpha_deg) + r"$ ^{\circ} $")
plt.plot(np.linspace(0, 1, n_panels), eppler_cp, 'o',  label='Eppler 553')
plt.plot(np.linspace(0, 1, n_panels), flat_plate_cp, 'x', label='Flat plate')
plt.xlabel(r'$ \frac{x}{c}$')
plt.ylabel(r'$\Delta C_p$')
plt.legend()

# -------------------------------------------------------------------------------------------------
# Inputs (Lift polar)
# -------------------------------------------------------------------------------------------------


alphas_deg = np.linspace(-5., 15., 100)
alphas = alphas_deg * np.pi / 180.
N_panels = 50

# -------------------------------------------------------------------------------------------------
# Eppler lift polar
# -------------------------------------------------------------------------------------------------

airfoilname = "e553"
Cls_eppler = []

for i in alphas:

    Cl = thin_airfoil_dvm(airfoilname, i, q_inf, n_panels, rho)[1]
    Cls_eppler.append(Cl)

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
plt.title("Lift polar comparison: Eppler 553 vs Flat plate")
plt.plot(alphas_deg, Cls_eppler, label='Eppler 553')
plt.plot(alphas_deg, Cls_flat, label='Flat plate')
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
alpha_deg = 5.
alpha = alpha_deg * np.pi / 180.
rho = 1.225
airfoilname = "e553"

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
plt.title(r" Effect of panel density on Eppler 553 pressure distribution, $\alpha =$ " + str(alpha_deg) + r"$ ^{\circ} $")
plt.plot(np.linspace(0, 1, n_low), cp_low, 'o',  label='N_panels = {}'.format(n_low))
plt.plot(np.linspace(0, 1, n_high), cp_high, 'x', label='N_panels ={}'.format(n_high))
plt.xlabel(r'$ \frac{x}{c}$')
plt.ylabel(r'$\Delta C_p$')
plt.legend()
