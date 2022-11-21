from collections import defaultdict
from collections import deque
import sys

class Node:
    def __init__(self, id, name, dur, es, ef, ls, lf) -> None:
        self.id = id
        self.name = name
        self.dur = dur
        self.es = es
        self.ef = ef
        self.ls = ls
        self.lf = lf
        
nodes = {}
visited = {}
criticalpath = []
forwardPass = defaultdict(list)
backwardPass = defaultdict(list)
leaves = {}
totaldur = 0
q = deque()
sec = deque()

path = './input3.txt'

for lines in open(path):
    line = lines.rstrip('\n').split(',')
    id = int(line[0]); name = line[1]
    dur = int(line[2])
    ef = 0
    if len(line) == 4:
        pred = line[3].split(';')
        for x in pred:
            x = int(x)
            forwardPass[x].append(id)
            backwardPass[id].append(x)
    else:
        q.append(id)
        ef = dur
    nodes[id] = Node(id, name, dur, 0, ef, 0, sys.maxsize)
    visited[id] = 0
    leaves[id] = 0
while q:
    outdegree = 0
    u = q.popleft()
    ef = nodes[u].ef
    for v in forwardPass[u]:
        nodes[v].es = max(nodes[v].es, ef)
        nodes[v].ef = nodes[v].es + nodes[v].dur
        if visited != 1:
            q.append(v)
            outdegree += 1
    if outdegree == 0 and visited[u] == 0:
        leaves[u] = 1;
        totaldur = max(totaldur, nodes[u].ef)
    visited[u] = 1

for key, val in leaves.items():
    if val:
        nodes[key].lf = totaldur
        nodes[key].ls = nodes[key].lf - nodes[key].dur
        q.append(key)
        sec.append(v)
        visited[key] = 0 

while q:
    u = q.popleft()
    ls = nodes[u].ls
    for v in backwardPass[u]:
        nodes[v].lf = min(nodes[v].lf, ls)
        nodes[v].ls = nodes[v].lf - nodes[v].dur
        if visited != 1:
            q.append(v)
    visited[u] = 1

while sec:
    u = sec.popleft()
    visited[u] = 0
    if nodes[u].es == nodes[u].ls and visited[u] == 0:
        criticalpath.append(nodes[u].name)
        for v in backwardPass[u]:
            if visited[v] == 1:
                sec.append(v)
                visited[v] = 0

def printNode(nodes):
    for key, value in nodes.items():
        print('id = {},node = {},duration = {},ES = {},EF = {},LS = {},LF = {}'
            .format(key, value.name, value.dur, value.es, value.ef, value.ls, value.lf))

printNode(nodes)

print (list(reversed(criticalpath)))