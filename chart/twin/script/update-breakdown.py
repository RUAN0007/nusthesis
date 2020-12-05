import sys
from common import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl

# [unsaturated, saturated]
fabric_proposal = [206, 404]
fabric_consensus = [802, 832]
fabric_buffer = [85, 6415]
fabric_validation = [604, 737]

tidb_prewrite= [210, 260]
tidb_commit = [227, 280]

# fabric_hatch=base_hatches[kFabricLabel]
# tidb_hatch=base_hatches[kTiDBLabel]
fabric_hatch=None
tidb_hatch=None

def main():
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""
    
#     print path
    f, (latency_ax) = plt.subplots()
    # f.set_size_inches(9, 4)
    width = 0.4

    fabric_xticks = [-0.25, .25]
    bottom = [0, 0]
    latency_ax.bar(fabric_xticks, fabric_proposal, width=width, color="red", edgecolor='black', hatch=fabric_hatch, label="Execute", bottom=bottom)

    bottom = sum_list(bottom, fabric_proposal)
    latency_ax.bar(fabric_xticks, fabric_consensus, width=width, color="orange", edgecolor='black', hatch=fabric_hatch, label="Order", bottom=bottom)

    bottom = sum_list(bottom, fabric_consensus)
    latency_ax.bar(fabric_xticks, fabric_buffer, width=width, color="yellow", edgecolor='black', hatch=fabric_hatch, label="Buffer", bottom=bottom)

    bottom = sum_list(bottom, fabric_buffer)
    latency_ax.bar(fabric_xticks, fabric_validation, width=width, color="coral", edgecolor='black', hatch=fabric_hatch, label="Validate", bottom=bottom)
    
    bottom = sum_list(bottom, fabric_validation)
    latency_ax.text(fabric_xticks[0], bottom[0], "Unsaturated", ha="center", va="bottom", fontsize=16, rotation=45)
    latency_ax.text(fabric_xticks[1], bottom[1], "Saturated", ha="center", va="bottom", fontsize=16, rotation=45)


    tidb_xticks = [1.25, 1.75]
    bottom = [0, 0]
    # latency_ax.bar(tidb_xticks, tidb_prewrite, width=width, color="blue", edgecolor='black', hatch=tidb_hatch, label="Prepare(2PC-1)", bottom=bottom)

    # bottom = sum_list(bottom, tidb_prewrite)
    # latency_ax.bar(tidb_xticks, tidb_commit, width=width, color="green", edgecolor='black', hatch=tidb_hatch, label="Commit(2PC-2)", bottom=bottom)
    # bottom = sum_list(bottom, tidb_commit)
    
    total_commit = sum_list(tidb_prewrite, tidb_commit)
    latency_ax.bar(tidb_xticks, total_commit, width=width, color="green", edgecolor='black', hatch=tidb_hatch, label="TiDB")


    bottom = total_commit
    latency_ax.text(tidb_xticks[0], bottom[0], "Unsaturated", ha="center", va="bottom", fontsize=16, rotation=45)
    latency_ax.text(tidb_xticks[1], bottom[1]+400, "Saturated", ha="center", va="bottom", fontsize=16, rotation=45)


    # latency_ax.set_title("Update")
    latency_ax.set(ylabel='ms')
    latency_ax.set_xticks([0, 1.5])
    latency_ax.set_xticklabels([kFabricLabel, kTiDBLabel], fontsize=24)
    latency_ax.set_ylim([0, 18500])

    latency_handles, latency_labels = latency_ax.get_legend_handles_labels()
    f.legend(latency_handles, latency_labels, fontsize=20,
             loc='upper left',  ncol=1, bbox_to_anchor=(0.58, 0.95))

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())
