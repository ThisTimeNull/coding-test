# B-Tree Implementation
import math

class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t # 최소 차수
        self.leaf = leaf
        self.keys = []
        self.children = []
        
    def insert_non_full(self, key):
        i = len(self.keys) - 1
        
        # left == True -> 리프 노드라는 소리
        if self.leaf:
            # 키를 적절한 위치에 삽입
            self.keys.append(None) # 공간 확보
            # 키를 삽입할 위치 찾기 : 오름차순 정렬
            while i >= 0 and key < self.keys[i]:
                self.keys[i+1] = self.keys[i]
                i -= 1
            self.keys[i+1] = key
        else:
            # 자식 노드로 이동  
            while i >= 0 and key < self.keys[i]:
                i -= 1
            i += 1
            
            # 자식 노드가 가득 찼다면 분할
            if len(self.children[i].keys) == (2 * self.t) - 1:
                self.split_child(i)

                if key > self.keys[i]:
                    i += 1
                
            self.children[i].insert_non_full(key)
            
    def split_child(self, i):
        t = self.t # 최소 차수
        y = self.children[i] # 분할할 자식 노드
        z = BTreeNode(y,t, leaf=y.leaf) # 새로 만들 오른쪽 자식 노드
        
        self.keys.insert(i, y.keys[t-1]) # 부모 노드에 중간 키 삽입
        self.children.insert(i + 1, z) # 새로 만든 z 노드를 부모의 자식 리스트에 추가
        
        # 키 분배
        z.keys = y.keys[t:]
        y.keys = y.keys[:t-1]
        
        # 자식 노드 분배(리프가 아닌경우)
        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]
            
    def __str__(self, level=0):
        result = " " * level + str(self.keys) + "\n"
        for child in self.children:
            result += child.__str__(level + 1)
        return result