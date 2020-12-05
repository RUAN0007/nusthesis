import sys
from common import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl

# Use fabric to format ahl_full_swap
kAhlFullSwapLabel, ahl_FullSwap_FMT, ahl_FullSwap_OPTS = kFabricLabel, FAB_FMT, FAB_LINE_OPTS
ahl_FullSwap_OPTS["label"] = "AHL(Periodic Reconfig)"

# Use quorum to format ahl_no_swap
kAhlNoSwapLabel, ahl_NoSwap_FMT, ahl_NoSwap_OPTS = kQuorumLabel , QUO_FMT , QUO_LINE_OPTS
QUO_LINE_OPTS["label"] = "AHL(Fixed Members)"
# Use etcd for format spanner
kSpannerLabel, spanner_fmt, spanner_OPTS = kEtcdLabel, ETCD_FMT, ETCD_LINE_OPTS
spanner_OPTS["label"] = "Spanner"

thruput = {kAhlFullSwapLabel: [7.65 , 13.5 , 19.96333333 , 23.36333333 , 24.95666667], 
           kAhlNoSwapLabel: [12.55666667,28.18333333,42.59,33.91333333,39.31666667], 
        #    kCockDBLabel: [22065,17727,9177,1465],
           kTiDBLabel: [543.0333271,691.1351728,857.3887249,1004.772903,1088.728142],
           kSpannerLabel: [611.3569382,622.3281865,572.9847225,560.0947448,606.2523178]}

# labels = [kFabricLabel, kQuorumLabel, kCockDBLabel, kTiDBLabel, kEtcdLabel]
# xlabels = ["3 (1)", "12 (4)", "24 (8)", "36 (12)", "48 (16)"]
xlabels = ["3", "12", "24", "36", "48"]

def main():
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""
    
#     print path
    f, (thruput_ax) = plt.subplots()
    # f.set_size_inches(, 4)
    xticks = range(len(xlabels))

    thruput_ax.plot(xticks, thruput[kAhlFullSwapLabel], ahl_FullSwap_FMT, **ahl_FullSwap_OPTS)
    thruput_ax.plot(xticks, thruput[kAhlNoSwapLabel], ahl_NoSwap_FMT, **ahl_NoSwap_OPTS)
    thruput_ax.plot(xticks, thruput[kTiDBLabel], TiDB_FMT, **TiDB_LINE_OPTS)
    thruput_ax.plot(xticks, thruput[kSpannerLabel], spanner_fmt, **spanner_OPTS)

    # thruput_ax.set_title("Throughput")
    thruput_ax.set(xlabel="# of server nodes (shards)", ylabel='tps')
    thruput_ax.set_xticks(xticks)
    thruput_ax.set_xticklabels(xlabels, fontsize=18)
    thruput_ax.set_ylim([5, 25000])
    thruput_ax.set_yscale("log")

    thruput_handles, thruput_labels = thruput_ax.get_legend_handles_labels()
    f.legend(thruput_handles, thruput_labels, fontsize=14,
             loc='upper center', ncol=2, bbox_to_anchor=(0.55, 0.90))

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())
