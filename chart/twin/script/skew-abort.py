import sys
from common import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl

# abort = {
#            kFabricLabel: [0.14,0.1612,0.1807,0.18475,0.2935,0.4565], 
#            kTiDBLabel: [0,0.02,0.021,0.0217,0.025,0.16],
#            }

abort = {
           kFabricLabel: [ 0.023138833, 0.03134479272, 0.07070707071, 0.1593533487, 0.4438559322], 
           kTiDBLabel: [0.144, 0.132, 0.14, 0.16, 0.277],
           }

abort[kFabricLabel] = [value * 100.0 for value in abort[kFabricLabel]]
abort[kTiDBLabel] = [value * 100.0 for value in abort[kTiDBLabel]]

# labels = [kFabricLabel, kQuorumLabel, kCockDBLabel, kTiDBLabel, kEtcdLabel]
xlabels = [0.2, 0.4, 0.6, 0.8, 1.0]

def main():
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""
    
#     print path
    f, (abort_ax) = plt.subplots()
    f.set_size_inches(8, 7)
    xticks = range(len(xlabels))
    width = 0.4
    fabric_xticks = sum_list(xticks, [-0.2] * len(xlabels))
    abort_ax.bar(fabric_xticks, abort[kFabricLabel], width=0.4, color=base_colors[kFabricLabel], 
                #  edgecolor='black', hatch=base_hatches[kFabricLabel], label=kFabricLabel)
                 edgecolor='black', label=kFabricLabel)

    tidb_xticks = sum_list(xticks, [0.2] * len(xlabels))
    abort_ax.bar(tidb_xticks, abort[kTiDBLabel], width=0.4, color=base_colors[kTiDBLabel], 
                #  edgecolor='black', hatch=base_hatches[kTiDBLabel], label=kTiDBLabel)
                 edgecolor='black', label=kTiDBLabel)

    # abort_ax.set_title("Abort Rate", fontsize=46)

    abort_ax.set_xlabel(r'Zipfian coefficient $\theta$', fontsize=28)
    abort_ax.set_ylabel('percent (%)', fontsize=28)

    abort_ax.set_xticks(xticks)
    abort_ax.set_xticklabels(xlabels, fontsize=28)
    abort_ax.yaxis.set_tick_params(labelsize=28)
    abort_ax.set_ylim([0, 50])
    # abort_ax.set_yscale("log")

    abort_handles, abort_labels = abort_ax.get_legend_handles_labels()
    # print len(abort_handles)
    f.legend(abort_handles, abort_labels, 
             loc='upper left',  ncol=1, bbox_to_anchor=(0.15, 0.95), fontsize=26)

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())
