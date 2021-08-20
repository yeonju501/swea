## 20th August 2021 TIL

0. 저장, 인접행렬, 인접리스트
1. global ans => 함수 외부에 있는 변수와 같은 것이야!



#### DFS 알고리즘 - 반복

```python
stack s
visited []
DFS(v)
	push(s, v)
    while not isEmpty(s)
    	v = pop(s)
        if not visited[v]
        	visited(v)
            for each w in adjacency(v)
            	if not visited[w]
                	push(s, w)
```



#### DFS 알고리즘 - 재귀

```python
DFS_Recursive(G, V)
	visited[v] = True
    for each all w in adjacency(G, V)
    	if visited[w] != True
        	DFS_Recursive(G, W)
```



#### 길찾기

```python
stack s
visited []
DFS(v)
	push(s, v)
    while not isEmpty(s)
    	v = pop(s)
        if not visited[v]
        	visit(v)
            for each w in adj(v)
            	if not visited[w]
                	push(s, w)
```



```py
```

