import sys
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl
import config

def main():
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""

    xlabels = ["Silicon", "Quartz"]
    series_names = [config.kFabricProvOLabel, config.kFabricSharpOLabel]
    series = {config.kFabricSharpOLabel: [849, 338], config.kFabricProvOLabel: [973, 363]}

    width, offsets = config.compute_width_offsets(len(series[config.kFabricSharpOLabel]))

    f, (ax) = plt.subplots()
    # # f.set_size_inches(, 4)
    for i, series_name in enumerate(series_names):
        series_data = series[series_name]
        series_offsets = [offsets[i]] * len(series_data)
        base_xticks = range(len(series_data))
        xticks = config.sum_list(base_xticks, series_offsets) 
        # print xticks
        # print series_name
        # print series_data
        ax.bar(xticks, series_data, width=width, color=config.base_colors[series_name], edgecolor='black',align='center', label=series_name)

    # ax.set_title("Throughput")
    ax.set(ylabel='us')
    ax.set_xticks(base_xticks)
    ax.set_xticklabels(xlabels, fontsize=24)
    ax.set_ylim([300, 1200])

    handles, labels = ax.get_legend_handles_labels()
    f.legend(handles, labels,
             loc='upper center', ncol=1, bbox_to_anchor=(0.67, 0.90), 
             columnspacing=1, handletextpad=1, fontsize=20)

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())