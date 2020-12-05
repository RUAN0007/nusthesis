import sys
from common import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl

thruput = {kFabricLabel: [973, 971, 958, 920, 728, 525], 
           kQuorumLabel: [198,208,204,216,223,207], 
           kCockDBLabel: [6566,7611,11232,11580,2990,29],
           kTiDBLabel: [5461, 4407, 3317, 585, 483, 173],
           kEtcdLabel: [19884,19565,19757,19337,18650,18343]}

# labels = [kFabricLabel, kQuorumLabel, kCockDBLabel, kTiDBLabel, kEtcdLabel]
xlabels = [0, 0.2, 0.4, 0.6, 0.8, 1.0]

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

    thruput_ax.set_xlabel(r'Zipfian coefficient $\theta$', fontsize=28)
    thruput_ax.set_ylabel('tps', fontsize=28)

    thruput_ax.set_xticks(xticks)
    thruput_ax.set_xticklabels(xlabels, fontsize=28)
    thruput_ax.yaxis.set_tick_params(labelsize=28)
    thruput_ax.set_ylim([100, 200000])
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
