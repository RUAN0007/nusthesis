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
    data_path = os.path.join(curDir, "data", "provenance","smallbank_util")
    x_axis, series_names, series = config.parse(data_path)

    xlabels = x_axis

    series_count = len(series_names) - 1 # BlkScan	Invocation are stacked into one bar series
    width, offsets = config.compute_width_offsets(series_count)

    f, (ax) = plt.subplots()
    # # f.set_size_inches(, 4)

    original_label = config.make_label(config.original_label)
    fabricprov_label = config.make_label(config.ldb_prov_label)
    fabricsharp_label = config.make_label(config.forkbase_label)

    invocation_delay = series["Invocation"]
    base_xticks = range(len(invocation_delay))

    series_offsets = [offsets[0]] * len(invocation_delay)
    xticks = config.sum_list(base_xticks, series_offsets) 
    ax.bar(xticks, invocation_delay, width=width, color=config.colors[original_label], edgecolor='black',align='center', label="Invocation(Fabric)")

    blkscan_delay = series["BlkScan"]
    ax.bar(xticks, blkscan_delay, width=width, color="white", edgecolor=config.colors[original_label],align='center', label="Block Scan(Fabric)", bottom=invocation_delay, hatch="xxx")

    fabricplus_delay = series[fabricprov_label]
    series_offsets = [offsets[1]] * len(fabricplus_delay)
    xticks = config.sum_list(base_xticks, series_offsets) 
    ax.bar(xticks, fabricplus_delay, width=width, color=config.colors[fabricprov_label], edgecolor='black',align='center', label=fabricprov_label)

    fabricsharp_delay = series[fabricsharp_label]
    series_offsets = [offsets[2]] * len(fabricsharp_delay)
    xticks = config.sum_list(base_xticks, series_offsets) 
    ax.bar(xticks, fabricplus_delay, width=width, color=config.colors[fabricsharp_label], edgecolor='black',align='center', label=fabricsharp_label)

    handles, labels = ax.get_legend_handles_labels()
    f.legend(handles, labels,
             loc='upper center', ncol=1, bbox_to_anchor=(0.42, 0.91), fontsize=20) 
            #  columnspacing=1, handletextpad=1, fontsize=20)
    

    # ax.set_title("Throughput and Abort Rate")
    ax.set(xlabel=r'# of scanned blocks', ylabel='sec')
    ax.set_xticks(base_xticks)
    ax.set_xticklabels(xlabels)
    ax.set_ylim([0, 40])
    # ax.set_yticks([0, 250, 500, 750, 1000, 1250, 1500])

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())