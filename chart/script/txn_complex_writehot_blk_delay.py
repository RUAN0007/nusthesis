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

    olatest_scheduler_label = config.make_label(config.forkbase_label, config.occ_latest_scheduler_label)
    fplus_scheduler_label = config.make_label(config.forkbase_label, config.fabricplus_scheduler_label)
    fg_scheduler_label = config.make_label(config.forkbase_label, config.fg_scheduler_label)

    olatest_scheduler_path = os.path.join(curDir, "data", "txn", "complex_writehot_blk_delay", olatest_scheduler_label)
    x_axis, series_names, olatest_scheduler_series = config.parse(olatest_scheduler_path)

    fplus_scheduler_path = os.path.join(curDir, "data", "txn", "complex_writehot_blk_delay", fplus_scheduler_label)
    _, _, fplus_scheduler_series = config.parse(fplus_scheduler_path)

    fg_scheduler_path = os.path.join(curDir, "data", "txn", "complex_writehot_blk_delay", fg_scheduler_label)
    _, _, fg_scheduler_series = config.parse(fg_scheduler_path)

    f, (axis) = plt.subplots()
    # f.set_size_inches(6, 6)

    base_xticks = range(len(x_axis))

    num_bar_series = 3
    width, offsets = config.compute_width_offsets(3)


########################################
# fplus_scheduler
    offset = offsets[0]
    fplus_scheduler_data = fplus_scheduler_series[fplus_scheduler_label]
    fplus_scheduler_hatch = "///"
    num_point = len(fplus_scheduler_data)
    bottom = [0] * num_point

    xticks = config.sum_list(base_xticks, [offset] * num_point)
    axis.bar(xticks, fplus_scheduler_data, width=width, color="white", edgecolor='black',
                hatch=fplus_scheduler_hatch, align="center")

########################################
# olatest_scheduler-latest
    offset = offsets[1]
    olatest_scheduler_data = olatest_scheduler_series[olatest_scheduler_label]
    olatest_scheduler_hatch = "xxx"
    num_point = len(olatest_scheduler_data)
    bottom = [0] * num_point

    xticks = config.sum_list(base_xticks, [offset] * num_point)
    axis.bar(xticks, olatest_scheduler_data, width=width, color="white", edgecolor='black',
                hatch=olatest_scheduler_hatch, align="center")


########################################
# fp_scheduler
    offset = offsets[2]
    bottom = [0] * num_point

    schedule_series = fg_scheduler_series["Schedule"]
    schedule_color = "r"
    xticks = config.sum_list(base_xticks, [offset] * num_point)
    axis.bar(xticks, schedule_series, width=width, color=schedule_color, edgecolor='black',
             bottom=bottom, align="center")
    bottom = config.sum_list(bottom, schedule_series)

    restoration_series = fg_scheduler_series["WW Reinstallation"]
    restoration_color = "g"
    xticks = config.sum_list(base_xticks, [offset] * num_point)
    axis.bar(xticks, restoration_series, width=width, color=restoration_color, edgecolor='black',
             bottom=bottom, align="center")
    bottom = config.sum_list(bottom, restoration_series)
             
    storage_series = fg_scheduler_series["Storage"]
    storage_color = "skyblue"
    xticks = config.sum_list(base_xticks, [offset] * num_point)
    axis.bar(xticks, storage_series, width=width, color=storage_color, edgecolor='black',
             bottom=bottom, align="center")
    bottom = config.sum_list(bottom, storage_series)

    prune_series = fg_scheduler_series["Txn Pruning"]
    prune_color = "orange"
    xticks = config.sum_list(base_xticks, [offset] * num_point)
    axis.bar(xticks, prune_series, width=width, color=prune_color, edgecolor='black',
             bottom=bottom, align="center")
    bottom = config.sum_list(bottom, prune_series)

    axis.tick_params(axis='both', which='major', labelsize=18)

    # axis.set_title("Reorder Latency")

    axis.set_xlabel("Write hot ratio (%)")
    axis.set_xticks(base_xticks)
    # latency_ax.set_xticklabels(xlabels, fontsize=18)
    axis.set_xticklabels(x_axis)

    axis.set_yticks(range(0, 101, 10))
    axis.set_ylim([0, 150])
    axis.set_ylabel("ms")
    # latency_ax.set_yscale("log")
    axis.yaxis.set_label_coords(-0.02,0.97)

# Fake series for legends
    legend_labels = ["Compute order", r'Restore $ww$', "Persist to storage", r'Prune $G$', 
                    fplus_scheduler_label, olatest_scheduler_label, fg_scheduler_label]
    olatest_scheduler_latest_legend = axis.bar(0, 0, color="white", edgecolor="black", hatch=olatest_scheduler_hatch)
    fplus_scheduler_legend = axis.bar(0, 0,color="white", edgecolor="black", hatch=fplus_scheduler_hatch)
    fg_scheduler_legend = axis.bar(0, 0, color="white", edgecolor="black")

    schedule_legend = axis.bar(0, 0, color=schedule_color, edgecolor="black")
    restore_legend = axis.bar(0, 0, color=restoration_color, edgecolor="black")
    storage_legend = axis.bar(0, 0, color=storage_color, edgecolor="black")
    prune_legend = axis.bar(0, 0, color=prune_color, edgecolor="black")

    legends = [schedule_legend, restore_legend, storage_legend, prune_legend, fplus_scheduler_legend, olatest_scheduler_latest_legend, fg_scheduler_legend]

    f.legend(legends, legend_labels, ncol=2, loc='upper center', bbox_to_anchor=(0.51, 0.86),handletextpad=1, fontsize=17)

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())