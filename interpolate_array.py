import numpy as np
from scipy.interpolate import interp1d

def interpolate(array, new_length):
    new = np.linspace(0, 1, new_length)
    old = np.linspace(0, 1, array.shape[0])
    interpolated_array = np.zeros((len(new), array.shape[1]))
    for i in range(array.shape[1]):
        interp_func = interp1d(old, array[:, i], kind='linear', fill_value="extrapolate")
        interpolated_array[:, i] = interp_func(new)
    return interpolated_array

