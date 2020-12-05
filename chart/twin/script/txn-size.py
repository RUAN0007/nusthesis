import sys
from common import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl

thruput = {kFabricLabel: [978, 891, 438, 214, 133, 90], 
           kQuorumLabel: [211,210,212,204,197,198], 
           kCockDBLabel: [4820,3099,1738,1366,1135,674],
           kTiDBLabel: [6491, 5559, 4578, 2406, 2507, 1249],
           kEtcdLabel: [24269,13910,10353,8688,7260,6645]}

# labels = [kFabricLabel, kQuorumLabel, kCockDBLabel, kTiDBLabel, kEtcdLabel]
xlabels = [1, 2 ,4 ,6, 8, 10]

def main():
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""
    
#     print path
    f, (thruput_ax) = plt.subplots()
    f.set_size_inches(8, 7)
    xticks = range(len(xlabels))

    thruput_ax.plot(xticks, thruput[kFabricLabel], FAB_FMT, **FAB_LINE_OPTS)
    thruput_ax.plot(xticks, thruput[kQuorumLabel], QUO_FMT, **QUO_LINE_OPTS)
    # thruput_ax.plot(xticks, thruput[kCockDBLabel], CockDB_FMT, **CockDB_LINE_OPTS)
    thruput_ax.plot(xticks, thruput[kTiDBLabel], TiDB_FMT, **TiDB_LINE_OPTS)
    thruput_ax.plot(xticks, thruput[kEtcdLabel], ETCD_FMT, **ETCD_LINE_OPTS)

    # thruput_ax.set_title("Throughput", fontsize=46)
    thruput_ax.set_xlabel("# op per txn", fontsize=28)
    thruput_ax.set_ylabel('tps', fontsize=28)
    thruput_ax.set_xticks(xticks)
    thruput_ax.set_xticklabels(xlabels, fontsize=28)
    thruput_ax.set_ylim([50, 500000])
    thruput_ax.yaxis.set_tick_params(labelsize=28)
    thruput_ax.set_yscale("log")

    thruput_handles, thruput_labels = thruput_ax.get_legend_handles_labels()
    f.legend(thruput_handles, thruput_labels, fontsize=26,
             loc='upper center', ncol=2, bbox_to_anchor=(0.53, 0.97))

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())
