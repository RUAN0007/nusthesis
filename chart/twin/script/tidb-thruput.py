import sys
from common import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl

external_thruput = [2618,3254,3152,3715,3556,3918]
storage_thruput = [6928,7635,7987,11529,9351,11332]

# labels = [kFabricLabel, kQuorumLabel, kCockDBLabel, kTiDBLabel, kEtcdLabel]
xlabels = range(40, 81, 8)

def main():
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""
    
#     print path
    f, (thruput_ax) = plt.subplots()
    # f.set_size_inches(, 4)
    xticks = range(len(xlabels))

    # external_thruput_fmt = FAB_FMT # Borrow line style from fabric
    # external_line_opt = FAB_LINE_OPTS
    # external_line_opt['label'] = "SQL"
    # print len(xticks), external_thruput
    # thruput_ax.plot(xticks, external_thruput, external_thruput_fmt, **external_line_opt)

    # storage_thruput_fmt = QUO_FMT # Borrow line style from quorum
    # storage_line_opt = QUO_LINE_OPTS
    # storage_line_opt['label'] = "Storage"

    # thruput_ax.plot(xticks, storage_thruput, storage_thruput_fmt, **storage_line_opt)
    width=0.42
    tick1 = sum_list(xticks, [-width / 2] * len(xticks))
    thruput_ax.bar(tick1, external_thruput, label="TiDB-Transaction", width=width, hatch="xxx", edgecolor="black")
    for i, tick in enumerate(tick1):
        thruput_ax.text(tick, external_thruput[i], external_thruput[i], ha="center", fontsize=12)

    tick2 = sum_list(xticks, [width / 2] * len(xticks))
    thruput_ax.bar(tick2, storage_thruput, label="TiKV-Storage", width=width, hatch="///", edgecolor="black")
    for i, tick in enumerate(tick2):
        thruput_ax.text(tick, storage_thruput[i], storage_thruput[i], ha="center", fontsize=12)

    thruput_ax.set_title("Throughput")
    thruput_ax.set(xlabel="# of clients", ylabel='tps')
    thruput_ax.set_xticks(xticks)
    thruput_ax.set_xticklabels(xlabels, fontsize=14)
    thruput_ax.set_ylim([1000, 30000])
    thruput_ax.set_yscale("log")

    thruput_handles, thruput_labels = thruput_ax.get_legend_handles_labels()
    f.legend(thruput_handles, thruput_labels, 
             loc='upper center', ncol=3, bbox_to_anchor=(0.55, 0.89))

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())