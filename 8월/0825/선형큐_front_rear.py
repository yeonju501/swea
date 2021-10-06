# front, rear 사용
SIZE = 100
Queue = [0] * SIZE
front = rear = -1

# enQ
rear += 1
Queue[rear] = 1
rear += 1
Queue[rear] = 2
rear += 1
Queue[rear] = 3

while front != rear: # not isEmpty
    front += 1
    print(Queue[front])
