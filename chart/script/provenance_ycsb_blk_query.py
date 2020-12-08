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
    
    series_names = [config.kFabricProvOLabel, config.kFabricSharpOLiteLabel, config.kFabricSharpOLabel]
    series = {}
    series[config.kFabricProvOLabel] = [x / 1000000.0 for x in [41559, 33669, 42458, 31646, 31574]]
    series[config.kFabricSharpOLiteLabel] = [x / 1000000.0 for x in [55509, 58855, 57440, 59480, 62494]]
    series[config.kFabricSharpOLabel] = [x / 1000000.0 for x in [24201, 24789, 24216, 22860, 25084]]

    xlabels = ["2^{}".format(i) for i in range(10, 15)]

    f, (ax) = plt.subplots()
    # # f.set_size_inches(, 4)
    for series_name in series_names:
        series_data = series[series_name]
        xticks = range(len(series_data))
        ax.plot(xticks, series_data, config.FMTS[series_name], **config.LINE_OPTS[series_name])

    # ax.set_title("Throughput")
    ax.set(xlabel='# of blocks', ylabel='ms')
    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels)
    ax.set_ylim([0.02, 0.100])

    handles, labels = ax.get_legend_handles_labels()
    f.legend(handles, labels,
             loc='upper center', ncol=1, bbox_to_anchor=(0.52, 0.87), 
             columnspacing=1, handletextpad=1, fontsize=20)

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())