import numpy as np
import os
import glob


def grid_gen(airfoilname, n_panels):
    """
    Import airfoil coordinates from text file, create panels on camber line and compute
    normal vectors.

    Airfoil must be specified as dat/txt file in the Lednicer format. This file must be placed in "data/airfoils/".
    TODO: Implement Selig format, implement case insensitivity in file name

    :param string airfoilname: Name of airfoil (case-sensitive, without file extension)
    :param int n_panels: Number of panels to be placed on camber line
    :return: List of tuples with unit normal vectors in (x,z)-directions
    :rtype: list
    """

    # Import airfoil coordinates as x,z lists
    path = glob.glob(os.path.join(os.getcwd(), "../data/airfoils/" + airfoilname + "*"))  # Find path of airfoil file
    if not len(path):  # Check if the file exists
        path_pytest = glob.glob(os.path.join(os.getcwd(), "data/airfoils/" + airfoilname + "*"))  # Needed for pytest
        if len(path_pytest):
            # In the current setup, pytest runs in the parent folder, so the path needs to be modified as shown
            # TODO: improve this - it's not pretty
            path = path_pytest
        else:
            raise NameError("Airfoil data file not found.")
    airfoil_data = np.genfromtxt(path[0], skip_header=3)  # Import airfoil coordinates
    idx_ul = np.argwhere(airfoil_data[:, 0] == 1)[0, 0]+1  # Index at which switch from upper to lower side takes place
    x_up, z_up = airfoil_data[:idx_ul, 0], airfoil_data[:idx_ul, 1]  # Extract upper side coordinates
    x_lo, z_lo = airfoil_data[idx_ul:, 0], airfoil_data[idx_ul:, 1]  # Extract lower side coordinates

    # Compute camber line coordinates as x,z lists
    z_lo_interp = np.interp(x_up, x_lo, z_lo)  # Interpolate lower z-coordinates at upper x-coordinates
    x_camber = x_up  # Camber line will be evaluated at upper x-coordinates
    z_camber = [z_lo_interp[i]+(z_up[i]-z_lo_interp[i])*0.5 for i in range(len(x_camber))]  # Compute camber z-coords.

    # Compute collocation points of N panels as x,z lists
    x_col = [x + 0.75/n_panels for x in np.linspace(0, 1, n_panels+1)[:-1]]  # Determine x-coordinates of coll. pts.
    z_col = np.interp(x_col, x_camber, z_camber)  # Compute collocation point z-coordinates

    # Compute normal unit vectors at collocation points as list of tuples (x,z) using "real" camber line. Note that
    # linear interpolation is used between the camber line points, so this is not truly analytical.
    # Other option: using the camber line panels defined by n_panels:
    # alphas = [np.tan((z_col[i+1]-z_col[i])/(x_col[i+1]-x_col[i])) for i in range(n_panels)]
    # norm_vec = [(np.sin(alpha_i), np.cos(alpha_i)) for alpha_i in alphas]
    idx = [np.argwhere(x_camber > x_col_i)[0, 0] for x_col_i in x_col]  # find indices of coll. pts. in camber x list
    alphas = [np.tan((z_camber[i]-z_camber[i-1])/(x_camber[i]-x_camber[i-1])) for i in idx]  # Compute alpha
    norm_vec = [(-np.sin(alpha_i), np.cos(alpha_i)) for alpha_i in alphas]
    return norm_vec


if __name__ == "__main__":
    res = grid_gen("e553", 10)
