class Node(object):
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def __repr__(self):
        return str(self.value)

def bfs(start, stop):
    print "BFS: Searching for a path between %s and %s" % (start, stop)
    queue = [start]
    visited = []
    while queue:
        current = dequeue_from(queue)
        ## necessary?
        if current in visited:
            break
        print " -- Examining %s" % current
        if current == stop:
            print "Found it!"
            return True
        visited.append(current)
        unvisited_neighbors = [n for n in current.neighbors if n not in visited]
        for n in unvisited_neighbors:
            enqueue(queue, n)

    print "No path found :("
    return False

def bfs_with_path(start, stop):
    print "BFS with path: Searching for a path between %s and %s" % (start, stop)
    queue = [start]
    visited = []
    paths = [[]]
    while queue:
        current = dequeue_from(queue)
        current_path = dequeue_from(paths)

        ## necessary?
        if current in visited:
            break

        current_path.append(current)

        print " -- Examining %s" % current

        if current == stop:
            print "Found it! Path: %s" % str(current_path)
            return True

        visited.append(current)
        enqueue(paths, current_path)
        unvisited_neighbors = [n for n in current.neighbors if n not in visited]
        for n in unvisited_neighbors:
            enqueue(queue, n)

    print "No path found :("
    return False

def dequeue_from(lst):
    item = lst.pop(0)
    return item

def enqueue(lst, item):
    lst.append(item)

def dfs_with_path(start, stop):
    print "DFS: Searching for a path between %s and %s" % (start, stop)
    stack = [start]
    visited = []
    paths = [[]]
    while stack:
        current = pop_from(stack)
        current_path = pop_from(paths)
        if current in visited:
            break

        print " -- Examining %s" % current
        current_path.append(current)

        if current == stop:
            print "Found it! Path: %s" % str(current_path)
            return True

        visited.append(current)
        paths.append(current_path)

        unvisited_neighbors = [n for n in current.neighbors if n not in visited]
        for n in unvisited_neighbors:
            push(stack, n)

    print "No path found :("
    return False

def pop_from(lst):
    item = lst.pop(0)
    return item

def push(lst, item):
    lst.insert(0, item)

if __name__ == "__main__":
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")
    F = Node("F")
    G = Node("G")
    A.neighbors.extend([B, E, G])
    B.neighbors.append(A)
    C.neighbors.append(F)
    D.neighbors.extend([G, F])
    E.neighbors.extend([A, F])
    F.neighbors.extend([C, D, E])
    G.neighbors.append(D)

    H = Node("H")
    J = Node("J")
    H.neighbors.append(J)
    J.neighbors.append(H)

    bfs(A, C)
    bfs_with_path(A, C)

    bfs(A, H)

    B.neighbors.append(E)
    E.neighbors.append(B)

    dfs_with_path(A, B)
    bfs_with_path(A, B)

    dfs_with_path(A, H)
