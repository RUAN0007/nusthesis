import sys
from common import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl

mpl.rcParams['legend.fontsize'] = 12

fabric_proposal = [131, 120, 234, 460]
fabric_order = [912, 915, 851, 1604]
fabric_validation = [465, 476, 592, 915]


quorum_proposal = [4, 10, 26, 178]
quorum_order = [ 53, 56, 76, 408 ]
quorum_validation = [3, 8, 31, 221]

proposal_color="red"
order_color="lightblue"
validation_color="green"

fabric_hatch="xxx"
quorum_hatch="ooo"

kProposalLabel = "proposal"
kOrderLabel = "consensus"
kValidationLabel = "validation"

xlabels = [10, 100, 1000, 5000]

def main():
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""
    
#     print path
    f, (latency_ax) = plt.subplots()
    # f.set_size_inches(, 4)
    xticks = range(len(xlabels))
    width = 0.4
    fabric_xticks = sum_list(xticks, [-0.2] * len(xlabels))

    bottom = [0] * len(xticks)
    latency_ax.bar(fabric_xticks, fabric_proposal, width=0.4, color=proposal_color, edgecolor='black',
                   hatch=fabric_hatch, label=kFabricLabel + "-" + kProposalLabel)

    bottom = sum_list(bottom, fabric_proposal)
    latency_ax.bar(fabric_xticks, fabric_order, width=0.4, color=order_color, edgecolor='black',
                   hatch=fabric_hatch, label=kFabricLabel + "-" + kOrderLabel, bottom=bottom)

    bottom = sum_list(bottom, fabric_order)
    latency_ax.bar(fabric_xticks, fabric_validation, width=0.4, color=validation_color, edgecolor='black',
                   hatch=fabric_hatch, label=kFabricLabel + "-" + kValidationLabel, bottom=bottom)


    quorum_xticks = sum_list(xticks, [0.2] * len(xlabels))

    bottom = [0] * len(xticks)
    latency_ax.bar(quorum_xticks, quorum_proposal, width=0.4, color=proposal_color, edgecolor='black',
                   hatch=quorum_hatch, label=kQuorumLabel + "-" + kProposalLabel)

    bottom = sum_list(bottom, quorum_proposal)
    latency_ax.bar(quorum_xticks, quorum_order, width=0.4, color=order_color, edgecolor='black',
                   hatch=quorum_hatch, label=kQuorumLabel + "-" + kOrderLabel, bottom=bottom)

    bottom = sum_list(bottom, quorum_order)
    latency_ax.bar(quorum_xticks, quorum_validation, width=0.4, color=validation_color, edgecolor='black',
                   hatch=quorum_hatch, label=kQuorumLabel + "-" + kValidationLabel, bottom=bottom)
    # The following bars are fake to generate the customized legend. 
    fakeFabric = latency_ax.bar(0, 0,label="Fabric", color="white", edgecolor="black", hatch=fabric_hatch)
    fakeQuorum = latency_ax.bar(0, 0,label="Quorum", color="white", edgecolor="black", hatch=quorum_hatch)
    fakeProposal = latency_ax.bar(0, 0,label="Proposal", color=proposal_color, edgecolor="black")
    fakeConsensus = latency_ax.bar(0, 0,label="Consensus", color=order_color, edgecolor="black")
    fakeCommit = latency_ax.bar(0, 0,label="Commit", color=validation_color, edgecolor="black")

    # latency_ax.bar(fabric_xticks, fabric_state, width=0.4, color=base_colors[kFabricLabel], 
    #              edgecolor='black', hatch=base_hatches[kFabricLabel], label=kFabricLabel+"-state")

    # latency_ax.bar(fabric_xticks, fabric_blk, width=0.4, color='lightblue', 
    # edgecolor='black', hatch=base_hatches[kFabricLabel], label=kFabricLabel+"-block",
    # bottom=fabric_state)

    # latency_ax.set_title("Latency Breakdown")
    latency_ax.set_xlabel("Record size (byte)", fontsize=24)
    latency_ax.set_ylabel("ms", fontsize=22)
    latency_ax.set_xticks(xticks)
    latency_ax.set_xticklabels(xlabels, fontsize=18)
    latency_ax.set_ylim([10, 90000])
    latency_ax.set_yscale("log")

    latency_handles, latency_labels = latency_ax.get_legend_handles_labels()
    f.legend([fakeProposal, fakeConsensus, fakeCommit,fakeFabric, fakeQuorum], [ "Proposal", "Consensus", "Commit","Fabric", "Quorum"], fontsize=18, ncol=2, loc='upper center', bbox_to_anchor=(0.57, 0.97))
    # f.legend(latency_handles, latency_labels, fontsize=14,
            #  loc='upper left',  ncol=2, bbox_to_anchor=(0.182, 0.86))

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())
