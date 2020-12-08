kMarkerSize=14
kLineWidth=1
kLineStyle="-"
kFabricProvOColor, kFabricSharpOColor, kFabricColor, kFabricSharpOLiteColor= "green", "red", 'blue', 'orange'
kFabricProvOMarker, kFabricSharpOMarker, kFabricMarker, kFabricSharpOLiteMarker = "x", "X", 'v', 's'
kFabricProvOLabel, kFabricSharpOLabel, kFabricLabel, kFabricSharpOLiteLabel = "FabricProv-O", "Fabric#-O", "Fabric", "Fabric#-Lite"
base_colors = {kFabricProvOLabel: kFabricProvOColor, kFabricSharpOLabel: kFabricSharpOColor, kFabricLabel: kFabricColor, kFabricSharpOLiteLabel:kFabricSharpOLiteColor}
base_hatches = {kFabricProvOLabel: "xxx", kFabricSharpOLabel: "ooo", kFabricLabel: "///", kFabricSharpOLiteLabel: "\\\\\\"}


FabricProvO_FMT=kFabricProvOMarker
FabricProvO_LINE_OPTS={"linestyle": kLineStyle, "linewidth":kLineWidth, "markersize":kMarkerSize, 'markerfacecolor':kFabricProvOColor, "color":kFabricProvOColor, "label": kFabricProvOLabel}

FabricSharpO_FMT=kFabricSharpOMarker
FabricSharpO_LINE_OPTS={"linestyle": kLineStyle, "linewidth":kLineWidth, "markersize":kMarkerSize, 'markerfacecolor':kFabricSharpOColor, "color":kFabricSharpOColor, "label": kFabricSharpOLabel}

Fabric_FMT=kFabricMarker
Fabric_LINE_OPTS={"linestyle": kLineStyle, "linewidth":kLineWidth, "markersize":kMarkerSize, 'markerfacecolor':kFabricColor, "color":kFabricColor, "label": kFabricLabel}

FabricSharpOLite_FMT=kFabricSharpOLiteMarker
FabricSharpOLite_LINE_OPTS={"linestyle": kLineStyle, "linewidth":kLineWidth, "markersize":kMarkerSize, 'markerfacecolor':kFabricSharpOLiteColor, "color":kFabricSharpOLiteColor, "label": "Fabric#-O(No DASL)"}

FMTS={kFabricProvOLabel: FabricProvO_FMT, kFabricSharpOLabel: FabricSharpO_FMT, kFabricLabel: Fabric_FMT, kFabricSharpOLiteLabel: FabricSharpOLite_FMT}

LINE_OPTS={kFabricProvOLabel: FabricProvO_LINE_OPTS, kFabricSharpOLabel: FabricSharpO_LINE_OPTS, kFabricLabel: Fabric_LINE_OPTS, kFabricSharpOLiteLabel: FabricSharpOLite_LINE_OPTS}

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
mpl.rcParams['font.size'] = 18

mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42

# export chapter=provenance; export chart=forward; python chart/script/${chapter}_${chart}.py chart/${chapter}/${chart}.pdf && xdg-open chart/${chapter}/${chart}.pdf