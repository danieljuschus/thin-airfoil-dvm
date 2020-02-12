import numpy as np


def aerodyn(vort_distr, q_inf, rho, n_panels):
    """TODO: Add docstring and more comments
    TODO: Add unit tests"""
    l_distr = vort_distr*rho*q_inf
    p_distr = l_distr * n_panels  # Lift divided by panel length assuming unit chord length
    lift = sum(l_distr)
    lift_coeff = lift / (0.5*rho*q_inf**2)
    cp_distr = p_distr / (0.5*rho*q_inf**2)
    return p_distr, lift, lift_coeff, cp_distr

# if __name__ == "__main__":
#     Q_inf = 5.
#     alpha = 10.
#     N_panels = 50
#     U_inf = Q_inf*np.cos(alpha*np.pi/180.)
#     W_inf = Q_inf*np.sin(alpha*np.pi/180.)
#     grid = grid_gen("e553", N_panels)
#     mat = inf_coeff(grid[1], grid[2], grid[3])
#     vec = RHS(U_inf, W_inf, grid[3])
#     vort_distr = solver(mat, vec)
#     res = aerodyn(vort_distr, U_inf, W_inf, 1.225, N_panels)
#     plt.plot(np.linspace(0,1,N_panels), res[3])