# TODO: Implement argparse
from thin_airfoil_dvm.grid_gen import grid_gen
from thin_airfoil_dvm.inf_coeff import inf_coeff
from thin_airfoil_dvm.aerodyn import aerodyn
import numpy as np
import matplotlib.pyplot as plt


def thin_airfoil_dvm(airfoilname, alpha, q_inf, n_panels, rho):
    """
    Main function of the thin airfoil DVM solver. Computes

    :param airfoilname:
    :param alpha:
    :param v:
    :param n_panels:
    :param u_inf:
    :param w_inf:
    :param rho:
    :return:
    :rtype: tuple
    """
    x_vort, z_vort, x_col, z_col, norm_vec = grid_gen(airfoilname, n_panels)
    # plt.plot(x_vort, z_vort)
    # plt.axis("equal")
    # plt.title("Grid generation debug plotting")
    # plt.show()
    inf_mat = inf_coeff(n_panels, x_vort, z_vort, x_col, z_col, norm_vec)
    rhs = [-q_inf*(np.cos(np.deg2rad(alpha))*norm_i[0] + np.sin(np.deg2rad(alpha))*norm_i[1]) for norm_i in norm_vec]
    vort_dist = np.linalg.inv(inf_mat).dot(rhs)
    p_distr, lift, lift_coeff, cp_distr = aerodyn(vort_dist, q_inf, rho, n_panels)
    return cp_distr, lift_coeff


if __name__ == "__main__":
    q_inf = 5.
    n_panels = 50
    rho = 1.225
    alpha = 15
    # res = thin_airfoil_dvm("e553", alpha, q_inf, n_panels, rho)
    res = thin_airfoil_dvm("NACA4408", alpha, q_inf, n_panels, rho)
    plt.plot(np.linspace(0, 1, n_panels), res[0])
    plt.xlabel("chord fraction")
    plt.ylabel("cp")
    # alphas = range(10)
    # cls = [thin_airfoil_dvm("e553", alpha, q_inf, n_panels, rho) for alpha in alphas]
    # plt.plot(alphas, cls)
    # plt.xlabel("alpha in deg")
    # plt.ylabel("lift coefficient")
    plt.show()
