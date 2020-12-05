import os

kMarkerSize=14
kLineWidth=1
kLineStyle="-"
kCockDbColor, kTiDBColor, kFabricColor, kQuorumColor, kEtcdColor, kTikvColor = "coral", "orange", 'g', 'skyblue', 'r', 'brown'
kCockDbMarker, kTiDBMarker, kFabricMarker, kQuorumMarker, kEtcdMarker, kTikvMarker = "x", "X", 'v', 's', 'o', 'p'
kCockDBLabel, kTiDBLabel, kFabricLabel, kQuorumLabel, kEtcdLabel, kTikvLabel = "CrDB", "TiDB", "Fabric", "Quorum", "Etcd", "TiKV"
base_colors = {kCockDBLabel: kCockDbColor, kTiDBLabel: kTiDBColor, kFabricLabel: kFabricColor, kQuorumLabel:kQuorumColor, kEtcdLabel: kEtcdColor, kTikvLabel: kTikvColor}
base_hatches = {kCockDBLabel: "xxx", kTiDBLabel: "xxx", kFabricLabel: "ooo", kQuorumLabel: "ooo", kEtcdLabel: "///", kTikvLabel: "///"}




# kCockDBLabel, kTiDBLabel, kFabricLabel, kQuorumLabel, kEtcd = "C-DB", "T-DB", "F-BC", "Q-BC", "E-DB"
# kCockDBLabel, kTiDBLabel, kFabricLabel, kQuorumLabel, kEtcd = "C", "T", "F", "Q", "E"

CockDB_FMT=kCockDbColor+kCockDbMarker
CockDB_LINE_OPTS={"linestyle": kLineStyle, "linewidth":kLineWidth, "markersize":kMarkerSize, 'markerfacecolor':kCockDbColor, "color":kCockDbColor, "label": kCockDBLabel}

TiDB_FMT=kTiDBMarker
TiDB_LINE_OPTS={"linestyle": kLineStyle, "linewidth":kLineWidth, "markersize":kMarkerSize, 'markerfacecolor':kTiDBColor, "color":kTiDBColor, "label": kTiDBLabel}

FAB_FMT=kFabricMarker
FAB_LINE_OPTS={"linestyle": kLineStyle, "linewidth":kLineWidth, "markersize":kMarkerSize, 'markerfacecolor':kFabricColor, "color":kFabricColor, "label": kFabricLabel}

QUO_FMT=kQuorumMarker
QUO_LINE_OPTS={"linestyle": kLineStyle, "linewidth":kLineWidth, "markersize":kMarkerSize, 'markerfacecolor':kQuorumColor, "color":kQuorumColor, "label": kQuorumLabel}

ETCD_FMT=kEtcdMarker
ETCD_LINE_OPTS={"linestyle": kLineStyle, "linewidth":kLineWidth, "markersize":kMarkerSize, 'markerfacecolor':kEtcdColor, "color":kEtcdColor, "label": kEtcdLabel}

FMT={kCockDBLabel: CockDB_FMT, kTiDBLabel: TiDB_FMT, kFabricLabel: FAB_FMT, kQuorumLabel: QUO_FMT, kEtcdLabel: ETCD_LINE_OPTS}

LINE_OPTS={kCockDBLabel: CockDB_LINE_OPTS, kTiDBLabel: TiDB_LINE_OPTS, kFabricLabel: FAB_LINE_OPTS, 
           kQuorumLabel: QUO_LINE_OPTS, kEtcdLabel: ETCD_LINE_OPTS}


# DB_BAR_OPTS = {"label": kCockDBLabel, "color": kDbColor, "hatch": "+++", "edgecolor": 'y'}
# TiDB_BAR_OPTS = {"label": kTiDBLabel, "color": kTiDBColor, "hatch": "***", "edgecolor":'y'}
# FAB_BAR_OPTS = {"label": kFabricLabel, "color": kFabricColor, "hatch": "///", "edgecolor":'y'}
# QUORUM_BAR_OPTS = {"label": kQuorumLabel, "color": kQuorumColor, "hatch": "xxx", "edgecolor":'y',}




# TXN_BUFFER_OPTS = {"label": "txn buffer", "color": "grey", "hatch": "xxx", "edgecolor": 'y'}
# PROPOSAL_OPTS = {"label": "proposal", "color": "g", "hatch": "///", "edgecolor": 'y'}
# CONSENSUS_OPTS = {"label": "consensus", "color": "c", "hatch": "ooo", "edgecolor": 'y'}
# VALIDATION_OPTS = {"label": "blk validation", "color": "orange", "edgecolor": 'y'}


# BLK_BUFFER_OPTS = {"label": "blk buffer", "color": "r", "hatch": "xxx", "edgecolor": 'y'}
# BLK_VERIFICATION_OPTS = {"label": "blk verification", "color": "g", "hatch": "///", "edgecolor": 'y'}
# TXN_VERIFICATION_OPTS = {"label": "txn verification", "color": "c", "hatch": "ooo", "edgecolor": 'y'}
# STATE_PERSISTANCE_OPTS = {"label": "state persistence", "color": "orange", "hatch": "+++", "edgecolor": 'y'}
# BLK_PERSISTANCE_OPTS = {"label": "blk persistence", "color": "m"}

# PRE_OPTS = {"label": "pre-execution", "color": "r", "hatch": "xxx", "edgecolor": 'y'}
# EXECUTION_OPTS = {"label": "execution", "color": "orange", "hatch": "///", "edgecolor": 'y'}
# POST_OPTS = {"label": "post-execution", "color": "c", "edgecolor": 'y'}



def sum_list(a,b):
    c = []
    for i, v in enumerate(a):
        c.append(a[i] + b[i])
    return c


def idx(l, v):
    for i, vv in enumerate(l):
        if v < vv:
            return i
    return len(l)


def bar_offset(bar_count, bar_idx, gap=1, width=0, hole_width=0):
    if hole_width == 0:
        if width != 0:
            rest = gap - bar_count * width
            num_hole = bar_count + 1
            hole_width = float(rest) / num_hole
        else:
            num_hole = bar_count * 2 + bar_count + 1
            hole_width = float(gap) / num_hole
            width = 2 * hole_width

    unit_length = width + hole_width
    if bar_count % 2 == 0:
        half = bar_count / 2
        # if bar_idx < half:
        #     unit =  0.5 - (half - bar_idx)
        # else:
        unit = 0.5 + (bar_idx - half)
        # print unit
        return unit * unit_length
    else:
        center = (bar_count - 1) / 2
        return (bar_idx - center) * unit_length



import matplotlib as mpl
mpl.rcParams['legend.fontsize'] = 24
mpl.rcParams['axes.titlesize'] = 30
mpl.rcParams['axes.titleweight'] = "bold"
mpl.rcParams['axes.labelsize']=24
mpl.rcParams['font.size'] = 14
