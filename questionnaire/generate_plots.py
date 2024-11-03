import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

csv = pd.read_csv("questionnaire/Human-Likeness of robotic arm with postrual synergies (Responses) - Form responses 1.csv")

# Define categories and methods
categories = ["Fake/Natural", "Machine-like/Human-like", "Unconscious/Conscious", "Artificial/Lifelike", "Moving rigidly/Moving Elegantly",
              "Doesn't make sense/Makes sense"]

methods = ["Method 1.1", "Method 1.2", "Method 1.3", "Method 2.1", "Method 2.2", "Method 2.3", "Method 3.1", "Method 3.2", "Method 3.3"]
csv = csv.drop(columns=["Timestamp", "Participant number"])
columns = [col for col in csv.columns]
means = [np.mean(csv[i].values) for i in columns]
stds = [np.std(csv[i].values) for i in columns]
data = np.zeros(shape=(len(methods), len(categories)))
errors = np.zeros(shape=(len(methods), len(categories)))
data  = np.reshape(means, (data.shape[0], data.shape[1]))
errors  = np.reshape(stds, (data.shape[0], data.shape[1]))

# Define the groupings of methods and categories for each plot
method_groups = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]  # Group 3 methods per plot
category_groups = [(0, 1, 2), (3, 4, 5)]  # Group 3 categories per plot

# Set the bar width
bar_width = 0.25

# Plotting each set of methods and categories in separate figures
for i, (method_idx1, method_idx2, method_idx3) in enumerate(method_groups):
    for j, (cat_idx1, cat_idx2, cat_idx3) in enumerate(category_groups):
        
        # Extract the relevant data and errors
        selected_data = data[[method_idx1, method_idx2, method_idx3], [cat_idx1, cat_idx2, cat_idx3]]
        selected_errors = errors[[method_idx1, method_idx2, method_idx3], [cat_idx1, cat_idx2, cat_idx3]]
        
        # Define the indices and categories for the current plot
        index = np.arange(3)
        selected_categories = [categories[cat_idx1], categories[cat_idx2], categories[cat_idx3]]
        selected_methods = [methods[method_idx1], methods[method_idx2], methods[method_idx3]]
        
        # Create a figure for each combination of method and category group
        fig, ax = plt.subplots(figsize=(8, 5))
        
        # Plot bars for each method within the selected categories
        for k, method_data in enumerate(selected_data):
            ax.bar(index + k * bar_width, method_data, bar_width, yerr=selected_errors[k], label=selected_methods[k], capsize=3)
        
        # Set labels and title
        ax.set_xlabel('Categories')
        ax.set_ylabel('Scores')
        ax.set_title(f'Comparison of {selected_methods} across {selected_categories}')
        ax.set_xticks(index + bar_width)
        ax.set_xticklabels(selected_categories)
        ax.legend(loc='upper left')
        
        plt.tight_layout()
        plt.show()