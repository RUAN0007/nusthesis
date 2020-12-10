import sys
from common import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl

# abort = {
#            kFabricLabel: [0.14,0.1612,0.1807,0.18475,0.2935,0.4565], 
#            kTiDBLabel: [0,0.02,0.021,0.0217,0.025,0.16],
#            }

kIncosisntencyLabel="Inconsistent Read (Fabric)"
kRWConflictLabel   ="Read-write Conflict (Fabric)"

abort = {
           kIncosisntencyLabel: [0, 0.02, 0.096, 0.1, 0.09479, 0.12247], 
           kRWConflictLabel: [0.01807228916, 0.08534836066, 0.4326285714, 0.6418230563, 0.7304742525, 0.75116568],
           kTiDBLabel: [0.0043, 0.017, 0.069, 0.146, 0.22, 0.326],
           }

abort[kIncosisntencyLabel] = [value * 100.0 for value in abort[kIncosisntencyLabel]]
abort[kRWConflictLabel] = [value * 100.0 for value in abort[kRWConflictLabel]]
abort[kTiDBLabel] = [value * 100.0 for value in abort[kTiDBLabel]]

# labels = [kFabricLabel, kQuorumLabel, kCockDBLabel, kTiDBLabel, kEtcdLabel]
xlabels = [1, 2,4,6,8,10]

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
    abort_ax.bar(fabric_xticks, abort[kRWConflictLabel], width=0.4, color="green", 
                 edgecolor='black', label=kRWConflictLabel)

    abort_ax.bar(fabric_xticks, abort[kIncosisntencyLabel], width=0.4, color="blue", 
                 edgecolor='black', label=kIncosisntencyLabel,bottom=abort[kRWConflictLabel])


    tidb_xticks = sum_list(xticks, [0.2] * len(xlabels))
    abort_ax.bar(tidb_xticks, abort[kTiDBLabel], width=0.4, color=base_colors[kTiDBLabel], 
                #  edgecolor='black', hatch=base_hatches[kTiDBLabel], label=kTiDBLabel)
                 edgecolor='black', label=kTiDBLabel)

    # abort_ax.set_title("Abort Rate", fontsize=46)

    abort_ax.set_xlabel('# of ops per txn', fontsize=28)
    abort_ax.set_ylabel('percent (%)', fontsize=28)

    abort_ax.set_xticks(xticks)
    abort_ax.set_xticklabels(xlabels, fontsize=28)
    abort_ax.yaxis.set_tick_params(labelsize=28)
    abort_ax.set_ylim([0, 140])
    # abort_ax.set_yscale("log")

    abort_handles, abort_labels = abort_ax.get_legend_handles_labels()
    print(len(abort_handles))
    f.legend(abort_handles, abort_labels, 
             loc='upper left',  ncol=1, bbox_to_anchor=(0.19, 0.97), fontsize=25)

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())
