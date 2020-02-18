import os
import glob
import numpy as np

airfoilname = "NACA4408_original"
path = glob.glob(os.path.join(os.getcwd(), "../airfoils/" + airfoilname + "*"))  # Find path of airfoil file


airfoil_data = np.genfromtxt(path[0])  # Import airfoil coordinates
idx_ul = np.argwhere(airfoil_data[:, 0] == 0)[0, 0] + 1  # Index at which switch from upper to lower side takes place
x_up, z_up = np.flip(airfoil_data[:idx_ul, 0],0), np.flip(airfoil_data[:idx_ul, 1],0)  # Extract upper side coordinates
x_lo, z_lo = airfoil_data[idx_ul:, 0], airfoil_data[idx_ul:, 1]  # Extract lower side coordinates
new_data = []

for i in xrange(len(x_up)):
    new_data.append([x_up[i], z_up[i]])

for j in xrange(len(x_lo)):
    new_data.append([x_lo[j], z_lo[j]])

np.savetxt("NACA4408.dat", new_data)
