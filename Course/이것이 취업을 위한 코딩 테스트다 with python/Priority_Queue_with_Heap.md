# [자료구조: 우선순위 큐(Priority Queue)와 힙(Heap) 10분 핵심 요약](https://www.youtube.com/watch?v=AjFlp951nz0&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=11)

## 우선순위 큐

* 우선순위 큐는 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조이다.
* 우선순위 큐는 데이터를 우선순위에 따라 처리하고 싶을 때 사용한다.

## 우선순위 큐 구현하기

* 리스트를 이용하여 구현할 수 있다.
* 힙을 이용하여 구현할 수 있다.

| 우선순위 큐 구현 방식 | 삽입 시간 | 삭제 시간 |
| :-------------------: | :-------: | :-------: |
|        리스트         |   O(1)    |   O(N)    |
|       힙(Heap)        |  O(logN)  |  O(logN)  |

* 단순히 N개의 데이터를 힙에 넣었다가 모두 꺼내는 작업은 정렬과 동일하다. (힙 정렬)
  * 이 경우 시간 복잡도는 O(NlogN)이다.

```python3
import sys
import heapq
input = sys.stdin.readline

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.headppop(h))
    return result

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

res = heapsort(arr)

for i in range(n):
    print(res[i])
```