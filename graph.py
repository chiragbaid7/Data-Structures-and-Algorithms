from collections import defaultdict, deque

class Graph:

    def __init__(self,nodes):
        #this will create empty list as a value for a non existent key
        self.list=defaultdict(list)
        self.nodes=nodes

    def AddEdge(self,x,y):
        self.list[x].append(y)
        self.list[y].append(x)

    def printGraph(self):
        for key in self.list:
            neigh=self.list[key]

    def BFS(self,src):
        queue=deque()
        #a node can be visited twice so to avoid maintain a visited array
        visited=[False]*self.nodes
        queue.append(src)
        while(queue):
            key =queue.popleft()
            visited[src]=True
            for neigh in self.list[key]:
                if(not visited[neigh]):
                    visited[neigh]=True
                    queue.append(neigh)

    def __util_DFS(self,node,visited):
        visited[node] = True
        for neighbour in self.graph[node]:
            if(not visited[neighbour]):
                self.__util_DFS(neighbour)
        
    def DFS(self,src):
        visited=[False]*self.nodes
        self.__util_DFS(src,visited)


    def DFSIteration(self,src, visited):
        stack = []
        stack.append(src)
        visited.add(src)
        visited[src] = True
        while(stack):
            parent = stack.pop()
            # print(parent)
            #Append all neighbours frames to the stack - LIFO
            # Everytime top vertices path will be explored
            for neighbour in self.list[parent]:
                if(not visited[neighbour]):
                    visited[neighbour] = True
                    stack.append(neighbour)

    def undirected_graph_cycle_BFS(self,src):
        queue=deque()
        visited=[False]*self.nodes 
        parent=[-1]*self.nodes 
        parent[src]=src 
        visited[src]=True
        queue.append(src)

        while(queue):
            node=queue.popleft()
            for neigh in self.list[node]:
                if(visited[neigh] and parent[node]==neigh):
                    continue
                if(visited[neigh] and node!=parent[neigh]):
                    return True 
                else:
                    visited[neigh]=True 
                    parent[neigh]=node 
                    queue.append(neigh)
        return False 
        
    def checkCyclePresenceInUndirectedGraph(self, visited, node, parentNode):
        #Condition to check cycle presence 
        if(visited[src]):
            return True
        visited[src] = True
        for neighbour in self.list[node]:
            if(neighbour == parent):
                continue
            elif(self.checkCyclePresenceInUndirectedGraph(visited, neighbour, node):
                return True
        return False

    def undirected_graph_cycle_DFS(self,src):
        visited=[False]*self.nodes 
        """
            dfs traversal you traverse along the current path till reach the dead end
            and backtrack and traverse from that node.Reapeat this untill all the nodes are 
            visited.
        """
        return self.checkCyclePresenceInUndirectedGraph(visited,src,src)

    #Count no of subgraphs
    def noOfConnectedComponents(self):
        countConnectedComponent = 0
        visited = [False] * self.nodes
        for node in self.list:
            if(not visited[node]):
                countConnectedComponent+=1
                self.DFSIteration(node,visited)
        return countConnectedComponent

    def dfsLargestComponent(self, count, visited, node):
        visited.add(node)
        count+=1
        #No of components
        for neighbour in self.list[node]:
            #Bi-directional graph edges will lead to stack exceeded error
            if(neighbour not in visited):
                count=self.dfsLargestComponent(count, visited, neighbour)
        return count

    def largestComponent(self):
        maxCount = 0
        visited = set()
        for node in self.list:
            if (node not in visited):
                count = self.dfsLargestComponent(1, visited, node)
                maxCount = max(count, maxCount)

        return maxCount

    def shortestPath(self, src, destination):
        # Perform BFS - uniform traversal
        # Queue - [node, distance]
        queue = deque()
        a = set()
        queue.append([src, 0])
        visited = [False]* self.nodes
        while(queue):
            parent, distance = queue.popleft()
            visited[parent] = True
            # a.add(parent)
            if(parent == destination):
                return distance
            for neighbour in self.list[parent]:
                #neighbour not in a
                if(not visited[neighbour]):
                    # parent -> neighbour
                    # distance[neighbour] = distance[parent] + 1
                    queue.append([neighbour], [distance + 1])
        return -1
    def interval
def main():
    g=Graph(7)
    g.AddEdge(1,0)
    g.AddEdge(5,0)
    g.AddEdge(5,8)
    g.AddEdge(2,4)
    g.AddEdge(3,2)
    g.AddEdge(4,3)
    # print("TOTAL COUNT",g.noOfConnectedComponents())
    print(g.largestComponent())
    #g.BFS(2)
    #g.DFS(1)
    # print(g.undirected_graph_cycle_BFS(1))
    # print(g.undirected_graph_cycle_DFS(1))
if __name__=="__main__":
    main()
