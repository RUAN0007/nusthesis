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
    effective_thruput_path = os.path.join(curDir, "data", "blksize_effective_thruput")
    raw_thruput_path = os.path.join(curDir, "data", "blksize_raw_thruput")
    x_axis, series_names, effective_series = parse(effective_thruput_path)
    _, _, raw_series = parse(raw_thruput_path)


    f, (axis) = plt.subplots()
    f.set_size_inches(9, 6)
    base_xticks = range(len(x_axis))
    width = 0.15 # a total of 5 series
    offsets = [-0.36, -0.18, 0, 0.18, 0.36]
    for i, label in enumerate(series_labels):
        num_point = len(x_axis)
        xticks = sum_list(base_xticks, [offsets[i]] * num_point)
        axis.bar(xticks, effective_series[label],width=width, label=label,  **bar_format(label))
        aborted = [raw_series[label][i] - effective_series[label][i] for i in range(len(effective_series[label]))]
        axis.bar(xticks, aborted,width=width, bottom=effective_series[label], color="white", edgecolor=base_colors[label],linewidth="1")
        # axis.plot(xticks, series[label],fmt(label))
    axis.text(3 - .23, 20, str(0), color=base_colors[kFppLabel], fontweight='bold')
    axis.text(4 - .23, 20, str(0), color=base_colors[kFppLabel], fontweight='bold')
    axis.text(5 - .23, 20, str(0), color=base_colors[kFppLabel], fontweight='bold')

    axis.tick_params(axis='both', which='major', labelsize=18)

    axis.yaxis.set_label_coords(-0.02, 0.95)
    axis.set_title("Throughput")

    axis.set_xlabel("# of txns per block")
    axis.set_xticks(base_xticks)
    # latency_ax.set_xticklabels(xlabels, fontsize=18)
    axis.set_xticklabels(x_axis)
    axis.set_yticks(range(0, 1500, 300))

    axis.set_ylim([0, 1700])
    axis.set_ylabel("tps")
    # latency_ax.set_yscale("log")

    handles, labels = axis.get_legend_handles_labels()
    newIdx = [0, 1, 4, 2, 3]

    f.legend([handles[i] for i in newIdx], [labels[i] for i in newIdx],
             loc='upper center', ncol=2, bbox_to_anchor=(0.54, 0.88)
             ,handletextpad=0.2)

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())