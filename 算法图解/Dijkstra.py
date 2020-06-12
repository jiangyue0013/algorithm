'''
Dijkstra 算法的步骤：
1. 找出最便宜的节点，即可在最短时间内前往节点的节点
2. 对于该节点的邻居，，检查是否有前往他们的更短路径，如果有就更新其开销。
3. 重复这个过程，直到对图中的每个节点都这样做了。
4. 计算最终路径


计算非加权图中的最短路径，可使用广度优先搜索。

要计算加权图中的最短路径，可使用 Dijkstra 算法。

在无向图中，每条边都是一个环。Dijkstra 算法只适用于有向无环图（directed acyclic graph,DAG)。

有负权边不能使用 Dijkstra 算法。需要使用 Bellman-Ford 算法
'''


graph = {}
graph['start'] = {}
graph['start']['a'] = 10
graph['a'] = {}
graph['a']['c'] = 20
graph['b'] = {}
graph['b']['a'] = 1
graph['c'] = {}
graph['c']['b'] = 1
graph['c']['fin'] = 30
graph['fin'] = {}

infinity = float('inf')

costs = {}
costs['a'] = 10
costs['b'] = infinity
costs['c'] = infinity
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = None
parents['c'] = None
parents['fin'] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(costs)
print(parents)


