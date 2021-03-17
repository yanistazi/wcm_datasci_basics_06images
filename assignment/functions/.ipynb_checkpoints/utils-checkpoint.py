# Utility functions for processing .csv data in assignment 6
import natsort
import glob
import numpy as np
import pandas as pd
# get_files function:
def get_files(pattern):
    """ 
    Extracts file in alphanumerical order that match the provided pattern
    """
    if isinstance(pattern, list):
        pattern = os.path.join(*pattern)
        
    files = natsort.natsorted(glob.glob(pattern))
    if not files:
        raise FileNotFoundError('Pattern could not detect file(s)')
        
    return files

 
def find_middle(in_column):
    """
    Find the middle index of input data column/array
    """
    # length of the input, divide by 2 to find the middle point
    middle = float(len(in_column))/2
    # round down with `floor` in case your middle point isn't divisible by 2 (odd length)
    return int(np.floor(middle))

def realign_data(in_data, align = "max"):
    """
    Center data around maximum or center of shortest column, pad with 0's 
    Args:
        in_data: array of input data
        align (str): "max" or "center", max will provide shifts to align maximum of input  data, whereas "center" will shift to middle index.
    
    Returns:
        d - new dataframe with realigned data
        shifts - how each entry was shifted
    """
    # Create a placeholder output dataframe the same size as input, replace the 0's later with realigned data
    x, y = in_data.shape
    d = pd.DataFrame(0, index=np.arange(x), columns = np.arange(y))
    shifts = np.zeros(y)
    
    # Find longest length sample and find it's peak/midpoint
    ind_longest = np.argmin((in_data == 0).astype(int).sum(axis=0).values)
    peak_longest = np.argmax(in_data.loc[:, ind_longest].values)
    # use your find_middle function here to find the center point for the assignment
    mid_longest = find_middle(in_data.index[in_data[ind_longest]!=0].values)
    
    # arrange the rest of the data's peaks into the new dataframe lining up to longest peak or longest midpoint
    for column in in_data:
        if align == "max":
            peak = np.argmax(in_data[column].values)
            pdiff = peak_longest - peak
            d[column] = in_data[column].shift(periods=pdiff, fill_value=0)
            # check shifted max location of input is same as reference peak
            assert np.argmax(d[column]) == peak_longest
            shifts[column] = pdiff
        elif align == "center":
            print("here")
            mid = find_middle(in_data.index[in_data[column]!=0].values)   # change for part 2
            mid_diff = mid_longest - mid
            d[column] = in_data[column].shift(periods=mid_diff, fill_value=0)
#             # check shifted max location of input is same as reference peak
#             assert np.argmax(d[column]) == peak_longest
            shifts[column] = mid_diff
            # Write the alignment code here, replacing peak with the center that you found (mid_longest). 
    
    return d, shifts
