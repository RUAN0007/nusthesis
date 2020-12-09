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
    

    curDir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(curDir, "data", "provenance", "ycsb_thruput")
    x_axis, series_names, series = config.parse(data_path)
    # print x_axis
    # print series_names
    # print series
    
    blk_sizes = x_axis
    xlabels = [str(int(x)/100) for x in blk_sizes]

    series_count = len(series_names)
    width, offsets = config.compute_width_offsets(series_count)

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
        ax.bar(xticks, series_data, width=width, color=config.colors[series_name], edgecolor='black',align='center', label=series_name)

    # ax.set_title("Throughput")
    ax.set(xlabel=r'# Txns per Block (x100)', ylabel='tps')
    ax.set_xticks(base_xticks)
    ax.set_xticklabels(xlabels)
    ax.set_ylim([0, 2500])

    handles, labels = ax.get_legend_handles_labels()
    f.legend(handles, labels,
             loc='upper center', ncol=1, bbox_to_anchor=(0.47, 0.90), 
             columnspacing=1, handletextpad=1, fontsize=20)

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())