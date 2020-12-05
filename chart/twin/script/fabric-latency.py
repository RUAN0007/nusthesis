import sys
from common import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl

e2e_delay = [693,666,635,688,835,1403,3483]
execute = [25,20,20,44,49,67,51]
consensus = [262,214,177,146,138,157,118]
validation = [222,207,235,271,359,921,3211]
other = []
label = range(200, 501, 50)
for i in range(len(e2e_delay)):
    other.append(e2e_delay[i] - execute[i] - consensus[i] - validation[i])

proposal_color="red"
order_color="lightblue"
validation_color="green"
other_color="grey"

def main():
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""
    
#     print path
    f, (delay_ax) = plt.subplots()
    # f.set_size_inches(, 4)
    xticks = range(len(label))
    width = 0.8

    bottom = [0] * len(label)
    delay_ax.bar(xticks, execute, width=width, color=proposal_color, 
                 label="Proposal", edgecolor="black", hatch="///")

    bottom = sum_list(bottom, execute)
    delay_ax.bar(xticks, consensus, width=width, bottom=bottom, 
                 color=order_color, label="Consensus", edgecolor="black", hatch="xxxx")
    
    bottom = sum_list(bottom, consensus)
    delay_ax.bar(xticks, validation, width=width, bottom=bottom, 
                 color=validation_color, label="Commit", edgecolor="black")

    bottom = sum_list(bottom, validation)
    delay_ax.bar(xticks, other, width=width, bottom=bottom, 
                 color=other_color, label="Other", edgecolor="black", hatch="oooo")
    
    delay_ax.plot((4.5, 4.5), (0, 5000), linestyle="--", color="r")

    delay_ax.set_title("Fabric Latency Breakdown", fontsize=24)
    delay_ax.set(xlabel="Request rate (tps)", ylabel='ms')
    delay_ax.set_xticks(xticks)
    delay_ax.set_xticklabels(label, fontsize=20)
    delay_ax.set_ylim([0, 5000])
    # delay_ax.set_yscale("log")

    delay_handles, delay_labels = delay_ax.get_legend_handles_labels()
    # print len(delay_handles)
    f.legend(delay_handles, delay_labels, 
             loc='upper left',  ncol=1, bbox_to_anchor=(0.20, 0.85), fontsize=20) #)

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())