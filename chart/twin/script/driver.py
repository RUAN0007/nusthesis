import sys
from common import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl


ycsb = [24, 30]
blockbench = [78, 56]
caliper = [442, 439]

def main():
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""
    
#     print path
    f, (thruput_ax) = plt.subplots(1, 1)
    f.set_size_inches(7, 4)
    thruput_ax.bar([-0.15, 0.85], ycsb, label="YCSB (Sync)", width=0.3, hatch="xxx", edgecolor="black")
    # thruput_ax.bar([0, 1], blockbench, label="Async-YCSB", width=0.3, hatch="///", edgecolor="black")
    thruput_ax.bar([0.15, 1.15], caliper, label="Caliper (Async)", width=0.3, edgecolor="black")

    thruput_ax.set_title("Throughput", fontsize=22)
    thruput_ax.set_ylabel('tps', fontsize=20)
    thruput_ax.set_xticks([0, 1])
    thruput_ax.set_xticklabels(["16x4", "16x8"], fontsize=20)
    thruput_ax.yaxis.set_tick_params(labelsize=20)
    thruput_ax.set_ylim([0, 700])

    thruput_handles, thruput_labels = thruput_ax.get_legend_handles_labels()
    f.legend(thruput_handles, thruput_labels, 
             loc='upper center', ncol=2, bbox_to_anchor=(0.55, 0.80), fontsize=17)

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())