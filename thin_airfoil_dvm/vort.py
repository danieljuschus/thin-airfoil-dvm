import numpy as np


def vort(circ, xi, zi, x, z):
    """
    Computes velocity induced by vortex with strength circ at any given point (x,z). The vortex is located at (xi,zi).
    See Katz & Plotkin.

    :param float circ: Circulation strength of vortex in ?
    :param float xi: X-position of vortex in m
    :param float zi: Z-position of vortex in m
    :param float x: X-position in m at which induced velocities should be evaluated
    :param float z: Z-position in m at which induced velocities should be evaluated
    :return u: Induced velocity in x-direction in m/s
    :return w: Induced velocity in z-direction in m/s
    :rtype: float
    """

    rx = x-xi
    rz = z-zi
    r = np.sqrt(rx**2+rz**2)
    u = circ/(2*np.pi*r**2)*rz
    w = -circ/(2*np.pi*r**2)*rz
    return u, w
