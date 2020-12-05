import sys
from common import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl

fabric_state = [64, 154, 1055, 5055]
fabric_blk = [6677, 6866, 8668, 16670]
tidb_state = [59.8,150,1050,5050]
xlabels = [10, 100, 1000, 5000]

def main():
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""
    
#     print path
    f, (storage_ax) = plt.subplots()
    # f.set_size_inches(, 4)
    xticks = range(len(xlabels))
    width = 0.4
    fabric_xticks = sum_list(xticks, [-0.2] * len(xlabels))
    storage_ax.bar(fabric_xticks, fabric_state, width=width, color=base_colors[kFabricLabel], 
                 edgecolor='black', hatch=base_hatches[kFabricLabel], label=kFabricLabel+"-state")

    storage_ax.bar(fabric_xticks, fabric_blk, width=width, color='lightblue', 
    edgecolor='black', hatch=base_hatches[kEtcdLabel], label=kFabricLabel+"-block",
    bottom=fabric_state)

    for i in range(len(fabric_xticks)):
        total = fabric_state[i] + fabric_blk[i]
        storage_ax.text(fabric_xticks[i], total, str(total),ha='center', va="bottom", fontsize=14)

    tidb_xticks = sum_list(xticks, [0.2] * len(xlabels))
    storage_ax.bar(tidb_xticks, tidb_state, width=width, color=base_colors[kTiDBLabel], 
                 edgecolor='black', hatch=base_hatches[kTiDBLabel], label=kTiDBLabel)
    for i in range(len(tidb_xticks)):
        storage_ax.text(tidb_xticks[i], tidb_state[i], str(tidb_state[i]),ha='center', va="bottom", fontsize=14)

    # storage_ax.set_title("Storage")
    storage_ax.set_xlabel("Record size (byte)", fontsize=22)
    storage_ax.set_ylabel("byte", fontsize=22)
    storage_ax.set_xticks(xticks)
    storage_ax.set_xticklabels(xlabels, fontsize=18)
    storage_ax.set_ylim([0, 25000])
    # storage_ax.set_yscale("log")

    storage_handles, storage_labels = storage_ax.get_legend_handles_labels()
    f.legend(storage_handles, storage_labels, fontsize=20,
             loc='upper left',  ncol=1, bbox_to_anchor=(0.20, 0.95))

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())
