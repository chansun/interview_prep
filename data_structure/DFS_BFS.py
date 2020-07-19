# Pseudo Code

def DFS(node):
    if node == None:
        return 0
    visit(node)
    node.visited = True
    for i in node.adjacent:
        if not i.visited:
            DFS(i)

# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
# Space Complexity: O(M), where M is the number of edges of the longest branch.


def BFS(node):
    if node == None:
        return 0
    queue = Queue()
    visit(node)
    node.visited = True
    queue.enqueue(node)
    while not queue.isEmpty():
        temp = queue.dequeue()
        visit(temp)
        for i in temp.adjacent:
            if not i.visited:
                temp.visited = True
                queue.enqueue(i)

# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
# Space Complexity: O(M), where M is the maximum number of edges from one vertex.

