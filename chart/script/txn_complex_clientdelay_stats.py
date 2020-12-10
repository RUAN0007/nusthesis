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
    data_path = os.path.join(curDir, "data", "txn", "complex_clientdelay_stats")
    x_axis, series_names, series = config.parse(data_path)

    f, (axis) = plt.subplots()
    # f.set_size_inches(6, 6)
    xticks = range(len(x_axis))

    # Reuse Fsharp bar format
    axis.bar(xticks, series["# of hop"], width=0.8, label="# of hops",  color="orange")
        # axis.plot(xticks, series[label],fmt(label))

    axis.tick_params(axis='both', which='major', labelsize=18)

    # axis.set_title(kFsharpLabel + " Statistics")

    axis.set_xlabel("Client delay (ms)")
    axis.set_xticks(xticks)
    # latency_ax.set_xticklabels(xlabels, fontsize=18)
    axis.set_xticklabels(x_axis)
    axis.set_yticks(range(0, 71, 10))

    axis.set_ylim([000, 110])
    axis.set_ylabel("bar")
    # axis.yaxis.set_label_coords(-0.02, 0.95)
    # latency_ax.set_yscale("log")

    axis2 = axis.twinx()
    fg_scheduler_label = config.make_label(config.forkbase_label, config.fg_scheduler_label)

    config.line_opts[fg_scheduler_label]["label"] = "Txn blk span"
    axis2.plot(xticks, series["Txn blk span"], config.fmts[fg_scheduler_label], **config.line_opts[fg_scheduler_label])
    axis2.set_ylim([-7, 10])
    axis2.set_yticks(range(0,8,2))
    axis2.set_ylabel("line")

    handles1, labels1 = axis.get_legend_handles_labels()
    handles2, labels2 = axis2.get_legend_handles_labels()
    f.legend(handles1 + handles2, labels1 + labels2,
             loc='upper center', ncol=1, bbox_to_anchor=(0.50, 0.88), 
             columnspacing=1, handletextpad=1,labelspacing=1)

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())