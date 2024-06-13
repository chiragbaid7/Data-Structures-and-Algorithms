from collections import defaultdict, deque 

class Graph:

    def __init__(self,nodes):
        #this will create empty list as a value for a non existent key
        self.graph=defaultdict(list)
        self.nodes=nodes

    def AddEdge(self,x,y):
        self.graph[x].append(y)
        #self.list[y].append(x)

    def topology_sort(self):        
        indegree=[0]*self.nodes 
        for parent in self.graph:
            for node in self.graph[parent]:
                indegree[node]+=1
        queue=deque()
        for node in self.list:
            if(indegree[node]==0):
                queue.append(node)
        while(queue):
            node=queue.popleft()
            print(node)
            for neigh in self.graph[node]:
                indegree[neigh]-=1
                if(indegree[neigh]==0):
                    queue.append(neigh)

    def __util_dfs(self,src,stack,visited):
        visited[src]=True 
        for neigh in self.list[src]:
            if( not visited[neigh]):
                self.__util_dfs(neigh,stack,visited)

        stack.append(src)
        return 

    def topology_sort_dfs(self):
        stack = deque()
        visited=[False]*self.nodes 
        #for disconnected graphs 
        for node in self.graph:
            if(not visited[node]):
                self.__util_dfs(node,stack,visited)
        print(stack)

    def utilsNewDFS(self, stack, node, visited):
        visited[node] = True
        for neighbour in graph[node]:
            if(not visited[node):
                self.utilsNewDFS(stack, node, visited)
        #Leaf node
        stack.append(node)
    def topologyDFS(self):
        stack = []
        visited = [False]*self.nodes
        for node in self.graph:
            #Explore from univisted nodes only
            if(not visited[node]):
                self.utilsNewDFS(stack, node, visited):
    def topologyBFS(self):
        indegree = [0] * self.nodes
        for node in self.graph:
            for neighbour in self.grpah[node]:
                indegree[neighbour]+=1
        queue = deque()
        for node in self.graph:
            if(indegree[node] == 0):
                queue.append(node)
        while(queue):
            node = queue.popleft()
            print(node)
            for neighbour in self.graph[node]:
                indegree[neighbour]-=1
                if(indegree[neighbour] == 0):
                    queue.append(neighbour)
        for node in indegree:
            if(node > 0):
                #Graph contains cycle
                return False
        
def main():
    g=Graph(6)
    g.AddEdge(2,3)
    g.AddEdge(3,1)
    g.AddEdge(4,0)
    g.AddEdge(5,2)
    g.AddEdge(4,1)
    g.AddEdge(5,0)
    g.topology_sort()
    #g.topology_sort_dfs()

if __name__=="__main__":
    main()
    
