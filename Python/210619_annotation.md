# PEP 3107 - Function Annotations

## 이유

Python 2.x 시리즈는 함수의 파라미터와 리턴 값을 표기할 표준적인 주석 방법이 없었고, 여러 툴과 라이브러리들이 그 갭을 메우고 있었다. 다른 사람들이 함수의 docstring을 분석하거나, 여기서 주석을 찾는 동안 몇몇은 PEP 318에서 소개된 decorator을 활용했다.

이 PEP는 이 시점까지 존재했던 매커니즘과 구문이 광범위하게 변경되어 생긴 혼란을 줄이기 위해, 이를 명시하는 표준적인 방법을 제공하는 것을 목표로 한다.

## Function Annotations의 기초

Python 3.0의 Function Annotation의 내/외부에 대해 논의하기 전에, 먼저 무엇이 annotations 이고, 무엇이 annotations이 아닌지에 대해 이야기해보자.

1. Function annotations, 파라미터와 리턴 값들 모두 완전히 선택사항이다.
2. Function annotations는 컴파일 시간에 임의의 파이썬 표현식과 연결짓는 하나의 방법에 지나지 않는다.

--- 
* https://www.python.org/dev/peps/pep-3107/