from collections import deque #yaha python ki inbuilt collections lib se dequeue import kar rahe jisme deque(QUEUE KE LIYE)

graph = {} # ek empty dic bana di jisme graph store ho ga

n = int(input("Enter number of nodes: ")) #mujhse node ki value lenge

for _ in range(n): #loop n time chalega if user put 6 then 6 times
    node = input("Node: ") #Krishna se node ka naam liya jaega
    graph[node] = input(f"Neighbours of {node}: ").split() # isse node ka neighbour lenge(.split() - string ko list mea convert)

start = input("Enter starting node: ") #krishna starting node dalega

def bfs(start): #bfs func bana diya start matlab node se start hoga
    q = deque([start]) #Queue bana liya
    vis = {start} #vis start banaya matlab node multiple/repeat visit nahi hoga

    while q: #jab tak apna queue empty nhi hoga tab tak loop chalega
        v = q.popleft() #q ka first element nikalenge
        print(v, end=" ") #Current node print kiya jaega

        for i in graph[v]: #current node kea neighbours dekhna hai
            if i not in vis: #check karo kya node already visit hua hai
                vis.add(i) #visited mea add kardo
                q.append(i) #Q mein add karo

print("\nBFS Traversal:")
bfs(start)


#BFS HOGAYA
