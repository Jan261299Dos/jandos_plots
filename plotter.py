import pandas as pd
import matplotlib.pyplot as plt
import os


def draw_plots(json_file):
    # Read JSON data into a pandas DataFrame
    df = pd.read_json(json_file)

    # Create the "plots" folder if it doesn't exist
    if not os.path.exists("plots"):
        os.makedirs("plots")

    # List to store the paths of the generated plots
    plot_paths = []

    # Columns to include in the plot
    deviation_columns = ['mean', 'max', 'min', 'floor_mean', 'floor_max', 'floor_min',
                         'ceiling_mean', 'ceiling_max', 'ceiling_min']

    # Iterate over deviation columns and draw plots
    for column in deviation_columns:
        # Create a bar plot to compare different columns
        fig, ax = plt.subplots(figsize=(10, 6))
        df.plot.bar(x='name', y=[column, 'gt_corners'], ax=ax)
        ax.set_xlabel('Room')
        ax.set_ylabel(f'Deviation ({column}) / Number of corners')
        ax.set_title(f'{column} Comparison')
        plt.xticks(rotation=45)

        # Save the plot
        plot_path = os.path.join("plots", f'{column}_comparison.png')
        plt.savefig(plot_path)
        plot_paths.append(plot_path)

    # Return the paths to all plots
    return plot_paths


# Example usage
json_file = 'deviation.json'
plot_paths = draw_plots(json_file)
print("Plots saved in the 'plots' folder:")
for path in plot_paths:
    print(path)

#
# import os
# import pandas as pd
# import matplotlib.pyplot as plt
#
#
# class Plotter:
#     def draw_plots(self, json_file):
#         df = pd.read_json(json_file)
#
#         # Plot and save comparisons
#         plots = []
#         columns = df.columns
#
#         for column in columns:
#             if column not in ["Gt_corners", "Rb_corners"]:
#                 fig, ax = plt.subplots()
#                 ax.plot(df["Gt_corners"], df[column], "o")
#                 ax.set_xlabel("Ground Truth Corners")
#                 ax.set_ylabel(column)
#                 plot_path = os.path.join("plots", f"{column}_comparison.png")
#                 plt.savefig(plot_path)
#                 plots.append(plot_path)
#
#         return plots
