import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Helper function to generate markdown tables
def create_markdown_table(categories, methods, data, errors, experiment):
    table_lines = []
    table_lines.append(f"### Table for {experiment}")
    table_lines.append("| **Category**            | " + " | ".join([f"**{method}**" for method in methods]) + " |")
    table_lines.append("|--------------------------| " + " | ".join(["-----------------------------"] * len(methods)) + " |")

    for cat_idx, category in enumerate(categories):
        row = [category] + [
            f"{data[method_idx, cat_idx]:.2f} &pm; {errors[method_idx, cat_idx]:.2f}"
            for method_idx in range(len(methods))
        ]
        table_lines.append("| " + " | ".join(row) + " |")
    
    return "\n".join(table_lines)


csv = pd.read_csv("questionnaire/Human-Likeness of robotic arm with postrual synergies (Responses) - Form responses 1.csv")

# Define categories and methods
categories = ["Fake/Natural", "Machine-like/Human-like", "Unconscious/Conscious", "Artificial/Lifelike", "Moving rigidly/Moving Elegantly",
              "Doesn't make sense/Makes sense"]

methods = ["7 PCAs Trajectory", "6 PCAs Trajectory", "panda_py Trajectory", "7 PCAs Trajectory", "6 PCAs Trajectory", "panda_py Trajectory", "7 PCAs Trajectory", "6 PCAs Trajectory", "panda_py Trajectory"]
csv = csv.drop(columns=["Timestamp", "Participant number"])
columns = [col for col in csv.columns]
means = [np.mean(csv[i].values) for i in columns]
stds = [np.std(csv[i].values) for i in columns]
data = np.zeros(shape=(len(methods), len(categories)))
errors = np.zeros(shape=(len(methods), len(categories)))
data  = np.reshape(means, (data.shape[0], data.shape[1]))
errors  = np.reshape(stds, (data.shape[0], data.shape[1]))

# Define the groupings of methods for each plot
method_groups = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]  # Group 3 methods per plot

# Set the bar width
bar_width = 0.2

plt.rcParams.update({'font.size': 15})

# Create a directory to save the markdown tables
output_dir = "questionnaire/tables"
os.makedirs(output_dir, exist_ok=True)

markdown_files = []

# Plotting each set of methods across all categories in separate figures
for i, (method_idx1, method_idx2, method_idx3) in enumerate(method_groups):
    
    # Extract the relevant data and errors for the current methods
    selected_data = data[[method_idx1, method_idx2, method_idx3], :]
    selected_errors = errors[[method_idx1, method_idx2, method_idx3], :]
    selected_methods = [methods[method_idx1], methods[method_idx2], methods[method_idx3]]

    # Create markdown content for the table
    markdown_content = create_markdown_table(categories, selected_methods, selected_data, selected_errors, f"Experiment {i+1}")
    
    # Save to a markdown file
    file_path = os.path.join(output_dir, f"experiment_{i + 1}_table.md")
    with open(file_path, "w") as file:
        file.write(markdown_content)
    
    markdown_files.append(file_path)
    
    # Define the indices for the categories
    index = np.arange(len(categories))
    selected_methods = [methods[method_idx1], methods[method_idx2], methods[method_idx3]]
    
    # Create a figure for each group of methods
    fig, ax = plt.subplots(figsize=(10, 6), dpi=600)
    
    # Plot bars for each method within all categories
    for k, method_data in enumerate(selected_data):
        ax.bar(index + k * bar_width, method_data, bar_width, yerr=selected_errors[k], 
               label=selected_methods[k], capsize=3)
    
    # Set labels and title with enhanced font sizes
    ax.set_xlabel('Categories', fontsize=14)
    ax.set_ylabel('Scores', fontsize=14)
    ax.set_title(f'Comparison of Experiment {i+1} methods across all categories', fontsize=16)
    ax.set_xticks(index + bar_width)
    ax.set_xticklabels(categories, rotation=45, ha="right", fontsize=12)
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    
    # Adjust layout for better readability
    plt.tight_layout()
    
    # Save the plot as a PNG file
    plt.savefig(f"questionnaire/method_comparison_plot_{i + 1}.png")
    
    # Display the plot
    plt.show()

# Group data by summing the specified methods
grouped_data = np.array([
    np.sum(data[[0, 3, 6], :], axis=0),  # Sum of 1.1, 2.1, 3.1
    np.sum(data[[1, 4, 7], :], axis=0),  # Sum of 1.2, 2.2, 3.2
    np.sum(data[[2, 5, 8], :], axis=0),  # Sum of 1.3, 2.3, 3.3
])

# Sum errors in quadrature for each grouped method
grouped_errors = np.array([
    np.sqrt(np.sum(errors[[0, 3, 6], :] ** 2, axis=0)),  # Errors for 1.1, 2.1, 3.1
    np.sqrt(np.sum(errors[[1, 4, 7], :] ** 2, axis=0)),  # Errors for 1.2, 2.2, 3.2
    np.sqrt(np.sum(errors[[2, 5, 8], :] ** 2, axis=0)),  # Errors for 1.3, 2.3, 3.3
])
methods_all = ["7 PCAs Trajectory", "6 PCAs Trajectory", "panda_py Trajectory"]

# Create markdown content for the table
markdown_content = create_markdown_table(categories, methods_all, grouped_data, grouped_errors, "Averages of Experiments")
    
# Save to a markdown file
file_path = os.path.join(output_dir, f"avg_experiment_table.md")
with open(file_path, "w") as file:
    file.write(markdown_content)
    
markdown_files.append(file_path)

fig, ax = plt.subplots(figsize=(10, 6), dpi= 600)
for k, method_data in enumerate(grouped_data):
        ax.bar(index + k * bar_width, method_data, bar_width, yerr=grouped_errors[k], 
               label=methods_all[k], capsize=3)

ax.set_xlabel('Categories', fontsize=14)
ax.set_ylabel('Scores', fontsize=14)
ax.set_title(f'Scores for average across all categories', fontsize=16)
ax.set_xticks(index)
ax.set_xticklabels(categories, rotation=45, ha="right", fontsize=12)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.savefig(f"questionnaire/averaged_comparison.png")
plt.show()



# # Generate tables for each experiment
# markdown_files = []
# for i, (method_idx1, method_idx2, method_idx3) in enumerate(method_groups):
#     selected_methods = [methods[method_idx1], methods[method_idx2], methods[method_idx3]]
#     selected_data = data[[method_idx1, method_idx2, method_idx3], :]
#     selected_errors = errors[[method_idx1, method_idx2, method_idx3], :]
    
#     # Create markdown content for the table
#     markdown_content = create_markdown_table(categories, selected_methods, selected_data, selected_errors, i)
    
#     # Save to a markdown file
#     file_path = os.path.join(output_dir, f"experiment_{i + 1}_table.md")
#     with open(file_path, "w") as file:
#         file.write(markdown_content)
    
#     markdown_files.append(file_path)

# markdown_files
