from thin_airfoil_dvm.grid_gen import grid_gen
from thin_airfoil_dvm.inf_coeff import inf_coeff
from thin_airfoil_dvm.aerodyn import aerodyn
import numpy as np


def thin_airfoil_dvm(airfoilname, alpha, q_inf, n_panels, rho):
    """
    Main function of the thin airfoil DVM solver. Computes

    :param str airfoilname: Name of the airfoil. Needs to be present in data/airfoils. Case-sensitive.
    :param float alpha: Angle of attack in degrees
    :param float q_inf: Freestream velocity in m/s
    :param int n_panels: Number of panels for grid generation
    :param float rho: Freestream air density in kg/m^3
    :return: delta cp distribution, lift coefficient
    :rtype: tuple
    """
    # Determine vorticity and collocation points and normal vectors from airfoil
    x_vort, z_vort, x_col, z_col, norm_vec = grid_gen(airfoilname, n_panels)
    # Determine influence coefficient matrix
    inf_mat = inf_coeff(n_panels, x_vort, z_vort, x_col, z_col, norm_vec)
    # Determine right hand side of equation
    rhs = [-q_inf*(np.cos(np.deg2rad(alpha))*norm_i[0] + np.sin(np.deg2rad(alpha))*norm_i[1]) for norm_i in norm_vec]
    # Solve system for vorticity distribution
    vort_dist = np.linalg.inv(inf_mat).dot(rhs)
    # Determine aerodynamic quantities
    p_distr, lift, lift_coeff, cp_distr = aerodyn(vort_dist, q_inf, rho, n_panels)
    return cp_distr, lift_coeff
