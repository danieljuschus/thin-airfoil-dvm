from thin_airfoil_dvm.inf_coeff import inf_coeff
from thin_airfoil_dvm.grid_gen import grid_gen
import numpy as np
import pytest


@pytest.fixture
def grid_gen_outputs():
    return grid_gen("e553", 10)


class TestInfCoeff:
    """TODO: Remove the 10 (=n_panels) from the methods"""
    def test_return_type(self, grid_gen_outputs):
        """Test return type"""
        assert type(inf_coeff(10, *grid_gen_outputs)) is np.ndarray

    def test_return_shape(self, grid_gen_outputs):
        """Test shape of returned matrix"""
        assert np.shape(inf_coeff(10, *grid_gen_outputs)) == (10, 10)
