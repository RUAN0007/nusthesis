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
    
    fabricprov_label = config.make_label(config.ldb_prov_label)
    fabricsharp_label = config.make_label(config.forkbase_label)
    fabricsharplite_label = fabricsharp_label + "(No DASL)"

    series_names = [fabricprov_label, fabricsharplite_label, fabricsharp_label]
    series = {}
    series[fabricprov_label] = [x / 1000000.0 for x in [41559, 33669, 42458, 31646, 31574]]
    series[fabricsharplite_label] = [x / 1000000.0 for x in [55509, 58855, 57440, 59480, 62494]]
    series[fabricsharp_label] = [x / 1000000.0 for x in [24201, 24789, 24216, 22860, 25084]]

    # Fabric# without DASL reuses the format of Fabric#, except the color.
    config.fmts[fabricsharplite_label] = config.fmts[fabricsharp_label]
    config.line_opts[fabricsharplite_label] = config.line_opts[fabricsharp_label].copy()
    config.line_opts[fabricsharplite_label]["color"] = "orange"
    config.line_opts[fabricsharplite_label]["markerfacecolor"] = "orange"
    config.line_opts[fabricsharplite_label]["label"] = fabricsharplite_label

    xlabels = ["2^{}".format(i) for i in range(10, 15)]

    f, (ax) = plt.subplots()
    # # f.set_size_inches(, 4)
    for series_name in series_names:
        series_data = series[series_name]
        xticks = range(len(series_data))
        ax.plot(xticks, series_data, config.fmts[series_name], **config.line_opts[series_name])

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