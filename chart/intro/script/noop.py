import sys
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl
import config

thruputs = [617, 1309, 1707, 1723, 2239, 2365, 2427, 2422]
blkSizes = [100, 500, 1000, 1500, 2000, 3000, 4000, 5000]

def main():
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""
    
    f, (ax) = plt.subplots()
    # f.set_size_inches(, 4)
    xlabels = [str(x/100) for x in blkSizes]
    xticks = [x + 0.5 for x in range(len(xlabels))]
    ax.bar(xticks, thruputs, width=0.6, color="blue", edgecolor='black')

    ax.set_title("Throughput")
    ax.set(xlabel=r'# Txns per Block (x100)', ylabel='tps')
    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels)
    ax.set_ylim([0, 3000])

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())