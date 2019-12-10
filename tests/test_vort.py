from thin_airfoil_dvm.vort import vort
import numpy
import pytest


@pytest.fixture
def input_simple_float():
    return 1., 0., 0., 1., 1.


class TestVort:
    def test_return_type_tuple(self, input_simple_float):
        assert type(vort(*input_simple_float)) is tuple

    def test_return_type_uw(self, input_simple_float):
        assert type(vort(*input_simple_float)[0]) is numpy.float64 \
               and type(vort(*input_simple_float)[1]) is numpy.float64
