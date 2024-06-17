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
        self.scaler = StandardScaler()

    def pca_calculation(self):
        # Standardizing the data
        self.data_standardized = self.scaler.fit_transform(self.data)

        # Performing PCA
        self.pca_result = self.pca.fit_transform(self.data_standardized)

        # Explained variance
        self.explained_variance = self.pca.explained_variance_ratio_

        # Cumulative explained variance
        self.cumulative_variance = np.cumsum(self.explained_variance)

    def plot(self):
        # Plotting explained variance
        plt.figure(figsize=(8, 6))
        plt.plot(range(1, self.n_components + 1), self.explained_variance, marker='o', label='Explained Variance')
        plt.plot(range(1, self.n_components + 1 ), self.cumulative_variance, marker='s', label='Cumulative Variance')
        plt.xlabel('Principal Component')
        plt.ylabel('Variance Ratio')
        plt.title('Explained Variance by Principal Components')
        plt.legend()
        plt.grid(True)
        plt.show()

    def print_data(self):
        # Print the PCA data
        pca_df = pd.DataFrame(data=self.pca_result, columns=[f'PC{i+1}' for i in range(self.n_components)])
        print(pca_df.head())
        print('Explained variance ratio by each component:', self.explained_variance)
        print('Cumulative explained variance ratio:', self.cumulative_variance)
