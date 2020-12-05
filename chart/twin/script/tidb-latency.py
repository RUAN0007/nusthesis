import sys
from common import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl

# e2e_delay = [564,691,714,992,1150,1154,1065]
# sql_parse = [0.056,0.051,0.046,0.043,0.04,0.038,0.03]
# sql_compile = [1.368,1.414,0.907,1.31,1.27,0.85,1.076]
# p1_commit = [255,356,325,470,544,551,498]
# p2_commit = [276,300,357,481,557,546,506]

e2e_delay = [564,691,714,992,1150]
sql_parse = [0.056,0.051,0.046,0.043,0.04]
sql_compile = [1.368,1.414,0.907,1.31,1.27]
p1_commit = [255,356,325,470,544]
p2_commit = [276,300,357,481,557]
other = []

label = range(2000, 4001, 500)
for i in range(len(e2e_delay)):
    other.append(e2e_delay[i] - sql_parse[i] - sql_compile[i] - p1_commit[i] - p2_commit[i])

parse_color="red"
compile_color="lightblue"
p1_commit_color="green"
p2_commit_color="limegreen"
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
    width = 0.6

    bottom = [0] * len(label)
    delay_ax.bar(xticks, sql_parse, width=width, color=parse_color, 
                 label="SQL-parse", edgecolor="black", hatch="xxx")

    bottom = sum_list(bottom, sql_parse)
    delay_ax.bar(xticks, sql_compile, width=width, bottom=bottom, 
                 color=compile_color, label="SQL-compile", edgecolor="black")
    
    bottom = sum_list(bottom, sql_compile)
    delay_ax.bar(xticks, p1_commit, width=width, bottom=bottom, 
                 color=p1_commit_color, label="Phase1-commit", edgecolor="black", hatch="///")

    bottom = sum_list(bottom, p1_commit)
    delay_ax.bar(xticks, p2_commit, width=width, bottom=bottom, 
                 color=p2_commit_color, label="Phase2-commit", edgecolor="black", hatch="\\\\\\")

    bottom = sum_list(bottom, p2_commit)
    delay_ax.bar(xticks, other, width=width, bottom=bottom, 
                 color=other_color, label="Other", edgecolor="black", hatch="ooo")

    delay_ax.set_title("TiDB Latency Breakdown", fontsize=24)
    delay_ax.set(xlabel="Request rate (tps)", ylabel='ms')
    delay_ax.set_xticks(xticks)
    delay_ax.set_xticklabels(label, fontsize=22)
    delay_ax.set_ylim([0, 2200])
    # delay_ax.set_yscale("log")

    delay_handles, delay_labels = delay_ax.get_legend_handles_labels()
    print len(delay_handles)
    f.legend(delay_handles, delay_labels, 
             loc='upper left',  ncol=1, bbox_to_anchor=(0.175, 0.85) , fontsize=18)

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())