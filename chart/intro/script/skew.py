import sys
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl
import config

thruputs = [845, 884, 872, 860, 773, 549]
zipfian = [0, 0.2, 0.4, 0.6, 0.8, 1]
abortRatio = [0.5362239297, 0.511871894, 0.4993407917, 0.5308237861, 0.5379557681, 0.6830254042]

def main():
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""
    
    f, (ax) = plt.subplots()
    # f.set_size_inches(, 4)
    xlabels = [str(s) for s in zipfian]
    xticks = [x + 0.5 for x in range(len(xlabels))]
    handles = []
    h1 = ax.bar(xticks, thruputs, width=0.6, color="orange", edgecolor='black', label="Throughput")
    handles.append(h1)


    ax.set_title("Skewed Workload \n Performance")
    ax.set(xlabel=r'Zipfian Coefficient $\theta$', ylabel='tps')
    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels)

    ax.set_ylim([0, 1800])

    ratioAx = ax.twinx()
    ratioAx.plot(xticks, abortRatio, "bo", linestyle="-", linewidth=1, markersize=14, markerfacecolor="purple", color="purple", label="Abort Ratio")
    ratioAx.set_ylim([-0.2,1.0])
    ratioAx.set(xlabel=r'Zipfian Coefficient $\theta$', ylabel='Percentage(%)')
    ratioAx.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    h2, _ = ratioAx.get_legend_handles_labels()
    handles.extend(h2)
    
    f.legend(handles, ["Throughput", "Abort Ratio"],
             loc='upper center', ncol=2,bbox_to_anchor=(0.50, 0.73))

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())