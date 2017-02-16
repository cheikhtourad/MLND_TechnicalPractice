# Question 3
# Given an undirected graph G, find the minimum spanning tree within G. 
# A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges.
# Your function should take in and return an adjacency list structured like this:

#{'A': [('B', 2)],
# 'B': [('A', 2), ('C', 5)], 
# 'C': [('B', 5)]}
#Vertices are represented as unique strings. The function definition should be question3(G)

# This question is answered by finding the minimum spanning tree of the graph.
# To do this, Prim's algorithm will be used.
import math


class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.seen = False

    def insert_node(self, val):
        new_node = Node(val)
        self.nodes.append(new_node)
        return new_node

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        "Insert a new edge, creating new nodes if necessary"
        nodes = {node_from_val: None, node_to_val: None}
        for node in self.nodes:
            if node.value in nodes:
                nodes[node.value] = node
                if all(nodes.values()):
                    break
        for node_val in nodes:
            nodes[node_val] = nodes[node_val] or self.insert_node(node_val)
        node_from = nodes[node_from_val]
        node_to = nodes[node_to_val]
        new_edge = Edge(new_edge_val, node_from, node_to)
        node_from.edges.append(new_edge)
        node_to.edges.append(new_edge)
        self.edges.append(new_edge)

    def _clear_visited(self):
        for node in self.nodes:
            node.visited = False

test1 = {'A': [('B', 2)],
         'B': [('A', 2), ('C', 5)], 
         'C': [('B', 5)]}

def question3(G):
    if not G:
        return {}
    # Take the input adjacency list and parse it to a graph
    graph = to_graph(G)
    return find_MST(graph)

def bfs(self, start_node_num):
        """An iterative implementation of Breadth First Search
        iterating through a node's edges. The output should be a list of
        numbers corresponding to the traversed nodes.
        ARGUMENTS: start_node_num is the node number (integer)
        MODIFIES: the value of the visited property of nodes in self.nodes
        RETURN: a list of the node values (integers)."""
        node = self.find_node(start_node_num)
        self._clear_visited()
        ret_list = []
        # Your code here
        queue = [node]
        node.visited = True
        def enqueue(n, q=queue):
            n.visited = True
            q.append(n)
        def unvisited_outgoing_edge(n, e):
            return ((e.node_from.value == n.value) and
                    (not e.node_to.visited))
        while queue:
            node = queue.pop(0)
            ret_list.append(node.value)
            for e in node.edges:
                if unvisited_outgoing_edge(node, e):
                    enqueue(e.node_to)
        return ret_list

# This function takes a graph and returns the Minimum Spaning Tree (MST) of that graph, also in the form of a graph
def find_MST(G):
    mst = Graph()

    node = G.nodes[1]
    G._clear_visited()
    queue = []
    def enqueue(n, q=queue):
            n.visited = True
            q.append(n)
    def unvisited_outgoing_edge(n, e):
            return ((e.node_from.value == n.value) and
                    (not e.node_to.visited))

    
    enqueue(node, queue)
    visited = [node.value]
    while queue:
        node = queue[-1]
        print 'Node', node.value
        possible_edges = [x for x in node.edges if not x.node_to.visited]
        # if there are no possible edges from the current node, pop it from the stack
        min_edge = None
        if not possible_edges:
            queue.pop()
            pass
        else:
            min_edge = min(possible_edges, key=lambda x: x.value )

        if min_edge:
            mst.insert_edge(min_edge.value, min_edge.node_from.value, min_edge.node_to.value)
            node = min_edge.node_to
            enqueue(node, queue)
            print 'Enqueue'
            print node.value
        #print min_edge.value

    return mst


def find_MST_helper(G):
    pass

# This function takes an adjacency list and returns a graph
def to_graph(G):
    graph = Graph()

    for entry in G:
        node = Node(entry)

        # Insert edges associated with the node created
        for edge in G[node.value]:
            graph.insert_edge(edge[1], node.value, edge[0])
    return graph



print question3(test1)
