import numpy as np
import glob
import os
import matplotlib.pyplot as plt


def XFOIL_cp_extraction(filename):
    path = glob.glob(os.path.join(os.getcwd(), "../data/XFOIL_data/" + filename + "*"))
    data = np.genfromtxt(path[0], skip_header=3)
    idx_ul = np.argwhere(data[:, 1] <= 0)[0, 0]
    distr_up = data[:idx_ul]
    distr_lo = np.flip(data[idx_ul:], 0)
    cps = distr_lo[:, 2] - distr_up[:, 2]
    cp_distr = [distr_lo[:, 0], cps.reshape(-1, 1)]
    return cp_distr


if __name__ == "__main__":
    xfoildata = "NACA0015_cp_alpha0"
    cp_distr = XFOIL_cp_extraction(xfoildata)
    plt.figure()
    plt.plot(cp_distr[0], cp_distr[1])
    plt.show()