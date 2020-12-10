import sys
import config
import os

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl


def main():
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""
    
    curDir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(curDir, "data", "txn", "complex_blksize_thruput")
    x_ax, series_names, series = config.parse(data_path)

    blk_sizes = x_ax
    req_rate_label = series_names[0]
    request_rate_series = series[req_rate_label]
    series_names = series_names[1:]

    f, (ax) = plt.subplots()
    # f.set_size_inches(7.5, 4)

    xticks = range(len(x_ax))
    max_xticks = {}
    max_thruputs = {}
    for i, series_name in enumerate(series_names):
        series_data = series[series_name]
        base_xticks = range(len(series_data))
        max_thruputs[series_name] = 0
        for j, r in enumerate(series_data):
            if max_thruputs[series_name] < r:
                max_thruputs[series_name] = r
                max_xticks[series_name] = j
        ax.plot(base_xticks, series_data,  config.fmts[series_name], **config.line_opts[series_name])

    max_color = "yellow" 
    for series_name in series_names:
        config.line_opts[series_name]["markerfacecolor"] = max_color
        config.line_opts[series_name]["label"] = None # Avoid generating legends
        ax.plot(max_xticks[series_name], max_thruputs[series_name],  config.fmts[series_name], **config.line_opts[series_name])
    ax.bar(0, 0, width=1, color=max_color, label="Optimal") # Fake for the legend

    # ax.set_title("Throughput and Abort Rate")
    ax.set_xlabel(r'Blk size (Request rate)')
    ax.set_xticks(xticks)
    xlabels = ["{}\n({})".format(int(blk_sizes[i]), int(request_rate_series[i])) for i in range(len(x_ax))]
    ax.set_xticklabels(xlabels, fontsize=15)

    ax.set_yticks(range(000, 1001, 200))

    ax.set_ylim([000, 900])
    ax.set_ylabel("tps")

    handles, labels = ax.get_legend_handles_labels()
    f.legend(handles, labels,
             loc='upper center', ncol=2, bbox_to_anchor=(0.53, 0.92), fontsize=18)
            #  columnspacing=1, handletextpad=1, fontsize=24)

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())