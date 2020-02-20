import math as m


def vort(circ, xi, zi, x, z):
    """
    Computes velocity induced by vortex with strength circ at any given point (x,z). The vortex is located at (xi,zi).

    :param float circ: Circulation strength of vortex in ?
    :param float xi: X-position of vortex in m
    :param float zi: Z-position of vortex in m
    :param float x: X-position in m at which induced velocities should be evaluated
    :param float z: Z-position in m at which induced velocities should be evaluated
    :return u: Induced velocity in x-direction in m/s
    :return w: Induced velocity in z-direction in m/s
    :rtype: tuple
    """
    rx = x-xi  # X-distance from vortex to point
    rz = z-zi  # Z-distance from vortex to point
    r = m.sqrt(rx**2+rz**2)  # Distance from vortex to point
    u = circ/(2*m.pi*r**2)*rz  # Induced velocity in x-direction
    w = -circ/(2*m.pi*r**2)*rx  # Induced velocity in z-direction
    return u, w
