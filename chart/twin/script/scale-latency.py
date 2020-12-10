import sys
from common import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl

thruput = {kFabricLabel: [871,897,946,1092,1153], 
           kQuorumLabel: [524,513,489,493,475], 
           kCockDBLabel: [35,37,39,38,37],
           kTiDBLabel: [142,150,150,146,149],
           kEtcdLabel: [31,30,33,33,30]}

# labels = [kFabricLabel, kQuorumLabel, kCockDBLabel, kTiDBLabel, kEtcdLabel]
xlabels = [3, 7, 11, 15, 19]

def main():
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""
    
#     print path
    f, (thruput_ax) = plt.subplots()
    # f.set_size_inches(, 4)
    xticks = range(len(xlabels))

    thruput_ax.plot(xticks, thruput[kFabricLabel], FAB_FMT, **FAB_LINE_OPTS)
    thruput_ax.plot(xticks, thruput[kQuorumLabel], QUO_FMT, **QUO_LINE_OPTS)
    thruput_ax.plot(xticks, thruput[kCockDBLabel], CockDB_FMT, **CockDB_LINE_OPTS)
    thruput_ax.plot(xticks, thruput[kTiDBLabel], TiDB_FMT, **TiDB_LINE_OPTS)
    thruput_ax.plot(xticks, thruput[kEtcdLabel], ETCD_FMT, **ETCD_LINE_OPTS)

    thruput_ax.set_title("Latency")
    thruput_ax.set(xlabel="# of nodes", ylabel='ms')
    thruput_ax.set_xticks(xticks)
    thruput_ax.set_xticklabels([3, 7, 9, 15, 19], fontsize=18)
    thruput_ax.set_ylim([0, 1800])
    # thruput_ax.set_yscale("log")

    thruput_handles, thruput_labels = thruput_ax.get_legend_handles_labels()
    f.legend(thruput_handles, thruput_labels, fontsize=16,
             loc='upper center', ncol=3, bbox_to_anchor=(0.55, 0.83))

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())