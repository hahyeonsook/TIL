## Python 자료형

### 리스트
* 연속된 공간에 요소를 배치하는 배열의 장점과 다양한 타입을 연결해 배치하는 연결 리스트의 장점을 모두 취한 형태이다.

```python
# 리스트 선언
>>> a = list()
>>> a = []

# 값 추가
>>> a = [1, 2, 3]
>>> a
[1, 2, 3]
>>> a.append(4)
>>> a
[1, 2, 3, 4]

# 특정 인덱스에 값 추가
>>> a.insert(3, 5)
>>> a
[1, 2, 3, 5, 4]

# 값 출력
>>> a[3]
5

# 슬라이싱
>>> a[1:3]
[2, 3]
>>> a[:3]
[1, 2, 3]
>>> a[4:]
[5, 4]

# 값으로 요소 삭제
>>> a.remove(5)
>>> a
[1, 2, 3, 4]

# 인덱스로 요소 삭제
>>> del a[2]
>>> a
[1, 2, 4]
```

### 딕셔너리

```python
# 딕셔너리 선언
>>> a = dict()
>>> a = {}

# 값 추가
>>> a = {'key1': 'value1', 'key2': 'value2'}
>>> a
{'key1': 'value1', 'key2': 'value2'}
>>> a['key3'] = 'value3'
>>> a
{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# 값 삭제
>>> del a['key3']
>>> a
{'key1': 'value1', 'key2': 'value2'}

# 값 출력
>>> for k, v in a.items():
...     print(k, v)
...
key1 value1
key2 value2
key3 value3
```

### 딕셔너리 모듈

#### defaultdict 객체
* 존재하지 않는 키를 조회할 경우, 디폴트 값으로 해당 키의 아이템을 생성.

```python
>>> a = collections.defaultdict(int)
>>> a['A'] = 5
>>> a['B'] = 4
>>> a
defaultdict(<class 'int'>, {'A': 5, 'B': 4})

>>> a['C'] += 1
>>> a
defaultdict(<class 'int'>, {'A': 5, 'B': 4, 'C': 1})
```

#### Counter 객체
* 아이템에 대한 계수를 계산해 딕셔너리로 리턴
  
```python
>>> a = [1, 2, 3, 4, 5, 5, 5, 6, 6]
>>> b = collections.Counter(a)
>>> b
Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1})

>>> type(b)
<class 'collections.Counter'>

# 가장 빈도 수가 높은 요소 추출
>>> b.most_common(2)
[(5, 3), (6, 2)]
```