import sys
from common import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl

kRaftLabel = kFabricLabel # Raft series use original Fabric style
kIbftLabel = kQuorumLabel #IBFT series use original Quorum Style
thruput = {kRaftLabel: [211,215.3333333,211,215.6666667,212.3333333,212.3333333], 
           kIbftLabel: [232.6666667,222.3333333,223.3333333,203,204,190.6666667]}

stdDev = {
    kRaftLabel:[3.605551275,3.511884584,2,8.621678104,12.66227994,2.081665999],
    kIbftLabel:[1.154700538,10.5039675, 5.507570547, 17.34935157, 16.82260384, 29.26317367]
}

# labels = [kFabricLabel, kQuorumLabel, kCockDBLabel, kTiDBLabel, kEtcdLabel]
xlabels = [1,2,3,4,5,6]

def main():
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""
    
#     print path
    f, (throughput_ax) = plt.subplots()
    # f.set_size_inches(6, 4)
    xticks = range(len(xlabels))

    raft_xticks = sum_list(xticks, [-0.2] * len(xlabels))
    throughput_ax.bar(raft_xticks, thruput[kRaftLabel], yerr=stdDev[kRaftLabel], width=0.4, color=base_colors[kRaftLabel], 
                 edgecolor='black', label="Raft",error_kw=dict(lw=2, capsize=5, capthick=1))

    ibft_xticks = sum_list(xticks, [0.2] * len(xlabels))
    throughput_ax.bar(ibft_xticks, thruput[kIbftLabel], yerr=stdDev[kIbftLabel], width=0.4, color=base_colors[kIbftLabel], 
                 edgecolor='black', label="Ibft",error_kw=dict(lw=2, capsize=3, capthick=1))

    # throughput_ax.set_title("Quorum Throughput", fontsize=28)
    throughput_ax.set(xlabel="# tolerated failures (f)", ylabel='tps')
    throughput_ax.set_xticks(xticks)
    throughput_ax.set_xticklabels(xlabels, fontsize=24)
    throughput_ax.yaxis.set_tick_params(labelsize=24)
    throughput_ax.set_ylim([0, 420])
    # latency_ax.set_yscale("log")

    handles, labels = throughput_ax.get_legend_handles_labels()
    f.legend(handles, ["Raft", "IBFT"], fontsize=20,
             loc='upper center', ncol=3, bbox_to_anchor=(0.65, 0.95))

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())
