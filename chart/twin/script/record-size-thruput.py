import sys
from common import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl

thruput = {kFabricLabel: [1726, 1687, 1349, 623], 
           kQuorumLabel: [1547,826,219,58], 
        #    kCockDBLabel: [22065,17727,9177,1465],
           kTiDBLabel: [4781, 4552, 3730, 1768],
           kEtcdLabel: [24788,22069,19518,5654]}

# labels = [kFabricLabel, kQuorumLabel, kCockDBLabel, kTiDBLabel, kEtcdLabel]
xlabels = [10, 100, 1000, 5000]

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
    # thruput_ax.plot(xticks, thruput[kCockDBLabel], CockDB_FMT, **CockDB_LINE_OPTS)
    thruput_ax.plot(xticks, thruput[kTiDBLabel], TiDB_FMT, **TiDB_LINE_OPTS)
    thruput_ax.plot(xticks, thruput[kEtcdLabel], ETCD_FMT, **ETCD_LINE_OPTS)

    # thruput_ax.set_title("Throughput")
    thruput_ax.set_xlabel("Record size (byte)", fontsize=24)
    thruput_ax.set_ylabel("tps", fontsize=22)
    thruput_ax.set_xticks(xticks)
    thruput_ax.set_xticklabels(xlabels, fontsize=18)
    thruput_ax.set_ylim([30, 1000000])
    thruput_ax.set_yscale("log")

    thruput_handles, thruput_labels = thruput_ax.get_legend_handles_labels()
    f.legend(thruput_handles, thruput_labels, fontsize=18,
             loc='upper center', ncol=2, bbox_to_anchor=(0.5, 0.95))

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())
