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
    
    series_names = [config.kFabricProvOLabel, config.kFabricSharpOLabel]
    series = {}
    series[config.kFabricProvOLabel] = [x / 1000000.0 for x in [1045175, # 1000
                               1568381, # 2000
                               2757734, # 3000
                               3248646, # 4000,
                               4042472, # 5000,
                               5143231, # 6000
                               6341226, # 7000
                               6294415, # 8000
                               7384893, # 9000
                               10380770] # 10000
                                ]
    series[config.kFabricSharpOLabel] = [x / 1000000.0 for x in [323971, # 1000
                               718925, # 2000
                               1061239, # 3000
                               1258163, # 4000,
                               1565504, # 5000,
                               1876250, # 6000
                               2164747, # 7000
                               3130134, # 8000
                               3855851, # 9000
                               4891380] # 10000
                               ]

    xlabels = [i for i in range(1, 11)]

    f, (ax) = plt.subplots()
    # # f.set_size_inches(, 4)
    for series_name in series_names:
        series_data = series[series_name]
        xticks = range(len(series_data))
        ax.plot(xticks, series_data, config.FMTS[series_name], **config.LINE_OPTS[series_name])

    # ax.set_title("Throughput")
    ax.set(xlabel='# of blocks (x1000)', ylabel='ms')
    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels)
    ax.set_ylim([0.0, 12.5])

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