import sys
from common import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl

label = range(400, 651, 50)

post_execution = [396,451,497,538,579,539]
post_consensus = [385,412,455,487,483,488]
post_validation = [382,414,422,425,422,421]

num_point = 5

label = label[0:num_point]
post_execution = post_execution[0:num_point]
post_consensus = post_consensus[0:num_point]
post_validation = post_validation[0:num_point]

proposal_color="red"
order_color="lightblue"
validation_color="green"

def main():
    if 1 < len(sys.argv) :
        diagram_path = sys.argv[1]
    else:
        diagram_path = ""
    
#     print path
    f, (thruput_ax) = plt.subplots()
    # f.set_size_inches(, 4)
    xticks = range(len(label))

    PostExecution_FMT = CockDB_FMT # Borrow style from tidb
    PostExecution_LINE_OPT = CockDB_LINE_OPTS
    PostExecution_LINE_OPT["label"] = 'Post-proposal'
    thruput_ax.plot(xticks, post_execution, PostExecution_FMT, **PostExecution_LINE_OPT)

    PostConsensus_FMT = TiDB_FMT # Borrow style from cockdb 
    PostConsensus_LINE_OPT = TiDB_LINE_OPTS
    PostConsensus_LINE_OPT["label"] = 'Post-consensus'
    thruput_ax.plot(xticks, post_consensus,  PostConsensus_FMT, **PostConsensus_LINE_OPT)

    postValidation_FMT = FAB_FMT # Borrow style from fabric 
    postValidation_LINE_OPT = FAB_LINE_OPTS
    postValidation_LINE_OPT["label"] = 'Post-validation'
    thruput_ax.plot(xticks, post_validation,  postValidation_FMT, **postValidation_LINE_OPT)
    
    thruput_ax.set_title("Fabric")
    thruput_ax.set(xlabel="Request rate (tps)", ylabel='tps')
    thruput_ax.set_xticks(xticks)
    thruput_ax.set_xticklabels(label, fontsize=14)
    thruput_ax.set_ylim([300, 600])

    thruput_handles, thruput_labels = thruput_ax.get_legend_handles_labels()
    print len(thruput_handles)
    f.legend(thruput_handles, thruput_labels, 
             loc='upper left',  ncol=1, bbox_to_anchor=(0.15, 0.89))

    if diagram_path == "":
        plt.tight_layout()
        plt.show()
    else:
        f.tight_layout()
        f.savefig(diagram_path, bbox_inches='tight')
    

if __name__ == "__main__":
    sys.exit(main())