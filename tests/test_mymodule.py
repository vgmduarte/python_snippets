import pytest as pt
import numpy as np
import numpy.testing as npt

from mypackage.mymodule import myfunc

def test_myfunc():
    npt.assert_array_equal(myfunc(3), np.array([]))
    npt.assert_array_eq
    