import numpy as np
from thin_airfoil_dvm.vort import vort


def inf_coeff(n_panels, x_vort, z_vort, x_col, z_col, norm_vec):
    """
    Determines influence coefficients.

    :param n_panels: Number of panels
    :param x_vort: List of x-coordinates of vortex points
    :param z_vort: List of z-coordinates of vortex points
    :param x_col: List of x-coordinates of collocation points
    :param z_col: List of z-coordinates of collocation points
    :param norm_vec: List of normal vectors
    :return: Influence coefficient matrix
    :rtype: np.array
    """
    inf_mat = np.empty((n_panels, n_panels))
    for i in range(n_panels):  # For each collocation point
        for j in range(n_panels):  # For each vortex
            u, w = vort(1., x_vort[j], z_vort[j], x_col[i], z_col[i])
            inf_mat[i, j] = u*norm_vec[i][0] + w*norm_vec[i][1]  # Determine influence coefficient and add to matrix
    return inf_mat
