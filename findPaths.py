# Python 3 program to count all paths  
# from a source to a destination.  
  
# A directed graph using adjacency  
# list representation  
class Graph: 
  
    def __init__(self, V): 
        self.V = V  
        self.adj = [[] for i in range(V)] 
      
    def addEdge(self, u, v): 
          
        # Add v to u’s list.  
        self.adj[u].append(v) 
      
    # Returns count of paths from 's' to 'd'  
    def countPaths(self, s, d): 
          
        # Mark all the vertices  
        # as not visited  
        visited = [False] * self.V 
      
        # Call the recursive helper  
        # function to print all paths  
        pathCount = [0]  
        self.countPathsUtil(s, d, visited, pathCount)  
        return pathCount[0] 
      
    # A recursive function to print all paths  
    # from 'u' to 'd'. visited[] keeps track   
    # of vertices in current path. path[]  
    # stores actual vertices and path_index  
    # is current index in path[]  
    def countPathsUtil(self, u, d,  
                       visited, pathCount): 
        visited[u] = True
      
        # If current vertex is same as  
        # destination, then increment count  
        if (u == d): 
            pathCount[0] += 1
      
        # If current vertex is not destination  
        else: 
              
            # Recur for all the vertices  
            # adjacent to current vertex 
            i = 0
            while i < len(self.adj[u]): 
                if (not visited[self.adj[u][i]]):  
                    self.countPathsUtil(self.adj[u][i], d,  
                                        visited, pathCount) 
                i += 1
      
        visited[u] = False
  
# Driver Code  
if __name__ == '__main__': 
  
    # Create a graph given in the  
    # above diagram  
    g = Graph(5)  
    g.addEdge(0, 1)  
    g.addEdge(0, 3)  
    g.addEdge(0, 5)  
    g.addEdge(1, 2)  
    g.addEdge(1, 3)  
    g.addEdge(2, 3)
    g.addEdge(2, 4)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(0, 5)    
  
    s = 0 #starting vertex
    d = 5 #destination vertex
    print(g.countPaths(s, d)) 
  
# This code is contributed by PranchalK and edited by Andrew 
