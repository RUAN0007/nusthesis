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
    
    series_names = [config.kFabricPlusLabel, config.kFabricSharpLiteLabel, config.kFabricSharpLabel]
    series = {}
    series[config.kFabricPlusLabel] = [x / 1000000.0 for x in [29166, 42222, 25575, 23483, 35100, 33435, 31574, 41922]]
    series[config.kFabricSharpLiteLabel] = [x / 1000000.0 for x in [8751, 7486, 9015, 11836, 17098, 36527, 61952, 114019]]
    series[config.kFabricSharpLabel] = [x / 1000000.0 for x in [13340, 12170, 14337, 16347, 18840, 22401, 25084, 27829]]

    xlabels = ["2^{}".format(i) for i in range(0, 9)]

    f, (ax) = plt.subplots()
    # # f.set_size_inches(, 4)
    for series_name in series_names:
        series_data = series[series_name]
        xticks = range(len(series_data))
        ax.plot(xticks, series_data, config.FMTS[series_name], **config.LINE_OPTS[series_name])

    # ax.set_title("Throughput")
    ax.set(xlabel='Block distance', ylabel='ms')
    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels)
    ax.set_ylim([0.0, 0.15])

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