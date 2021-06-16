## Stack

* Order, 순서를 지킨다(LIFO).
* Unique, 유니크하진 않다.
* Search, TOP의 값들을 빼면서 검색해야 한다.
* Modification, 어렵다.

* 끝에 들어온 값이 중요하다.


```python
# 파이썬에서는 list로 사용하는 것을 권장
_list = []
```

## Queue

```python
from collections import deque

dq = deque()
dq = deque([1, 2, 3, 4, 5]) # literable한 데이터를 넣어서 만듬

dq.append(6)
dq.appendleft(6) # 앞에서 하는 연산은 left를 붙인다.

removed = dq.pop() # pop(), popleft() 연산은 제거한 값을 리턴한다.
removed = dq.popleft()

# dq.rotate(n) : dq.appendleft(dq.pop()) * n (n > 0)
# dq.rotate(n) : dq.append(dq.popleft()) * |n| (n < 0)
dq.rotate(1) # [5, 1, 2, 3, 4]
dq.rotate(-2) # []
```