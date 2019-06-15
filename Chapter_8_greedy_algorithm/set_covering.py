# 需要覆盖的州
states_nedded = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
# 广播台清单使用字典表示
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])
# 最终选择的广播台
fianl_stations = set()
while states_nedded:
    best_station = None
    states_coverd = set()
    for station, states_for_station in stations.items():
        covered = states_nedded & states_for_station
        if len(covered) > len(states_coverd):
            best_station = station
            states_coverd = covered
    states_nedded -= states_coverd
    fianl_stations.add(best_station)
print(fianl_stations)