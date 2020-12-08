import sys
import config
import os

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl


def main():
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""
    
    blk_hatch, state_hatch, txn_verification_hatch, other_hatch = "xxxx", "ooo", "\\\\", None
    f, (ax) = plt.subplots()
    # # f.set_size_inches(, 4)

    curDir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(curDir, "data", "provenance","ycsb_breakdown", "block_persistence")
    x_axis, series_names, series = config.parse(data_path)

    xlabels = x_axis
    series_count = len(series_names)
    width, offsets = config.compute_width_offsets(series_count)

    bottoms = {}
    for i, series_name in enumerate(series_names):
        series_data = series[series_name]
        series_offsets = [offsets[i]] * len(series_data)
        base_xticks = range(len(series_data))
        xticks = config.sum_list(base_xticks, series_offsets) 
        # print xticks
        # print series_name
        # print series_data
        ax.bar(xticks, series_data, width=width, color="white", edgecolor=config.base_colors[series_name],align='center', hatch=blk_hatch)
        bottoms[series_name] = series_data


    curDir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(curDir, "data", "provenance","ycsb_breakdown", "state_persistence")
    x_axis, series_names, series = config.parse(data_path)

    for i, series_name in enumerate(series_names):
        series_data = series[series_name]
        series_offsets = [offsets[i]] * len(series_data)
        base_xticks = range(len(series_data))
        xticks = config.sum_list(base_xticks, series_offsets) 
        ax.bar(xticks, series_data, width=width, color="white", edgecolor=config.base_colors[series_name],align='center', hatch=state_hatch, bottom=bottoms[series_name])
        bottoms[series_name] = config.sum_list(bottoms[series_name], series_data)


    curDir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(curDir, "data", "provenance","ycsb_breakdown", "txn_verification")
    x_axis, series_names, series = config.parse(data_path)

    for i, series_name in enumerate(series_names):
        series_data = series[series_name]
        series_offsets = [offsets[i]] * len(series_data)
        base_xticks = range(len(series_data))
        xticks = config.sum_list(base_xticks, series_offsets) 
        ax.bar(xticks, series_data, width=width, color="white", edgecolor=config.base_colors[series_name],align='center', hatch=txn_verification_hatch, bottom=bottoms[series_name])
        bottoms[series_name] = config.sum_list(bottoms[series_name], series_data)


    curDir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(curDir, "data", "provenance","ycsb_breakdown", "other")
    x_axis, series_names, series = config.parse(data_path)

    for i, series_name in enumerate(series_names):
        series_data = series[series_name]
        series_offsets = [offsets[i]] * len(series_data)
        base_xticks = range(len(series_data))
        xticks = config.sum_list(base_xticks, series_offsets) 
        ax.bar(xticks, series_data, width=width, color="white", edgecolor=config.base_colors[series_name],align='center', hatch=other_hatch, bottom=bottoms[series_name])
        bottoms[series_name] = config.sum_list(bottoms[series_name], series_data)
    
    ## Fake bars for legends
    fake_bars = []
    fake_bars.append(ax.bar(0, 0, hatch=blk_hatch, color="white", edgecolor="black"))
    fake_bars.append(ax.bar(0, 0, hatch=state_hatch,color="white",  edgecolor="black"))
    fake_bars.append(ax.bar(0, 0, hatch=txn_verification_hatch, color="white", edgecolor="black"))
    fake_bars.append(ax.bar(0, 0, hatch=other_hatch,color="white",  edgecolor="black"))
    f.legend(fake_bars, ["Block Persistence", "State Persistence", "Txn Verification", "Other"],
             loc='upper left', ncol=1, bbox_to_anchor=(0.17, 0.89), fontsize=16) 

    fake_bars = []
    fake_bars.append(ax.bar(0, 0, color=config.kFabricColor))
    fake_bars.append(ax.bar(0, 0, color=config.kFabricProvOColor))
    fake_bars.append(ax.bar(0, 0, color=config.kFabricSharpOColor))
    f.legend(fake_bars, [config.kFabricLabel, config.kFabricProvOLabel, config.kFabricSharpOLabel],
             loc='upper left', ncol=1, bbox_to_anchor=(0.61,0.89), fontsize=14) 

    # ax.set_title("Throughput and Abort Rate")
    ax.set(xlabel=r'# Txns per Block (x100)', ylabel='ms')
    ax.set_xticks(base_xticks)
    ax.set_xticklabels(xlabels)
    ax.set_ylim([0, 1200])
    # ax.set_yticks([0, 250, 500, 750, 1000, 1250, 1500])

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())