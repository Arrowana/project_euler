from copy import deepcopy

pyr=[[2],[4,5],[1,3,5]]
a=[[(0,0),10],[(2,3),20],[(4,4),30]]

queue=[[[(0,0)], [(1,0), (1,1)]]]

def path_cost(path):
    return sum(pyr[node[0]][node[1]] for node in path[0])

while True:
    print "queue:", queue
    candidate=max(queue, key=path_cost)
    print "candidate:", candidate
    node = candidate[0][-1]

    if candidate[1]:
        next_node=max(candidate[1], key=lambda x: pyr[x[0]][x[1]])
        print "next_node:", next_node
        new_path = [candidate[0]+[next_node], [(next_node[0]+1, next_node[1]+i) for i in range(2)]]
        candidate[1].remove(next_node)
        print new_path
        queue.append(new_path)
    else:
        print "no more new combinations, delete from queue"

print max(a, key=lambda x: x[1])
