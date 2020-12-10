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
    data_path = os.path.join(curDir, "data", "txn", "complex_readinterval_thruput")
    xlabels, series_names, series = config.parse(data_path)

    f, (ax) = plt.subplots()
    # f.set_size_inches(7.5, 4)

    xticks = range(len(xlabels))
    for i, series_name in enumerate(series_names):
        series_data = series[series_name]
        base_xticks = range(len(series_data))
        ax.plot(base_xticks, series_data,  config.fmts[series_name], **config.line_opts[series_name])
    
    # ax.set_title("Throughput and Abort Rate")
    ax.set_xlabel('Read interval (ms)')
    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels, fontsize=15)

    ax.set_yticks(range(000, 1001, 200))

    ax.set_ylim([000, 900])
    ax.set_ylabel("tps")

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