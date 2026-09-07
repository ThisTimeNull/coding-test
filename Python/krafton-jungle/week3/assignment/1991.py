# 백준 1991 : 트리 순회
import sys
input = sys.stdin.readline

N = int(input().strip())

tree = {}
for i in range(N):
    root, left, right = input().strip().split()
    tree[root] = (left, right)

def preorder(node):
    if node == '.':
        return
    
    print(node, end='')
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node):
    if node == '.':
        return
    
    inorder(tree[node][0])
    print(node, end='')
    inorder(tree[node][1])

def postorder(node):
    if node == '.':
        return
    
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end='')

print(f"{preorder('A')}\n{inorder('A')}\n{postorder('A')}")

# ---------------------------------------------------------------------------
# 다른 풀이방법
import sys
input = sys.stdin.readline
N = int(input().strip())

graph = {}
for _ in range(N):
    a,b,c = input().strip().split()
    graph[a] = (b,c)

preorder_result = ""
inorder_result = ""
postorder_result = ""

def solve(node = "A"):
    global preorder_result, inorder_result, postorder_result
    
    if node != ".":
        preorder_result += node
        solve(graph[node][0])
        inorder_result += node
        solve(graph[node][1])
        postorder_result += node
        
solve()
print(f"{preorder_result}\n{inorder_result}\n{postorder_result}")