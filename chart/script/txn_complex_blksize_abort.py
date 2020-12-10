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
    data_path = os.path.join(curDir, "data", "txn", "complex_blksize_abort")
    x_ax, series_names, series = config.parse(data_path)

    blk_sizes = x_ax
    req_rate_label = series_names[0]
    request_rate_series = series[req_rate_label]
    series_names = series_names[1:]

    f, (ax) = plt.subplots()
    # f.set_size_inches(7.5, 4)

    xticks = range(len(x_ax))
    for i, series_name in enumerate(series_names):
        series_data = series[series_name]
        base_xticks = range(len(series_data))
        ax.plot(base_xticks, series_data,  config.fmts[series_name], **config.line_opts[series_name])

    # ax.set_title("Throughput and Abort Rate")
    ax.set_xlabel(r'Blk size (Request rate)')
    ax.set_xticks(xticks)
    xlabels = ["{}\n({})".format(int(blk_sizes[i]), int(request_rate_series[i])) for i in range(len(x_ax))]
    ax.set_xticklabels(xlabels, fontsize=15)

    ax.set_yticks([0, .25, .5, .75, 1.0])

    ax.set_ylim([0, 1.5])
    ax.set_ylabel("percent(%)")

    handles, labels = ax.get_legend_handles_labels()
    f.legend(handles, labels,
             loc='upper center', ncol=2, bbox_to_anchor=(0.54, 0.92), fontsize=18)
            #  columnspacing=1, handletextpad=1, fontsize=24)

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())