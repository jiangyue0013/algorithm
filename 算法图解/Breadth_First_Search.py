'''
广度优先搜索（ BFS:breadth first search )的运行时间为O(V+E)，其中 V 为顶点（ vertice )数, E 为边数。
如果任务 A 依赖于任务 B，在列表中任务 A 就必须在任务 B 后面。这被称为拓扑排序，使用它可根据图创建一个有序列表。
树是一中特殊的图，其中没有往后指的边。
####小结
* 广度优先搜索指出是否有从A到B的路径。
* 如果有，广度优先搜索将找出最短入境。
* 面临类似于寻找最短路径问题时，可尝试使用图来建立模型，再使用广度优先搜索来解决问题。
* 有向图中的边为箭头，箭头的方向指定了关系的方向。
* 无向图中的边不带箭头，其中的关系是双向的。
* 队列是先进先出（FIFO）的。
* 栈是后进先出的（LIFO）的。
* 你需要按加入顺序检查被搜索列表中的人，否则找到的就不是最短路径，因此搜索列表必须是队列。
* 对于检查过的人，务必不要再去检查，否则可能导致无限循环。

'''


from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person, 'is a mango seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['jonny', 'thom']
graph['anuj'] = []
graph['peggy'] = []
graph['jonny'] = []
graph['thom'] = []

search('you')