'''
旅行商问题和集合覆盖问题有一些共同之处：

你需要计算所有的解，并从中选出最小/最短的那个。这两个问题都属与NP完全问题。

#### 如何识别NP完全问题

* 元素较少时算法的运行速度非常快，但随着元素数量的增加，速度会变得非常慢。
* 涉及“所有组合”的问题通常是NP完全问题。
* 不能将问题分成小问题，必须考虑各种可能的情况。这可能是NP完全问题。
* 如果问题涉及序列（如旅行商问题中的城市序列）且难以解决，它就可能就是NP完全问题。
* 如果问题涉及集合（如广播台集合）且难以解决，它就可能是NP完全问题。
* 如果问题可转换成集合覆盖问题或旅行商问题，那它肯定是NP完全问题。

#### 小结
* 贪婪算法寻找局部最优解，企图以这种方式获得全局最优解。
* 对于NP完全问题，还没有找到快速解决方法。
* 面临NP完全问题时，最佳做法是使用近似算法。
* 贪婪算法易于实现、运行速度快，是不错的近似算法。
'''


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