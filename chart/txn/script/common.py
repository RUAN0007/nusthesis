import os

kOriginalLabel, kFppLabel, kFoccStandardLabel, kFoccLatestLabel, kFsharpLabel = "Fabric", "Fabric++", "Focc-s", "Focc-l", "Fabric#"

kMarkerSize=14
kLineWidth=1
kLineStyle="-"
kOriginalColor, kFppColor, kFoccStandardColor, kFoccLatestColor, kFsharpColor = "r", "orange", 'g', 'skyblue', 'purple'
kOriginalMarker, kFppMarker, kFoccStandardMarker, kFoccLatestMarker, kFsharpMarker = "D", "X", 'v', 's', 'o'

base_colors = {kOriginalLabel: kOriginalColor, kFppLabel: kFppColor, kFoccStandardLabel: kFoccStandardColor, kFoccLatestLabel:kFoccLatestColor, kFsharpLabel: kFsharpColor}

# base_hatches = {kOriginalLabel: "xxx", kFppLabel: "xxx", kFoccStandardLabel: "ooo", kFoccLatestLabel: "ooo", kFsharpLabel: "///"}
base_hatches = {kOriginalLabel: "", kFppLabel: "", kFoccStandardLabel: "", kFoccLatestLabel: "", kFsharpLabel: ""}

kMarkerEdgeWidth=1
kMarkerEdgeColor='black'

Original_FMT=kOriginalColor+kOriginalMarker
Original_LINE_OPTS={"linestyle": kLineStyle, "linewidth":kLineWidth, "markersize":kMarkerSize, 'markerfacecolor':kOriginalColor, "color":kOriginalColor, "markeredgewidth": kMarkerEdgeWidth,  "markeredgecolor":kMarkerEdgeColor}

Fpp_FMT=kFppMarker
Fpp_LINE_OPTS={"linestyle": kLineStyle, "linewidth":kLineWidth, "markersize":kMarkerSize, 'markerfacecolor':kFppColor, "color":kFppColor, "markeredgewidth": kMarkerEdgeWidth,  "markeredgecolor":kMarkerEdgeColor}

FoccStandard_FMT=kFoccStandardMarker
FoccStandard_LINE_OPTS={"linestyle": kLineStyle, "linewidth":kLineWidth, "markersize":kMarkerSize, 'markerfacecolor':kFoccStandardColor, "color":kFoccStandardColor,"markeredgewidth": kMarkerEdgeWidth,  "markeredgecolor":kMarkerEdgeColor}

FoccLatest_FMT=kFoccLatestMarker
FoccLatest_LINE_OPTS={"linestyle": kLineStyle, "linewidth":kLineWidth, "markersize":kMarkerSize, 'markerfacecolor':kFoccLatestColor, "color":kFoccLatestColor,"markeredgewidth": kMarkerEdgeWidth,  "markeredgecolor":kMarkerEdgeColor}

Fsharp_FMT=kFsharpMarker
Fsharp_LINE_OPTS={"linestyle": kLineStyle, "linewidth":kLineWidth, "markersize":kMarkerSize, 'markerfacecolor':kFsharpColor, "color":kFsharpColor,"markeredgewidth": kMarkerEdgeWidth,  "markeredgecolor":kMarkerEdgeColor}

FMT={kOriginalLabel: Original_FMT, kFppLabel: Fpp_FMT, kFoccStandardLabel: FoccStandard_FMT, kFoccLatestLabel: FoccLatest_FMT, kFsharpLabel: Fsharp_FMT,}

LINE_OPTS={kOriginalLabel: Original_LINE_OPTS, kFppLabel: Fpp_LINE_OPTS, kFoccStandardLabel: FoccStandard_LINE_OPTS, 
           kFoccLatestLabel: FoccLatest_LINE_OPTS, kFsharpLabel: Fsharp_LINE_OPTS}


def fmt(label):
    return FMT[label]


def line_fmt(label):
    return LINE_OPTS[label]


def bar_format(label):
    return {"color":base_colors[label], 
            "edgecolor":'black', 
            "hatch":base_hatches[label], 
            }

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

# A Handy method parse the first column as x axis, the remaining columns as series \t delimited
# The first row denotes for series name

def parse(statPath, is_numeric_x=False):
    series = {}
    x_axis = []
    f = open(statPath,'r')
    lines = f.readlines()
    series_names = []
    lines[0] = lines[0].strip()
    for i, series_name in enumerate(lines[0].split("\t")):
        if i == 0:
            continue # Ignore the first column
        series_name = series_name.strip()
        series_names.append(series_name)
        series[series_name] = []
    
    for line in lines[1:]:
        line = line.strip()
        splits = line.split("\t")
        if is_numeric_x:
            x_axis.append(float(splits[0]))
        else:
            x_axis.append(splits[0].strip())

        for i, series_name in enumerate(series_names):
            series[series_name].append(float(splits[i+1]))

    return x_axis, series_names, series

import matplotlib as mpl
mpl.rcParams['legend.fontsize'] = 19
mpl.rcParams["legend.labelspacing"] = 0
mpl.rcParams["legend.columnspacing"] = 0.4
mpl.rcParams["legend.handletextpad"] = 0

mpl.rcParams['axes.titlesize'] = 30
mpl.rcParams['axes.titleweight'] = "bold"
mpl.rcParams['axes.labelsize']=24
mpl.rcParams['font.size'] = 14

mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42

if  __name__ == "__main__":
    # print bar_format(kFoccLatestLabel)
    a, b, c = parse("data/hot_ratio_thruput")
    print a
    print b
    print c
    
# export chart=blksize_abort; python chart/txn/script/${chart}.py chart/txn/${chart}.pdf && xdg-open chart/txn/${chart}.pdf