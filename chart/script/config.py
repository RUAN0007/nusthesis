kMarkerSize=14
kLineWidth=1
kLineStyle="-"

# These below labels must be consistent with the tex.
original_scheduler_label = "O"
fabricplus_scheduler_label = "P"
occ_standard_scheduler_label = "S"
occ_latest_scheduler_label = "L"
fg_scheduler_label = "F"

txn_scheduler_labels = [original_scheduler_label, fabricplus_scheduler_label, occ_standard_scheduler_label, occ_latest_scheduler_label, fg_scheduler_label]

original_label = "Original"
ldb_prov_label = "Prov"
forkbase_label = "Sharp"

storage_types = [original_label,ldb_prov_label, forkbase_label]

# Use the markder to differentiate the Txn scheduler
raw_markers = {original_scheduler_label: "v", 
              fabricplus_scheduler_label: "X", 
              occ_standard_scheduler_label: "s", 
              occ_latest_scheduler_label: "x", 
              fg_scheduler_label: "o"} 

# Use the color to differentiate the storage
raw_colors = {original_label: "green", ldb_prov_label: "blue", forkbase_label: "red"} 
forkbase_scheduler_colors = {original_scheduler_label: raw_colors[forkbase_label], 
                             fabricplus_scheduler_label: "orange",
                             occ_standard_scheduler_label: "skyblue", 
                             occ_latest_scheduler_label: "c",
                             fg_scheduler_label: "purple"}

def make_label_by_storage(storage):
    if storage == original_label:
        return "Fabric"
    if storage == forkbase_label:
        return "Fabric#"
    else:
        return "FabricProv"


'''
We expect the constructed label match with the series name in data files. 
'''
def make_label(storage, scheduler_label=original_scheduler_label):
    if storage == original_label:
        storage_label = ""
        return "Fabric"

    if storage == forkbase_label:
        storage_label = "#"
    else:
        storage_label = storage
    return "Fabric{}-{}".format(storage_label, scheduler_label) 

labels = {}
colors = {}
line_opts = {}
fmts = {}


for storage in storage_types:
    for scheduler_label in txn_scheduler_labels:
        label =  make_label(storage, scheduler_label)
        if storage == forkbase_label:
            color = forkbase_scheduler_colors[scheduler_label]
        else:
            color = raw_colors[storage]

        labels[label] = label
        colors[label] = color
        fmts[label] = raw_markers[scheduler_label]
        line_opts[label] = {"linestyle": kLineStyle, "linewidth":kLineWidth, "markersize":kMarkerSize, 'markerfacecolor':color, "color":color, "label": label}


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