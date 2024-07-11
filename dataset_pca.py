from dataset_extractor import dataset_extractor
from scipy.interpolate import interp1d
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
import os

def interpolate_to_common_time(array, avg_time):
        common_time = np.linspace(0, 1, avg_time)
        # Function to interpolate joint angles to the common time basis
        time_points = np.linspace(0, 1, array.shape[0])
        interpolated_array = np.zeros((len(common_time), array.shape[1]))
        for i in range(array.shape[1]):
            interp_func = interp1d(time_points, array[:, i], kind='linear', fill_value="extrapolate")
            interpolated_array[:, i] = interp_func(common_time)
        return interpolated_array

def dataset_pca(folder):
    data = []
    for file in os.listdir(folder):
        if file.endswith(".xml"):
            data.append(dataset_extractor(os.path.join(folder, file)))
    
    total = sum(i.shape[0] for i in data)
    avg_time = total//len(data)

    # Interpolate all arrays to the common time basis
    interpolated_arrays = [interpolate_to_common_time(array, avg_time) for array in data]

    # Combine the interpolated data
    combined_data = np.vstack(interpolated_arrays)

    # Standardize the data
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(combined_data)
    print(f"Standardized data shape: {standardized_data.shape}")  # Should be (600, 7)

    # Apply PCA
    pca = PCA(n_components=7)  # Retain all 7 components but reduce noise
    principal_components = pca.fit_transform(standardized_data)
    print(f"Principal components shape: {principal_components.shape}")  # Should be (600, 7)

    # Inverse transform to get back to original feature space
    denoised_data = pca.inverse_transform(principal_components)
    print(f"Denoised data shape: {denoised_data.shape}")  # Should be (600, 7)

    # De-standardize the data
    denoised_data = scaler.inverse_transform(denoised_data)
    print(f"De-standardized data shape: {denoised_data.shape}")  # Should be (600, 7)

    # Reshape the denoised data back into individual iterations
    # Average the denoised data over the common time basis
    final_data = np.zeros((avg_time, 7))
    for i in range(0, avg_time*len(data), avg_time):
        final_data += denoised_data[i:i+avg_time]
    final_data /= len(data)
    print(f"Final averaged data shape: {final_data.shape}")  # Should be (100, 7)

    # Output the final set
    print(final_data.shape)
    return final_data