kMarkerSize=14
kLineWidth=1
kLineStyle="-"
kFabricPlusColor, kFabricSharpColor, kFabricColor, kFabricSharpLiteColor= "green", "red", 'blue', 'orange'
kFabricPlusMarker, kFabricSharpMarker, kFabricMarker, kFabricSharpLiteMarker = "x", "X", 'v', 's'
kFabricPlusLabel, kFabricSharpLabel, kFabricLabel, kFabricSharpLiteLabel = "FabricPlus", "FabricSharp", "Fabric", "FabricSharpLite"
base_colors = {kFabricPlusLabel: kFabricPlusColor, kFabricSharpLabel: kFabricSharpColor, kFabricLabel: kFabricColor, kFabricSharpLiteLabel:kFabricSharpLiteColor}
base_hatches = {kFabricPlusLabel: "xxx", kFabricSharpLabel: "ooo", kFabricLabel: "///", kFabricSharpLiteLabel: "\\\\\\"}


FabricPlus_FMT=kFabricPlusMarker
FabricPlus_LINE_OPTS={"linestyle": kLineStyle, "linewidth":kLineWidth, "markersize":kMarkerSize, 'markerfacecolor':kFabricPlusColor, "color":kFabricPlusColor, "label": kFabricPlusLabel}

FabricSharp_FMT=kFabricSharpMarker
FabricSharp_LINE_OPTS={"linestyle": kLineStyle, "linewidth":kLineWidth, "markersize":kMarkerSize, 'markerfacecolor':kFabricSharpColor, "color":kFabricSharpColor, "label": kFabricSharpLabel}

Fabric_FMT=kFabricMarker
Fabric_LINE_OPTS={"linestyle": kLineStyle, "linewidth":kLineWidth, "markersize":kMarkerSize, 'markerfacecolor':kFabricColor, "color":kFabricColor, "label": kFabricLabel}

FabricSharpLite_FMT=kFabricSharpLiteMarker
FabricSharpLite_LINE_OPTS={"linestyle": kLineStyle, "linewidth":kLineWidth, "markersize":kMarkerSize, 'markerfacecolor':kFabricSharpLiteColor, "color":kFabricSharpLiteColor, "label": kFabricSharpLiteLabel}

FMTS={kFabricPlusLabel: FabricPlus_FMT, kFabricSharpLabel: FabricSharp_FMT, kFabricLabel: Fabric_FMT, kFabricSharpLiteLabel: FabricSharpLite_FMT}

LINE_OPTS={kFabricPlusLabel: FabricPlus_LINE_OPTS, kFabricSharpLabel: FabricSharp_LINE_OPTS, kFabricLabel: Fabric_LINE_OPTS, kFabricSharpLiteLabel: FabricSharpLite_LINE_OPTS}

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


def sum_list(a,b):
    c = []
    for i, v in enumerate(a):
        c.append(a[i] + b[i])
    return c

'''
Compute a bar's width and offsets given the number of series. 
offsets is an array with series_count elements. 
The consecutive difference is the bar width and the median is 0.
'''
def compute_width_offsets(series_count):
    width = 1.0 / (series_count + 1)
    start_offset = 0 - width * (float(series_count) / 2 - .5)
    offsets = [start_offset + width * i for i in range(series_count)]
    return width, offsets



import matplotlib as mpl
mpl.rcParams['legend.fontsize'] = 16
mpl.rcParams["legend.labelspacing"] = 0.4
mpl.rcParams["legend.columnspacing"] = 0.4
mpl.rcParams["legend.handletextpad"] = 0.4

mpl.rcParams['axes.titlesize'] = 30
mpl.rcParams['axes.titleweight'] = "bold"
mpl.rcParams['axes.labelsize']=20
mpl.rcParams['font.size'] = 14

mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42

# export chart=ycsb; python chart/provenance/script/${chart}.py chart/provenance/${chart}.pdf && xdg-open chart/provenance/${chart}.pdf