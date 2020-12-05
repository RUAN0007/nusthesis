import sys
from common import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl

delay = {kFabricLabel: 3472, kQuorumLabel: 536, kCockDBLabel: 50, 
           kTiDBLabel: 106, kEtcdLabel:25, kTikvLabel:86}

# labels = [kFabricLabel, kQuorumLabel, kCockDBLabel, kTiDBLabel, kEtcdLabel, kTikvLabel]
labels = [kFabricLabel, kQuorumLabel,  kTiDBLabel, kEtcdLabel, kTikvLabel]

def main():
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""
    
#     print path
    f, (delay_ax) = plt.subplots()
    # f.set_size_inches(9, 4)
    xticks = range(len(labels))
    colors = [base_colors[label] for label in labels]
    hatches = [base_hatches[label] for label in labels]
    width = 1

    data = [delay[label] for label in labels]
    for xtick in range(len(xticks)):
        delay_ax.bar(xtick, data[xtick], color=colors[xtick], edgecolor='black', hatch=hatches[xtick])
    # delay_ax.set_title("Update", fontsize=36)
    delay_ax.set(ylabel='ms')
    delay_ax.set_xticks(xticks)

    delay_ax.set_xticklabels(labels, fontsize=22,rotation=30)
    delay_ax.yaxis.set_tick_params(labelsize=20)

    delay_ax.set_ylim([0, 4000])

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())
