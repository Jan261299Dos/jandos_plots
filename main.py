from plotter import draw_plots


def main():
    json_file = 'C:\\Users\\Viktus\\Documents\\my_project\\deviation.json'
    plot_paths = draw_plots(json_file)
    print("Plots saved in the 'plots' folder:")
    for path in plot_paths:
        print(path)


if __name__ == "__main__":
    main()

