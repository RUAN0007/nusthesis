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
    # We reuse the Fabric results in provenance experiment, but strip away for others
    data_path = os.path.join(curDir, "data", "provenance","smallbank_thruput")
    x_axis, series_names, series = config.parse(data_path)
    series_names = [config.kFabricLabel]
    series = {config.kFabricLabel: series[config.kFabricLabel]}

    xlabels = x_axis

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
        ax.bar(xticks, series_data, width=width, color=config.base_colors[series_name], edgecolor='black',align='center', label=series_name)

    # handles, labels = ax.get_legend_handles_labels()
    # f.legend(handles, labels,
    #          loc='upper center', ncol=1, bbox_to_anchor=(0.37, 0.94), fontsize=20) 
            #  columnspacing=1, handletextpad=1, fontsize=20)
    

    # ax.set_title("Throughput and Abort Rate")
    ax.set(xlabel=r'Zipfian coefficient $\theta$', ylabel='tps')
    ax.set_xticks(base_xticks)
    ax.set_xticklabels(xlabels)
    ax.set_ylim([0, 2000])
    ax.set_yticks([0, 250, 500, 750, 1000, 1250, 1500])

    curDir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(curDir, "data", "provenance", "smallbank_abort")
    x_axis, series_names, series = config.parse(data_path)
    series_names = [config.kFabricLabel]
    series = {config.kFabricLabel: series[config.kFabricLabel]}

    abort_ax = ax.twinx()
    for i, series_name in enumerate(series_names):
        series_data = series[series_name]
        base_xticks = range(len(series_data))
        # print xticks
        # print series_name
        # print series_data
        # print series_name, config.FMTS[series_name]
        abort_ax.plot(base_xticks, series_data,  config.FMTS[series_name], **config.LINE_OPTS[series_name])
    abort_ax.set_ylim([-0.75, 1.0])
    abort_ax.set_yticks([0, .5, 1.0])
    abort_ax.set_yticklabels(["0", "50", "100"])
    abort_ax.set(ylabel='abort rate(%)')

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())