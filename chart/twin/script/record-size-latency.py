import sys
from common import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl

latency = {kFabricLabel: [807,809,877,925], 
           kQuorumLabel: [147, 180, 308, 1439], 
           kCockDBLabel: [15,19,56,43],
           kTiDBLabel: [100,114,113,124],
           kEtcdLabel: [12,13,30,43]}

# labels = [kFabricLabel, kQuorumLabel, kCockDBLabel, kTiDBLabel, kEtcdLabel]
xlabels = [10, 100, 1000, 5000]

def main():
    print "This chart is deprecated..."
    return 1 
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""
    
#     print path
    f, (latency_ax) = plt.subplots()
    # f.set_size_inches(, 4)
    xticks = range(len(xlabels))

    latency_ax.plot(xticks, latency[kFabricLabel], FAB_FMT, **FAB_LINE_OPTS)
    latency_ax.plot(xticks, latency[kQuorumLabel], QUO_FMT, **QUO_LINE_OPTS)
    latency_ax.plot(xticks, latency[kCockDBLabel], CockDB_FMT, **CockDB_LINE_OPTS)
    latency_ax.plot(xticks, latency[kTiDBLabel], TiDB_FMT, **TiDB_LINE_OPTS)
    latency_ax.plot(xticks, latency[kEtcdLabel], ETCD_FMT, **ETCD_LINE_OPTS)

    latency_ax.set_title("Latency")
    latency_ax.set(xlabel="Record size (byte)", ylabel='ms')
    latency_ax.set_xticks(xticks)
    latency_ax.set_xticklabels(xlabels, fontsize=18)
    latency_ax.set_ylim([0, 2500])
    # latency_ax.set_yscale("log")

    latency_handles, latency_labels = latency_ax.get_legend_handles_labels()
    f.legend(latency_handles, latency_labels, fontsize=15,
             loc='upper center', ncol=3, bbox_to_anchor=(0.55, 0.83))

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())