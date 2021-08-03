# [Advanced Python testing techniques - 안재만 - PyCon.KR 2019](https://www.youtube.com/watch?v=3CfxhnDjtQQ)

## Test Driven Development
* 로직을 작성하기 전에 테스트를 먼저 구현

## unittest, pytest
* unittest: python 기본 지원 단위 테스트 프레임워크
* pytest: 조금 더 powerfule한 테스트 프레임워크
  * 오류가 더 자세하게 나옴.

### unittest로 구현
* class 기반으로 코드를 구현해야 함.

### pytest로 구현
* func 기반, class 기반 모두 구현할 수 있음.

## Fixture
* 테스트에서 data, context가 필요할 때 정의를 해서 사용할 수 있음.
* 어딘가에 Fixture를 정의해놓으면 test에서 사용할 수 있음.

## Sure를 이용하여 더 직관적으로 구현
* [Sure](https://github.com/gabrielfalcao/sure)
* Assertion을 쓰기 쉽게 해주는 라이브러리
* **CPython에서만 사용 가능**
* Number, String, Collection, Callable 등에 대한 assertion 지원

## Behavior Driven Development
* TDD와 유사
* 테스트 코드 그 자체보다, 비즈니스 요구사항에 집중하자
* Python Libs
  * behave, lettuce, **pytest-bdd**

### BDD로 작성해보자.
* 먼저 자연어로 테스트 코드를 작성하자.
  * ex) 정상 가입한 유저가 있을 때, 올바른 정보로 로그인을 하게 되면, 로그인이 성공해야 한다.
 
```
# login.feature
Feature: 유저 로그인 테스트
    Scenario: 정상 가입 후 로그인 케이스
        Given: 한 client가 있다.
        When: 해당 유저가 올바른 정보로 가입하면
        Then: 정상적으로 로그인이 성공해야 한다.
```
```python
@scenario('login.feature', '유저 밴 테스트')
def scenario_유저_밴_테스트():
    pass

@given('관리자 계정')
def admin():
    ...

@given('정상적으로 가입한 유저가 있다')
def registered():
    ...

@when('관리자가 해당 유저를 밴 시키면')
def 관리자가_해당_유저를_밴_시키면(admin, registered):
    admin.ban(registered.username).success()

@then('API 호출이 실패 해야 한다')
def API_호출이_실패_해야_한다(registered):
    registered.some_API().fail(403)
```

* Feature: 테스트할 대상 기능
* Scenario: 테스트 상황 설명(시나리오)
* Given: 테스트에 사용할 데이터, 컨텍스트
  * Background: 모든 시나리오에서 기본적으로 사용되는 데이터, 컨텍스트
* When: 테스트를 수행할 조건
* Then: 테스트를 수행했을 때 보장되어야 하는 결과

### BDD 사용시 유의 점
* 자연어로 define된 시나리오와 python 테스트 코드가 분리되어 있어 찾기 힘듦
* 최대한 재사용 가능한 문장으로 테스트를 구성
* When에서 동작을 수행한 return 값은 Then에서 가져올 수 없음
  * Given에서 context를 만들어 놓고, When에서 수행한 동작을 context에 저장하고 Then에서 확인하자.

## HTTP Mocking과 monkey patching으로 독립적인 테스트 코드 구현하기

### 인증서버를 분리해서 새로 구현하겠습니다.
* 로직 테스트를 위해 외부 인증서버가 필요-외부 dependency가 발생
  * mocking 사용

### HTTP Mocking
* Mocking: 거짓의, 가장의
* HTTP Mocking: 발생하는 HTTP Call을 interrupt 하여 실제로 HTTP Call을 보내지 않고, 정해진 동작을 수행하여 response를 반환하도록 함
* Python: [HTTPretty](https://github.com/gabrielfalcao/HTTPretty)
* Common Use Cases
  * TDD of API integrations
  * Fake responses of external APIs
  * Record and payback HTTP requests

### Monkey patching
* 런타임에 정의되어 있는 클래스나 모듈의 attribute를 바꿈
* 테스트 코드에서도 많이 활용
  * B 모듈을 사용하는 A 모듈을 테스트, B 모듈에서 나온 결과는 항상 같은 값으로 고정
* HTTPretty도 Monkey patching을 이용하여 구현되어 있음

## Randomized testing을 이용하여 온전한 테스트 코드 구현하기
* 이거 정말 모든 경우에 다 되는걸까?
* 랜덤한 input에 대해 function이 return해야할 값이나 수행할 동작을 테스트
  * ex) 이 함수에서는 어떤 input이 들어와도 error가 나면 안됨
  * ex) 이 함수에서는 어떤 input이 들어와도 0이상의 값이 나와야 함
* Randomized testing
  * QuickCheck
  * python - hypothesis

## Benchmark testing을 이용하여 로직 시간 측정하기
* 이거 잘 동작은 하는데, 너무 오래 걸리는 것 같아요.
* Benchmark test
  * 함수를 수행하는데 걸린 시간을 측정
  * 1초에 몇 개의 요청을 처리할 수 있는지에 대한 근사 가능
  * 다수가 사용하는 실 서비스 환경에서는 반드시 필요
  * 흔히 사용되는 로직이나 많이 호출될 것으로 보이는 API에 우선 적용
* How to?
  * time이나 timeit으로 수동 측정
  * pytest-benchmark

## 그 외 유용한 툴
* 어디서 오래 걸리는지 좀 더 자세히 보고싶어요
  * Profiling 툴을 사용(pytest-profiling)
  * 함수별 execution graph와 실행시간을 보여줌
* 우리의 N대의 서버들이 부하를 얼마나 버티는지 알고싶어요
  * http://locust.io