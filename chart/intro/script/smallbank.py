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
    data_path = os.path.join(curDir, "data", "smallbank")
    x_axis, series_names, series = config.parse(data_path)

    f, (axis) = plt.subplots()
    # f.set_size_inches(7.5, 4)

    xticks = range(len(x_axis))
    committed_series = series["Committed"]
    bottom = [0] * len(committed_series)
    axis.bar(xticks, committed_series, width=0.7, color="blue", edgecolor='black',
              label="Effective", bottom=bottom)

    bottom = config.sum_list(bottom, committed_series)
    axis.bar(xticks, series["Aborted"], width=0.7, color="red", edgecolor='black',
              label="Aborted", bottom=bottom)

    axis.tick_params(axis='both', which='major', labelsize=18)

    axis.set_title("Smallbank Throughput")

    axis.set_xlabel(r'Zipfian coefficient $\theta$')
    axis.set_xticks(xticks)
    axis.set_xticklabels(x_axis)

    axis.axvline(x=0.5, ymin=0, ymax=1, color="black", linestyle="--")

    axis.set_yticks(range(000, 1701, 400))

    axis.set_ylim([000, 2420])
    axis.set_ylabel("tps")
    # latency_ax.set_yscale("log")
    axis.yaxis.set_label_coords(-0.01,0.9)


    handles, labels = axis.get_legend_handles_labels()
    f.legend(handles, labels,
             loc='upper center', ncol=1, bbox_to_anchor=(0.52, 0.82), 
             columnspacing=1, handletextpad=1, fontsize=24)

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())