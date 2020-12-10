import sys
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl
import config

def main():
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""
    

    curDir = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(curDir, "data", "txn", "ycsb_thruput")
    x_axis, series_names, series = config.parse(data_path)
    # print x_axis
    # print series_names
    # print series
    
    blk_sizes = x_axis
    xlabels = [str(int(x)/100) for x in blk_sizes]


    original_label = config.make_label_by_storage(config.original_label)
    series_names = [original_label] # override the series name, to be appended later.

    # Combine series for different schedulers of Fabric# and FabricProv respectively
    gains = {}
    for storage_type in [config.ldb_prov_label, config.forkbase_label]:
        system_label =  config.make_label_by_storage(storage_type)
        series_names.append(system_label)
        series[system_label] = [] # the min of the original and the sharp scheduler
        gains[system_label] = [] # fg scheduler - original scheduler

        original_scheduler = config.make_label(storage_type, config.original_scheduler_label)
        fg_scheduler = config.make_label(storage_type, config.fg_scheduler_label)

        original_scheduler_result = series[original_scheduler]
        fg_scheduler_result = series[fg_scheduler]

        for i in range(len(original_scheduler_result)):
            if original_scheduler_result[i] < fg_scheduler_result[i]:
                series[system_label].append(original_scheduler_result[i])
            else:
                series[system_label].append(fg_scheduler_result[i])
            gains[system_label].append(fg_scheduler_result[i] - original_scheduler_result[i])

        config.colors[system_label] = config.raw_colors[storage_type]

    series_count = len(series_names)
    width, offsets = config.compute_width_offsets(series_count)

    f, (ax) = plt.subplots()
    f.set_size_inches(9, 5)
    for i, series_name in enumerate(series_names):
        series_data = series[series_name]
        series_offsets = [offsets[i]] * len(series_data)
        base_xticks = range(len(series_data))
        xticks = config.sum_list(base_xticks, series_offsets) 
        # print xticks
        # print series_name
        # print series_data
        ax.bar(xticks, series_data, width=width, color=config.colors[series_name], edgecolor='black',align='center', label=series_name)

    speedup_hatch = "xxx"
    overhead_hatch = None
    for i, storage_type in enumerate([config.ldb_prov_label, config.forkbase_label]):
        system_label =  config.make_label_by_storage(storage_type)
        gains_data = gains[system_label]
        base_data = series[system_label]
        series_offsets = [offsets[i+1]] * len(gains_data) # i+1 due to Fabric as the first bar. 
        base_xticks = range(len(gains_data))
        xticks = config.sum_list(base_xticks, series_offsets) 

        # We draw bar one by one as their hatches may be different.
        for i, gain in enumerate(gains_data):
            if 0 < gain:
                hatch_type = speedup_hatch
            else:
                hatch_type = overhead_hatch
            ax.bar(xticks[i], gain, width=width, color="white", edgecolor=config.colors[system_label],align='center', hatch=hatch_type, bottom=base_data[i])


    # ax.set_title("Throughput")
    ax.set(xlabel='# of txns per block (x100)', ylabel='tps')
    ax.set_xticks(base_xticks)
    ax.set_xticklabels(xlabels)
    ax.set_ylim([0, 2500])

    handles, labels = ax.get_legend_handles_labels()
    f.legend(handles, labels,
             loc='upper center', ncol=1, bbox_to_anchor=(0.35, 0.90), fontsize=20)
            #  columnspacing=1, handletextpad=1, fontsize=20)
    
    fake_speedup_bar = ax.bar(0, 0, color="white", edgecolor="black", hatch=speedup_hatch)
    fake_overhead_bar = ax.bar(0, 0, color="white", edgecolor="black", hatch=overhead_hatch)
    f.legend([fake_speedup_bar, fake_overhead_bar], ["Speedup", "Overhead"],
             loc='upper center', ncol=1, bbox_to_anchor=(0.75, 0.90), fontsize=20)
    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())