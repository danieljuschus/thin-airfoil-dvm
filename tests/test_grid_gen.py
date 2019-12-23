# TODO: is there a way to not run grid_gen with the same input for every test?
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
        assert type(grid_gen("e553", 10)) is list

    def test_return_type_tuple(self):
        assert all(isinstance(n, tuple) for n in grid_gen("e553", 10))

    def test_return_list_length(self):
        assert len(grid_gen("e553", 10)) == 10

    # test return type float?
