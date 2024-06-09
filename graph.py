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
            print(key,neigh)

    def DFS(self):
        # BFS in a graph
        queue = deque()
        visited = [False] * self.nodes
        queue.append(src)
        while(queue):
            vertex = queue.popleft()
            for neighbour in self.list[vertex]:
                #Push only when that vertex is not visited
                if(not vertex[neighbour]):
                    visited[neighbour] = True
                    queue.append(neighbour)
        

    def BFS(self,src):
        queue=deque()
        #a node can be visited twice so to avoid maintain a visited array
        visited=[False]*self.nodes
        visited[src]=True 
        queue.append(src)
        while(queue):
            key =queue.popleft()
            print(key)
            for neigh in self.list[key]:
                if(not visited[neigh]):
                    visited[neigh]=True
                    queue.append(neigh)
    def DFSIteration(self):
        stack = []
        visited = [False] * self.nodes
        stack.append(src):
        while(stack):
            parent = stack.pop()
            #Print
            print(parent)
            for neighbour in self.list[parent]:
                if(not visisted[neigbour]):
                    visisted[neigbour] = True
                    stack.append(neighbour)
            
    def __util_DFS(self,src,visited):
        visited[src]=True 
        print(src)
        for neigh in self.list[src]:
            if(not visited[neigh]):
                self.__util_DFS(neigh,visited)
        return
        
    def DFS(self,src):
        visited=[False]*self.nodes 
        self.__util_DFS(src,visited)

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
        
    def __cycle_dfs(self,visited,src,parent):
        if(visited[src] and parent!=src):
            return True
        visited[src]=True 
        for child in self.list[src]:
            if(child==parent): #if the node is the parent of src then continue and traverse from the other end 
                continue 
            elif(self.__cycle_dfs(visited,child,src)):
                return True 
        return False 


    def undirected_graph_cycle_DFS(self,src):
        visited=[False]*self.nodes 
        """
            dfs traversal you traverse along the current path till reach the dead end
            and backtrack and traverse from that node.Reapeat this untill all the nodes are 
            visited.
        """
        return self.__cycle_dfs(visited,src,src)

    


def main():
    g=Graph(5)
    g.AddEdge(1,2)
    g.AddEdge(2,3)
    g.AddEdge(2,4)
    g.AddEdge(3,4)
    #g.BFS(2)
    #g.DFS(1)
    print(g.undirected_graph_cycle_BFS(1))
    print(g.undirected_graph_cycle_DFS(1))
if __name__=="__main__":
    main()
