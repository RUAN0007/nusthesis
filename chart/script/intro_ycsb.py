import sys
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl
import config

# thruputs = [308, 1031, 1481, 1571, 1458, 1535]
# blkSizes = [100, 500, 1000, 1500, 2000, 2500]

thruputs = [308, 520, 876, 1088, 1257, 1481, 1571, 1458, 1535]
blkSizes = [100, 200, 400, 600, 800, 1000, 1500, 2000, 2500]

def main():
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""
    
    f, (ax) = plt.subplots()
    # f.set_size_inches(, 4)
    xlabels = [str(x/100) for x in blkSizes]
    xticks = [x + 0.5 for x in range(len(xlabels))]
    color = config.raw_colors[config.original_label]

    ax.bar(xticks, thruputs, width=0.6, color=color, edgecolor='black')

    # ax.set_title("YCSB Throughput")
    ax.set(xlabel=r'# of txns per block (x100)', ylabel='tps')
    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels)
    ax.set_ylim([0, 2000])
    ax.hlines(1500, 0, 9, colors='red', linestyles='--')

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())