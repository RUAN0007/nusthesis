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

    ostandard_scheduler_path = os.path.join(curDir, "data", "txn", "complex_readhot_txn_delay", ostandard_scheduler_label)
    x_axis, series_names, ostandard_scheduler_series = config.parse(ostandard_scheduler_path)

    fplus_scheduler_path = os.path.join(curDir, "data", "txn", "complex_readhot_txn_delay", fplus_scheduler_label)
    _, _, fplus_scheduler_series = config.parse(fplus_scheduler_path)

    fg_scheduler_path = os.path.join(curDir, "data", "txn", "complex_readhot_txn_delay", fg_scheduler_label)
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

    xticks = config.sum_list(base_xticks, [offset] * num_point)
    axis.bar(xticks, fplus_scheduler_data, width=width, color="white", edgecolor='black',
                hatch=fplus_scheduler_hatch, align="center")

########################################
# ostandard_scheduler-standard
    offset = offsets[1]
    ostandard_scheduler_data = ostandard_scheduler_series[ostandard_scheduler_label]
    ostandard_scheduler_hatch = "xxx"
    num_point = len(ostandard_scheduler_data)

    xticks = config.sum_list(base_xticks, [offset] * num_point)
    axis.bar(xticks, ostandard_scheduler_data, width=width, color="white", edgecolor='black',
                hatch=ostandard_scheduler_hatch, align="center")


########################################
# fg_scheduler
    offset = offsets[2]
    bottom = [0] * num_point

    dep_resolution_series = fg_scheduler_series["Dep Resolution"]
    dep_resolution_color = "r"
    xticks = config.sum_list(base_xticks, [offset] * num_point)
    axis.bar(xticks, dep_resolution_series, width=width, color=dep_resolution_color, edgecolor='black',
             bottom=bottom, align="center")
    bottom = config.sum_list(bottom, dep_resolution_series)

    accessibility_series = fg_scheduler_series["Test Accessibility"]
    accessibility_color = "g"
    xticks = config.sum_list(base_xticks, [offset] * num_point)
    axis.bar(xticks, accessibility_series, width=width, color=accessibility_color, edgecolor='black',
             bottom=bottom, align="center")
    bottom = config.sum_list(bottom, accessibility_series)
             
    index_record_series = fg_scheduler_series["Update Pending"]
    index_record_color = "skyblue"
    xticks = config.sum_list(base_xticks, [offset] * num_point)
    axis.bar(xticks, index_record_series, width=width, color=index_record_color, edgecolor='black',
             bottom=bottom, align="center")
    bottom = config.sum_list(bottom, index_record_series)

    # axis.tick_params(axis='both', which='major', labelsize=18)
    # axis.set_title("Txn Process Latency")

    axis.set_xlabel("Read hot ratio (%)")
    axis.set_xticks(base_xticks)
    # latency_ax.set_xticklabels(xlabels, fontsize=18)
    axis.set_xticklabels(x_axis)

    axis.set_yticks(range(0, 1001, 200))
    axis.set_ylim([1, 2200])
    axis.set_ylabel("us")
    # axis.set_yscale("log")
    axis.yaxis.set_label_coords(-0.02,0.97)

# Fake series for legends
    legend_labels = ["Identify conflict", "Update graph", "Index record", 
                     fplus_scheduler_label, ostandard_scheduler_label, fg_scheduler_label]
    ostandard_scheduler_standard_legend = axis.bar(0, 0, color="white", edgecolor="black", hatch=ostandard_scheduler_hatch)
    fplus_scheduler_legend = axis.bar(0, 0,color="white", edgecolor="black", hatch=fplus_scheduler_hatch)
    fg_scheduler_legend = axis.bar(0, 0, color="white", edgecolor="black")

    dep_legend = axis.bar(0, 0, color=dep_resolution_color, edgecolor="black")
    accessibility_legend = axis.bar(0, 0, color=accessibility_color, edgecolor="black")
    index_legend = axis.bar(0, 0, color=index_record_color, edgecolor="black")

    legends = [dep_legend, accessibility_legend, index_legend, fplus_scheduler_legend, ostandard_scheduler_standard_legend, fg_scheduler_legend]

    f.legend(legends, legend_labels, ncol=2, loc='upper center', bbox_to_anchor=(0.535, 0.86),handletextpad=0.3, fontsize=17)

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())