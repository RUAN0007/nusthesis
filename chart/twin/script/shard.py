import sys
from common import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl


ycsb_cockdb = 10551
ycsb_tidb = 5787
ycsb_ahl = 325

sb_cockdb = 4285
sb_tidb = 11995
sb_ahl = 491

ycsb_hatch=base_hatches[kFabricLabel]
sb_hatch=base_hatches[kFabricLabel]

def main():
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""
    
#     print path
    f, (thruput_ax) = plt.subplots()
    # f.set_size_inches(9, 4)
    width = 0.25

    thruput_ax.bar(-0.25, ycsb_cockdb, width=width, color="red", edgecolor='black', hatch=ycsb_hatch, label="CockroachDB")
    thruput_ax.bar(0, ycsb_tidb, width=width,color="green", edgecolor='black', hatch=ycsb_hatch, label="TiDB")
    thruput_ax.bar(0.25, ycsb_ahl, width=width,color="yellow", edgecolor='black', hatch=ycsb_hatch, label="AHL")

    thruput_ax.text(-0.25, ycsb_cockdb, ycsb_cockdb, ha="center",va="bottom", fontsize=12) 
    thruput_ax.text(0, ycsb_tidb, ycsb_tidb, ha="center", va="bottom", fontsize=12)
    thruput_ax.text(0.25, ycsb_ahl, "<500", ha="center",va="bottom", fontsize=12)

    latency_handles, latency_labels = thruput_ax.get_legend_handles_labels()

    thruput_ax.bar(0.75, sb_cockdb, width=width, color="red", edgecolor='black', hatch=sb_hatch, label="CrDB")
    thruput_ax.bar(1, sb_tidb, width=width,color="green", edgecolor='black', hatch=sb_hatch,label="TiDB")
    thruput_ax.bar(1.25, sb_ahl, width=width,color="yellow", edgecolor='black', hatch=sb_hatch, label="AHL")

    thruput_ax.text(0.75, sb_cockdb, sb_cockdb, ha="center",va="bottom", fontsize=12)
    thruput_ax.text(1, sb_tidb, sb_tidb, ha="center",va="bottom", fontsize=12)
    thruput_ax.text(1.25, sb_ahl, "<500", ha="center",va="bottom", fontsize=12)

    thruput_ax.set_title("Throughput")
    thruput_ax.set(ylabel='tps')
    thruput_ax.set_xticks([0, 1])
    thruput_ax.set_xticklabels(["YCSB", "Smallbank"], fontsize=24)
    thruput_ax.set_ylim([1, 1000000000])
    thruput_ax.set_yscale("log")

    f.legend(latency_handles, latency_labels, fontsize=22,
             loc='upper left',  ncol=1, bbox_to_anchor=(0.175, 0.86))

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())