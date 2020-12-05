import sys
from common import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl

mbt = [34.0609, 124.0609, 1024.0609, 5024.0609]
mpt = [1090.4631, 1184.3002, 2071.7699, 6083.7872]
xlabels = ["10", "100", "1000", "5000"]

def main():
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""

    kMbtLabel = kFabricLabel  # Color MBT with the original Fabric style
    KMptLabel = kQuorumLabel 
#     print path
    f, (storage_ax) = plt.subplots()
    # f.set_size_inches(, 4)
    xticks = range(len(xlabels))
    width = 0.4
    mbt_xticks = [-0.2, 0.8, 1.8, 2.8]
    storage_ax.bar(mbt_xticks, mbt, width=width, color=base_colors[kMbtLabel], 
                 edgecolor='black', label="Merkle bucket tree")

    for i in range(len(mbt_xticks)):
        storage_ax.text(mbt_xticks[i], mbt[i], str(int(mbt[i])),ha='center', va="bottom", fontsize=14)

    mpt_xticks = [0.2, 1.2, 2.2, 3.2]
    storage_ax.bar(mpt_xticks, mpt, width=width, color=base_colors[KMptLabel],
                 edgecolor='black', label="Merkle patricia trie")

    for i in range(len(mpt_xticks)):
        storage_ax.text(mpt_xticks[i], mpt[i], str(int(mpt[i])), ha='center', va="bottom", fontsize=14)

    # storage_ax.set_title("State Storage")
    storage_ax.set_xlabel("Record size (byte)", fontsize=22)
    storage_ax.set_ylabel("byte", fontsize=22)
    storage_ax.set_xticks(xticks)
    storage_ax.set_xticklabels(xlabels, fontsize=18)
    storage_ax.set_ylim([1, 1000000])
    storage_ax.set_yscale("log")

    storage_handles, storage_labels = storage_ax.get_legend_handles_labels()
    f.legend(storage_handles, storage_labels, fontsize=20,
             loc='upper left',  ncol=1, bbox_to_anchor=(0.15, 0.95))

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())
