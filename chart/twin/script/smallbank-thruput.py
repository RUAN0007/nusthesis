import sys
from common import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl

thruput = {kFabricLabel: 405, kQuorumLabel: 675, kCockDBLabel: 5953, kTiDBLabel: 7393}
delay = {kFabricLabel: 794, kQuorumLabel: 691, kCockDBLabel: 410, kTiDBLabel: 320}

labels = [kFabricLabel, kQuorumLabel, kCockDBLabel, kTiDBLabel]

def main():
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""
     
    base=1.0
    
#     print path
    f, (thruput_ax) = plt.subplots()
    xticks = range(len(labels))
    colors = [base_colors[label] for label in labels]
    hatches = [base_hatches[label] for label in labels]
    width = 1

    data = [thruput[label] / base for label in labels]
    for xtick in range(len(xticks)):
        thruput_ax.bar(xtick, data[xtick], color=colors[xtick], edgecolor='black', hatch=hatches[xtick])
        thruput_ax.text(xtick, data[xtick], str(int(data[xtick])), ha="center", va="bottom")
    thruput_ax.set_title("Throughput", fontsize=36)
    thruput_ax.set(ylabel='tps')
    thruput_ax.set_xticks(xticks)
    thruput_ax.set_xticklabels(labels, fontsize=22)
    thruput_ax.set_yticks(range(0, 10001, 2000))
    thruput_ax.yaxis.set_tick_params(labelsize=20)
    thruput_ax.set_ylim([0, 10000])

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())