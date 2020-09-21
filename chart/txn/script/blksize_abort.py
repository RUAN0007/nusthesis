import sys
from common import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl

series_labels = [kOriginalLabel, kFppLabel, kFsharpLabel,kFoccStandardLabel, kFoccLatestLabel]

def main():
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""
    
    curDir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(curDir, "data", "blksize_abort_rate")
    x_axis, series_names, series = parse(data_path)

    f, (axis) = plt.subplots()
    f.set_size_inches(6, 6)
    xticks = range(len(x_axis))
    for label in series_labels:
        pruned_ticks = []
        pruned_series = []
        for i in range(len(series[label])):
            if series[label][i] >= 0:
                pruned_ticks.append(xticks[i])
                pruned_series.append(series[label][i])

        axis.plot(pruned_ticks, pruned_series,fmt(label), label=label,  **line_fmt(label))
        # axis.plot(xticks, series[label],fmt(label))

    axis.tick_params(axis='both', which='major', labelsize=18)

    axis.set_title("Throughput")

    axis.set_xlabel("# of txns per block")
    axis.set_xticks(xticks)
    # latency_ax.set_xticklabels(xlabels, fontsize=18)
    axis.set_xticklabels(x_axis)
    axis.set_yticks([0, .2, .4, .6, .8, 1.0])

    axis.set_ylim([-.1, 1.2])
    axis.set_ylabel("tps")

    handles, labels = axis.get_legend_handles_labels()
    f.legend(handles, labels,
             loc='upper center', ncol=2, bbox_to_anchor=(0.53, 0.88))

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())