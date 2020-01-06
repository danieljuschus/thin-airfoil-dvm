# TODO: is there a way to not run grid_gen with the same input for every test?
# TODO: use fixture
from thin_airfoil_dvm.grid_gen import grid_gen
import pytest


class TestGridGen:
    def test_file_not_found(self):
        """Test exception if wrong airfoil name used as input"""
        with pytest.raises(NameError):
            grid_gen("some_wrong_airfoil_name", 10)

    def test_return_type(self):
        """Test return type
        TODO: Somehow make sure that this test still works if data/airfoils/ is empty"""
        assert type(grid_gen("e553", 10)) is tuple

    def test_return_type_lists(self):
        """Test if all elements within returned tuple are lists"""
        assert all(isinstance(res_n, list) for res_n in grid_gen("e553", 10)[:-1])

    def test_return_type_norm_vec(self):
        """Test if norm_vec list consists of tuples"""
        assert all(isinstance(n, tuple) for n in grid_gen("e553", 10)[-1])

    def test_return_list_length(self):
        """Test is all returned list have right length"""
        assert all(len(res_n) == 10 for res_n in grid_gen("e553", 10))

    # test return type float?
