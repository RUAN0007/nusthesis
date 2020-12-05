import sys
from common import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl

fabric_authentication = 4294
fabric_simulation = 406
fabric_endorsement = 59

tidb_parse=16
tidb_compile=15
tidb_storage=275

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
    width = 0.25

    latency_ax.bar(-0.25, fabric_authentication, width=width, color="red", edgecolor='black', hatch=fabric_hatch, label="Authentication")
    latency_ax.bar(0, fabric_simulation, width=width,color="orange", edgecolor='black', hatch=fabric_hatch, label="Simulation")
    latency_ax.bar(0.25, fabric_endorsement, width=width,color="yellow", edgecolor='black', hatch=fabric_hatch, label="Endorsement")

    text_font_size=18
    latency_ax.text(-0.25, fabric_authentication, fabric_authentication, ha="center",  va="bottom", fontsize=text_font_size)
    latency_ax.text(0, fabric_simulation, fabric_simulation, ha="center",  va="bottom",fontsize=text_font_size)
    latency_ax.text(0.25, fabric_endorsement, fabric_endorsement, ha="center",  va="bottom",fontsize=text_font_size)


    latency_ax.bar(0.75, tidb_parse, width=width, color="blue", edgecolor='black', hatch=tidb_hatch, label="SQL-parse")
    latency_ax.bar(1, tidb_compile, width=width,color="lightblue", edgecolor='black', hatch=tidb_hatch,label="SQL-compile")
    latency_ax.bar(1.25, tidb_storage, width=width,color="green", edgecolor='black', hatch=tidb_hatch, label="Storage-get")

    latency_ax.text(0.75, tidb_parse, tidb_parse, ha="center", va="bottom", fontsize=text_font_size)
    latency_ax.text(1, tidb_compile, tidb_compile, ha="center", va="bottom", fontsize=text_font_size)
    latency_ax.text(1.25, tidb_storage, tidb_storage, ha="center", va="bottom", fontsize=text_font_size)

    #latency_ax.set_title("Query")
    latency_ax.set(ylabel='us')
    latency_ax.set_xticks([0, 1])
    latency_ax.set_xticklabels([kFabricLabel, kTiDBLabel], fontsize=22)
    latency_ax.set_ylim([0, 5000])

    latency_handles, latency_labels = latency_ax.get_legend_handles_labels()
    f.legend(latency_handles, latency_labels, fontsize=20,
             loc='upper left',  ncol=1, bbox_to_anchor=(0.45, 0.95))

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())
