import numpy as np
import pandas as pd
from sklearn.decomposition import PCA as pca
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

class PCA:
    def __init__(self, data, n_components):
        self.data = data
        self.n_components = n_components
        self.pca = pca(self.n_components)
        self.explained_variance = None
        self.cumulative_variance = None
        self.data_reconstructed = None
        self.scaler = StandardScaler()
        self.joint_limits = [(2.8973,-2.8973), (1.7628,-1.7628), (2.8973,-2.8973), (-0.0698, -3.0718), (2.8973,-2.8973), (3.7525,-0.0175), (2.8973,-2.8973)]

    def print_original_data(self):
        # Print the PCA data
        data_df = pd.DataFrame(data=self.data, columns=[f'Joint {i+1}' for i in range(self.data.shape[1])])
        print(data_df.head())

    def pca_calculation(self):
        # Standardizing the data
        self.data_standardized = self.scaler.fit_transform(self.data)
    
        # Performing PCA
        self.pca_result = self.pca.fit_transform(self.data_standardized)

        # Explained variance
        self.explained_variance = self.pca.explained_variance_ratio_

        # Cumulative explained variance
        self.cumulative_variance = np.cumsum(self.explained_variance)
        return self.pca.components_

    def pca_plot(self):
        # Plotting PCAs
        plt.figure(figsize=(8, 6))
        plt.plot(range(1, self.n_components + 1), self.explained_variance, marker='o', label='Explained Variance')
        plt.plot(range(1, self.n_components + 1 ), self.cumulative_variance, marker='s', label='Cumulative Variance')
        plt.xlabel('Principal Component')
        plt.ylabel('Variance Ratio')
        plt.title('Explained Variance by Principal Components')
        plt.legend()
        plt.grid(True)
        plt.show()

    def print_pca_data(self):
        # Print the PCA data
        pca_df = pd.DataFrame(data=self.pca_result, columns=[f'PC{i+1}' for i in range(self.n_components)])
        print(pca_df.head())
        print('Explained variance ratio by each component:', self.explained_variance)
        print('Cumulative explained variance ratio:', self.cumulative_variance)
    
    def get_pca_components(self):
        return self.pca.components_

    def pca_inverse_calculation(self):
        # Inverse Transform
        self.data_reconstructed = self.pca.inverse_transform(self.pca_result)
        self.data_reconstructed = self.scaler.inverse_transform(self.data_reconstructed)
        return self.data_reconstructed
    
    def inverse_pca_plot(self):
        # Plotting original vs reconstructed joints
        fig, axes = plt.subplots(7, figsize=(15,30), sharex=True)
        plt.suptitle('Original vs Reconstructed Joint Angle for Joints')
        for i, ax in enumerate(axes.flatten()):
            ax.plot(self.data[:, i], label=f'Original Joint {i+1}')
            ax.hlines(y=self.joint_limits[i][0], xmin = 0, xmax=self.data.shape[0], linewidth=1, color='r', linestyle='--')
            ax.hlines(y=self.joint_limits[i][1], xmin = 0, xmax=self.data.shape[0], linewidth=1, color='r', linestyle='--')
            ax.plot(self.data_reconstructed[:, i], label=f'Reconstructed Joint {i+1}', linestyle='--')
            ax.legend(loc='best')
            ax.grid(True)
        plt.xlabel('Time Step')
        plt.ylabel('Joint Angle')
        plt.show()

    def print_reconstructed_data(self):
        # Print the PCA data
        reconstructed_df = pd.DataFrame(data=self.data_reconstructed, columns=[f'Joint {i+1}' for i in range(self.data_reconstructed.shape[1])])
        print(reconstructed_df.head())
