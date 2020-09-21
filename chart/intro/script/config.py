

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

# export chart=smallbank; python chart/intro/script/${chart}.py chart/intro/${chart}.pdf && xdg-open chart/intro/${chart}.pdf