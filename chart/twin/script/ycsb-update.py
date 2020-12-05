import sys
from common import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl

# labels = [kFabricLabel, kQuorumLabel, kCockDBLabel, kTiDBLabel, kEtcdLabel, kTikvLabel]
labels = [kFabricLabel, kQuorumLabel,  kTiDBLabel, kEtcdLabel, kTikvLabel]

thruput = {kFabricLabel: 1294, kQuorumLabel: 245, kCockDBLabel: 10101, 
           kTiDBLabel: 5159, kEtcdLabel:16781, kTikvLabel:14117}

# query_thruput = {kFabricLabel: 8637, kQuorumLabel: 19166, kCockDBLabel: 34306, 
#            kTiDBLabel: 71920, kEtcdLabel:282192, kTikvLabel:94050

# mixed_thruput = {kFabricLabel: 808, kQuorumLabel: 485, kCockDBLabel: 5020, kTiDBLabel: 7148, kEtcdLabel:39547, kTikvLabel:23360}

# skewed_thruput = {kFabricLabel: 804, kQuorumLabel: 497, kCockDBLabel: 298, kTiDBLabel: 411, kEtcdLabel:39267,
# kTikvLabel: 21542}

def main():
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""
    
    f, (update_ax) = plt.subplots()
    # f.set_size_inches(12, 4)
    xticks = range(len(labels))
    colors = [base_colors[label] for label in labels]
    hatches = [base_hatches[label] for label in labels]
    width = 1

    data = [thruput[label]  for label in labels]
    for xtick in range(len(xticks)):
        update_ax.bar(xtick, data[xtick], color=colors[xtick], hatch=hatches[xtick], edgecolor='black')
        update_ax.text(xtick, data[xtick], str(data[xtick]),  ha="center", va="bottom")
    # update_ax.set_title("Update", fontsize=36)
    update_ax.set(ylabel='tps')
    update_ax.set_xticks(xticks)
    update_ax.set_xticklabels(labels, fontsize=22,rotation=30)
    update_ax.yaxis.set_tick_params(labelsize=20)
    update_ax.set_ylim([100, 100000])
    update_ax.set_yscale("log")

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())
