from thin_airfoil_dvm.vort import vort
import pytest


@pytest.fixture
def input_simple_float():
    return 1., 0., 0., 1., 1.


class TestVort:
    def test_return_type(self, input_simple_float):
        """Test return type"""
        assert type(vort(*input_simple_float)) is tuple

    def test_return_type_uw(self, input_simple_float):
        """Test type of each velocity"""
        assert all(isinstance(n, float) for n in vort(*input_simple_float))

    def test_value(self, input_simple_float):
        """Test value of each velocity"""
        assert vort(*input_simple_float) == (0.07957747154594765, -0.07957747154594765)
