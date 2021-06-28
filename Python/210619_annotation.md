# PEP 3107 - Function Annotations

## 이유

Python 2.x 시리즈는 함수의 파라미터와 리턴 값을 표기할 표준적인 주석 방법이 없었고, 여러 툴과 라이브러리들이 그 갭을 메우고 있었다. 다른 사람들이 함수의 docstring을 분석하거나, 여기서 주석을 찾는 동안 몇몇은 PEP 318에서 소개된 decorator을 활용했다.

이 PEP는 이 시점까지 존재했던 매커니즘과 구문이 광범위하게 변경되어 생긴 혼란을 줄이기 위해, 이를 명시하는 표준적인 방법을 제공하는 것을 목표로 한다.

## Function Annotations의 기초

Python 3.0의 Function Annotation의 내/외부에 대해 논의하기 전에, 먼저 무엇이 annotations 이고, 무엇이 annotations이 아닌지에 대해 이야기해보자.

1. Function annotations, 파라미터와 리턴 값들 모두 완전히 선택사항이다.
2. Function annotations는 컴파일 시간에 임의의 파이썬 표현식과 연결짓는 하나의 방법에 지나지 않는다.

   그것 자체로, 파이썬은 annotations에 어떤 특별한 의미나 중요성을 두지 않는다. 파이썬은 이러한 표현식을 아래 Accessing Function Annotations 문단에서 설명된 대로 사용할 수 있도록 간단하게 만들었다.

   annotation이 의미를 갖는 유일한 방법은 제 3의 라이브러리들에 의해 해석될 때이다. 이러한 annotation 사용자들은 함수의 주석들을 사용하여 원하는   모든  것을 할 수 있다. 예를 들어, 한 라이브러리는 문자열 기반의 주석을 사용하여 향상된 도움말 메시지를 제공할 수 있다. 다음과 같이   
   ```python3
   def compile(source: "something compilable",
               filename: "where the compilable thing comes from",
               mode: "is this a single statement or suite?"):   
       ...
   ```   
   또 다른 라이브러리는 파이썬의 function과 method의 typechecking을 제공하는데 사용될 수 있다. 이 라이브러리는 annotation를 함수의 input과 return 타입을 나타내는데 사용할 수 있었다. 
   
   ```
   def haul(item: Haulable, *vargs: PackAnimal) -> Distance:
       ...
   ```
   
   하지만 첫 번째 예시의 문자열이나 두 번째 예신의 타입 정보 모두 자신으로서는 의미를 갖지 않고 다른 라이브러리에서만 의미를 가진다.

3. 2번에 따르면, 이 PEP는 built-in types와 같은 어떤 종류의 표준 의미론도 소개하려고 시도하지 않는다. 이 작업은 제 3의 라이브러리에 맡긴다.

## Syntax

### Parameters

매개 변수를 위한 주석의 형식은 다음과 같이 매개 변수 이름 뒤에 온다.
```python
def foo(a: expression, b: expression = 5):
    ...
```

수도 문법에서, 매개 변수는 `identifier [: expression] [=expression]` 처럼 보여진다. 즉, 주석은 항상 매개 변수의 기본 값 보다 먼저 와야 하며, 주석과 기본 값 모두 선택 사항이라는 것이다. 마치/같은 등부호가 기본 값을 나타내는 데 사용되는 것처럼, 콜론도 주석을 나타내는데 사용된다. 모든 주석 표현식은 기본 값처럼, 함수 정의가 실행될 때 평가된다.

많은 매 개변수(*args, **kwargs 같은 매개 변수)도 유사하게 표시된다.
```python
def foo(*args: expression, **kwargs: expression):
    ...
```

중첩된 매개 변수들의 주석은 항상 마지막 괄호 뒤가 아닌 매개 변수의 이름 뒤에 따라온다. 중첩된 매개 변수의 주석처리는 필수는 아니다.

```python
def foo((x1, y1: expression),
        (x2: expression, y2: expression)=(None, None)):
    ...
```

--- 
* https://www.python.org/dev/peps/pep-3107/