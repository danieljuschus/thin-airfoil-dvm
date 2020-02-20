def aerodyn(vort_distr, q_inf, rho, n_panels):
    """
    Determine aerodynamic quantities from vorticity distribution.

    :param np.array vort_distr: Array with vorticity distribution
    :param float q_inf: Freestream velocity in m/s
    :param float rho: Fresstream air density in kg/m^3
    :param int n_panels: Number of panels
    :return: Pressure distribution, lift, lift coefficient, pressure coefficient distribution
    :rtype: tuple
    """
    l_distr = vort_distr*rho*q_inf
    p_distr = l_distr * n_panels  # Lift divided by panel length assuming unit chord length
    lift = sum(l_distr)
    lift_coeff = lift / (0.5*rho*q_inf**2)
    cp_distr = p_distr / (0.5*rho*q_inf**2)
    return p_distr, lift, lift_coeff, cp_distr
