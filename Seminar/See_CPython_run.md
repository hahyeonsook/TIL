# ["See CPython run: Getting to know your Python interpreter" - James Bennett (North Bay Python 2019)](https://www.youtube.com/watch?v=tzYhv61piNY)


 ```python
 import ast, inspect, pprint


def slow_week():
    seconds_per_day = 86400
    return 7 * seconds_per_day


pprint.pprint(ast.dump(ast.parse(inspect.getsource(slow_week))))
 ```

* 위의 코드는 파이썬에게 추상 구문 트리를 보여달라고 요청하는 코드이다.
* 아래는 위의 코드를 실행시킨 결과로 볼 수 있는 출력이다.

Module(
    body=[
        FunctionDef(
            name='slow_week', 
            args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]),
            body=[
                Assign(targets=[Name(id='seconds_per_day', ctx=Store())], value=Constant(value=86400)), 
                Return(value=BinOp(left=Constant(value=7), op=Mult(), right=Name(id='seconds_per_day', ctx=Load())))
            ],
            decorator_list=[]
        )
    ], 
    type_ignores=[]
)

* dis는 Python이 아래에서 수행하는 작업을 볼 수 있도록 한다.
* `slow_week`를 실행할 때, python이 실제로 하고 있는 것을 볼 수 있는 것이다.

```python
import dis

dis.dis(slow_week)
```

5           0 LOAD_CONST               1 (86400)
            2 STORE_FAST               0 (seconds_per_day)

6           4 LOAD_CONST               2 (7)
            6 LOAD_FAST                0 (seconds_per_day)
            8 BINARY_MULTIPLY
            10 RETURN_VALU

* 컴퓨터 내부의 CPU에는 많은 전기 회로가 있는 실리콘 웨이퍼가 있다.
* 이 전기 회로의 작동 방식은 특정 패턴의 전기를 보내면 정채진 패턴의 전기가 나오고, 이 패턴은 특정 동작을 일으키도록 설정되어 있다.
* 이런 패턴에 이름을 부여하는데, 그것을 명령어라고 부른다.

* 우리는 친근하고 읽기 쉬운 소스 코드를 좋아하지만, 컴퓨터는 오직 2진 명령어만 이해한다.
* 컴파일러는 이런 소스 코드를 컴퓨터에 필요한 프로세서용 명령으로 변환하여 컴파일되도록 하는 훌륭한 도구이다.

* Is Python an interpreted language or a compiled one?
  * Yes

* 일부 언어들에서는 컴퓨터 내부에 있는 특정 프로세서에 대해 두 가지 명령으로 컴파일하는 대신 가상 머신을 구축하는 방법을 사용한다.
* 가상 머신은 프로세서를 모방하는 소프트웨어 조각을 만든다. 그 소프트웨어는 명령어로 무엇을 해야 하는지 알고 있다. 그리고 명령어를 컴퓨터에 대한 실제 명령어로 변환한다. 그리고 이것들을 바이트 코드라고 부른다.
* 바이트 코드가 Java, C#, 모든 .NET 언어들, 모든 jvm 언어들, Python 에서 사용된다.
* 바이트 코드는 파이썬이 실제로 실행하는 것이므로 가상 머신은 이런 바이트 코드 명령어들을 실행하는 방법을 알고 있는 프로세서의 소프트웨어 구현을 제공한다.
* 이런 파일들을 보고싶다면 파이썬이 .pyc 확장자를 사용하여 남겨둔 파이썬 바이트 코드 파일을 볼 수 있다.
* 파이썬이 코드를 로드, 파서, 이해한 후 가장 먼저 하는 일 중에 하나는 파이썬을 바이트 코드로 컴파일하고 pyc 파일로 저장하는 것이다. 
* 왜냐면 코드를 로드, 파서, 이해하는 것을 다시 반복하지 않기 위해서이다.
* 즉, python의 가상 머신을 위해 소스 코드가 바이트 코드로 컴파일 된 것을 저장하는 것이다.

~11:00