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
    data_path = os.path.join(curDir, "data", "intro", "smallbank_blk")
    x_axis, series_names, series = config.parse(data_path)
    blk_sizes = x_axis
    req_rate_label, effective_thruput_label, raw_thruput_label, abort_label = series_names[0], series_names[1],series_names[2],series_names[3],

    f, (axis) = plt.subplots()
    # f.set_size_inches(7.5, 4)

    xticks = range(len(x_axis))
    effective_series = series[effective_thruput_label]
    color = config.raw_colors[config.original_label]
    axis.bar(xticks, effective_series, width=0.7, color=color, edgecolor='black',
              label="Effective")

    abort_series = [series[raw_thruput_label][i] - effective_series[i] for i in range(len(series[raw_thruput_label]))]
    axis.bar(xticks, abort_series, width=0.7, color="white", edgecolor=color,
              label="Aborted", bottom=effective_series, hatch="xx")

    axis.tick_params(axis='both', which='major', labelsize=18)

    # axis.set_title("Throughput and Abort Rate")

    axis.set_xlabel(r'Blk size (Request rate)')
    axis.set_xticks(xticks)
    request_rate_series = series[req_rate_label]
    xlabels = ["{}\n({})".format(int(blk_sizes[i]), int(request_rate_series[i])) for i in range(len(x_axis))]
    axis.set_xticklabels(xlabels, fontsize=15)

    axis.set_yticks(range(000, 1701, 400))

    axis.set_ylim([000, 2420])
    axis.set_ylabel("tps")
    # latency_ax.set_yscale("log")
    axis.yaxis.set_label_coords(-0.01,0.9)

    abort_ax = axis.twinx()

    format_label=config.make_label(config.original_label) # Use the original Fabric format style
    line_opt = config.line_opts[format_label]
    line_opt["label"] = "Abort Rate"

    abort_ax.plot(xticks, series[abort_label], config.fmts[format_label], **line_opt)
    abort_ax.set_ylim([-0.5, 1.2])
    abort_ax.set_yticks([0, .5, 1.0])
    abort_ax.set_yticklabels(["0", "50", "100"])
    abort_ax.set(ylabel='percent(%)')


    handles, labels = axis.get_legend_handles_labels()
    abort_handles, abort_labels = abort_ax.get_legend_handles_labels()
    f.legend(handles + abort_handles, labels + abort_labels,
             loc='upper center', ncol=2, bbox_to_anchor=(0.47, 0.92), fontsize=18)
            #  columnspacing=1, handletextpad=1, fontsize=24)

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())