
import os
import pandas as pd
import matplotlib.pyplot as plt


class Plotter:
    def draw_plots(self, json_file):
        df = pd.read_json(json_file)

        # Plot and save comparisons
        plots = []
        columns = df.columns

        for column in columns:
            if column not in ["Gt_corners", "Rb_corners"]:
                fig, ax = plt.subplots()
                ax.plot(df["Gt_corners"], df[column], "o")
                ax.set_xlabel("Ground Truth Corners")
                ax.set_ylabel(column)
                plot_path = os.path.join("plots", f"{column}_comparison.png")
                plt.savefig(plot_path)
                plots.append(plot_path)

        return plots
