import numpy as np
import pandas as pd
# import natsort # not working
from ..functions.utils import *


def test_find_middle_even():
    # test if a given even array return the right index
    test_array = np.arange(912)
    middle = 456
    output_to_test = find_middle(test_array)
    assert middle == output_to_test

def test_find_middle_odd():
    # test if a given odd array return the right index
    test_array = np.arange(129)
    middle = 64
    output_to_test = find_middle(test_array)
    assert middle == output_to_test

def test_realign_max():
    d1 = np.arange(9)
    d2 = np.arange(6)
    d1 = d1 * d1[::-1]
    d2 = d2 * d2[::-1]
    true_shift = np.array([0,2])
    test_df = pd.DataFrame([d1,d2]).fillna(0).T
    d , shifts = realign_data(test_df,align='max')
    np.testing.assert_array_equal(true_shift,shifts)
    
    
def test_realign_center():
    d1 = np.arange(9)
    d2 = np.arange(6)
    d1 = d1 * d1[::-1]
    d2 = d2 * d2[::-1]
    true_shift = np.array([0,1])  
    test_df = pd.DataFrame([d1,d2]).fillna(0).T
    d , shifts = realign_data(test_df,align='center')
    np.testing.assert_array_equal(true_shift,shifts)
