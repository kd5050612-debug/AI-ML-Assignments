graph = {} #isme bhi empty dic banayi jisme graph store hoga

n = int(input("Enter number of nodes: ")) #Krishna isme no of nodes put karega

for _ in range(n): #ye loop bhi n time chalega if 5 then 5 times
    node = input("Node: ") #Krishna se node ka naam le rahe
    graph[node] = input(f"Neighbours of {node}: ").split() #node kea neighbour ka ip le rahe or split to pata hee hai

start = input("Enter starting node: ") #Starting node dal rahe

def dfs(v, vis): #do func banaye ek current node and dusra visited node
    print(v, end=" ") #Current node ko print kardo
    vis.add(v) #Current node ko visit mark kardo

    for i in graph[v]: #Current node kea neighbour check karo or loop ek-ek neighbour chalao
        if i not in vis: #check karo ki neigh visit hua hai ki nhi
            dfs(i, vis) #isko recurrsive call kehte hai isme app fir se func call hoga

print("\nDFS Traversal:")
dfs(start, set())

#DFS Hogaya
