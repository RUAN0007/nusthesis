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
    data_path = os.path.join(curDir, "data", "txn", "smallbank_prov")
    x_axis, series_names, series = config.parse(data_path)
    # print x_axis
    # print series_names
    # print series
    
    xlabels = x_axis

    # Combine two series with and without dep capture into a single bar set. 
    series_names = [] # Override later
    basis = {}  # Basis performance with the provenance capture
    overheads = {} # Performance gain without the capture
    overhead_rates = {}
    for storage_type in [config.ldb_prov_label, config.forkbase_label]:
        system_label_wo_capture =  config.make_label(storage_type, config.fg_scheduler_label)
        system_label = system_label_wo_capture
        system_label_with_capture = "{}(Dep)".format(system_label) # The format correspond to data files

        series_names.append(system_label)
        basis[system_label] = [] 
        overheads[system_label] = []
        overhead_rates[system_label] = []

        point_count = len(series[system_label_with_capture])

        for i in range(point_count):
            result_with_capture = series[system_label_with_capture][i]
            result_wo_capture = series[system_label_wo_capture][i]
            overhead = result_wo_capture - result_with_capture
            basis[system_label].append(result_with_capture)
            overheads[system_label].append(overhead)
            overhead_rates[system_label].append(overhead / result_wo_capture)

    series_count = len(series_names)
    width, offsets = config.compute_width_offsets(series_count)

    f, (ax) = plt.subplots()
    overhead_ax = ax.twinx()
    overhead_hatch = "///"
    # # f.set_size_inches(, 4)
    for i, series_name in enumerate(series_names):
        base_data = basis[series_name]
        overhead_data = overheads[series_name]
        rate_data = overhead_rates[series_name]

        series_offsets = [offsets[i]] * len(base_data)
        base_xticks = range(len(base_data))
        xticks = config.sum_list(base_xticks, series_offsets) 
        # print xticks
        # print series_name
        # print base_data
        ax.bar(xticks, base_data, width=width, color=config.colors[series_name], edgecolor='black',align='center', label=series_name)
        ax.bar(xticks, overhead_data, width=width, color="white", edgecolor=config.colors[series_name],align='center', hatch=overhead_hatch, bottom=base_data)
        config.line_opts[series_name]["markerfacecolor"] = "white"
        overhead_ax.plot(base_xticks, rate_data,  config.fmts[series_name], **config.line_opts[series_name])
            

    # ax.set_title("Throughput and Abort Rate")
    ax.set(xlabel=r'Zipfian coefficient $\theta$', ylabel='Bar (tps)')
    ax.set_xticks(base_xticks)
    ax.set_xticklabels(xlabels, fontsize=16)
    ax.set_ylim([0, 2200])
    ax.set_yticks([0, 250, 500, 750, 1000, 1250, 1500])

    overhead_ax.set_ylim([-0.5, 0.75])
    overhead_ax.set_yticks([0, .25, .5, .75])
    overhead_ax.set_yticklabels(["0", "25", "50", "75"])
    overhead_ax.set(ylabel='Line (reduction rate %)')


    fake_overhead_bar = ax.bar(0, 0, color="white", edgecolor="black", hatch=overhead_hatch, label="Dependency\nOverhead")

    handles, labels = ax.get_legend_handles_labels()
    f.legend(handles, labels,
             loc='upper center', ncol=1, bbox_to_anchor=(0.36, 0.90), fontsize=16)
            #  columnspacing=1, handletextpad=1, fontsize=20)

    # f.legend([fake_overhead_bar], ["Dependency \nOverhead"],
            #  loc='upper center', ncol=1, bbox_to_anchor=(0.73, 0.90), fontsize=16)

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())