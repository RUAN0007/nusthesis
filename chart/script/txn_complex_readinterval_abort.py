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

    ostandard_scheduler_label = config.make_label(config.forkbase_label, config.occ_standard_scheduler_label)
    fplus_scheduler_label = config.make_label(config.forkbase_label, config.fabricplus_scheduler_label)
    fg_scheduler_label = config.make_label(config.forkbase_label, config.fg_scheduler_label)

    ostandard_scheduler_path = os.path.join(curDir, "data", "txn", "complex_readinterval_abort", ostandard_scheduler_label)
    x_axis, series_names, ostandard_scheduler_series = config.parse(ostandard_scheduler_path)

    fplus_scheduler_path = os.path.join(curDir, "data", "txn", "complex_readinterval_abort", fplus_scheduler_label)
    _, _, fplus_scheduler_series = config.parse(fplus_scheduler_path)

    fg_scheduler_path = os.path.join(curDir, "data", "txn", "complex_readinterval_abort", fg_scheduler_label)
    _, _, fg_scheduler_series = config.parse(fg_scheduler_path)

    f, (axis) = plt.subplots()
    # f.set_size_inches(6, 6)

    base_xticks = range(len(x_axis))

    num_bar_series = 3
    width, offsets = config.compute_width_offsets(3)

########################################
# fplus_scheduler
    offset = offsets[0]
    fplus_scheduler_hatch = "///"
    simulation_data = fplus_scheduler_series["simulation abort"]
    num_point = len(simulation_data)
    bottom = [0] * num_point

    simulation_abort_color = "skyblue"
    xticks = config.sum_list(base_xticks, [offset] * num_point)
    axis.bar(xticks, simulation_data, width=width, color=simulation_abort_color, edgecolor='black',
                hatch=fplus_scheduler_hatch, align="center", bottom=bottom)
    bottom = config.sum_list(bottom, simulation_data)

    other_abort_color = "green"
    xticks = config.sum_list(base_xticks, [offset] * num_point)
    other_data = fplus_scheduler_series["others"]
    axis.bar(xticks, other_data, width=width, color=other_abort_color, edgecolor='black',
                hatch=fplus_scheduler_hatch, align="center", bottom=bottom)

########################################
# ostandard_scheduler-standard
    offset = offsets[1]
    ostandard_scheduler_hatch = "xxx"

    ww_abort_data = ostandard_scheduler_series["ww-abort"]
    num_point = len(ww_abort_data)
    bottom = [0] * num_point

    xticks = config.sum_list(base_xticks, [offset] * num_point)
    ww_abort_color = "red"
    axis.bar(xticks, ww_abort_data, width=width, color=ww_abort_color, edgecolor='black',
                hatch=ostandard_scheduler_hatch, align="center", bottom=bottom)
    bottom = config.sum_list(bottom, ww_abort_data)

    rw_abort_data = ostandard_scheduler_series["2rw-abort"]
    rw_abort_color = "orange"
    axis.bar(xticks, rw_abort_data, width=width, color=rw_abort_color, edgecolor='black',
                hatch=ostandard_scheduler_hatch, align="center", bottom=bottom)


# ########################################
# fg_scheduler
    offset = offsets[2]
    bottom = [0] * num_point

    fg_scheduler_data = fg_scheduler_series[fg_scheduler_label]
    fg_scheduler_color = "white"
    xticks = config.sum_list(base_xticks, [offset] * num_point)
    axis.bar(xticks, fg_scheduler_data, width=width, color=fg_scheduler_color, edgecolor='black',
             bottom=bottom, align="center")
    bottom = config.sum_list(bottom, fg_scheduler_data)

########################################
    # axis.set_title("Abort Rate")
    axis.set_xlabel("Read interval (ms)")
    axis.set_xticks(base_xticks)
    # latency_ax.set_xticklabels(xlabels, fontsize=18)
    axis.set_xticklabels(x_axis)

    axis.set_yticks([0, .25, .50, .75, 1.00])
    axis.set_yticklabels([0, 25, 50, 75, 100])
    axis.set_ylim([0, 1.4])
    axis.set_ylabel("%")
    # axis.set_yscale("log")
    axis.yaxis.set_label_coords(-0.02,0.97)

# Fake series for legends
    legend_labels = ["Concurrent-ww", "2 consecutive rw", "Simulation abort", 
                      "Others", fplus_scheduler_label, ostandard_scheduler_label, fg_scheduler_label]
    ostandard_scheduler_legend = axis.bar(0, 0, color="white", edgecolor="black", hatch=ostandard_scheduler_hatch)
    fplus_scheduler_legend = axis.bar(0, 0,color="white", edgecolor="black", hatch=fplus_scheduler_hatch)
    fg_scheduler_legend = axis.bar(0, 0, color="white", edgecolor="black")

    ww_abort_legend = axis.bar(0, 0, color=ww_abort_color, edgecolor="black")
    rw_abort_legend = axis.bar(0, 0, color=rw_abort_color, edgecolor="black")
    early_simulaton_abort_legend = axis.bar(0, 0, color=simulation_abort_color, edgecolor="black")
    others_abort_legend = axis.bar(0, 0, color=other_abort_color, edgecolor="black")

    legends = [ww_abort_legend, rw_abort_legend, early_simulaton_abort_legend, others_abort_legend, fplus_scheduler_legend, ostandard_scheduler_legend,  fg_scheduler_legend]

    f.legend(legends, legend_labels, ncol=2, loc='upper center', bbox_to_anchor=(0.52, 0.90),handletextpad=0.3, fontsize=18)

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())