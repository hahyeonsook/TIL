# 인텔리제이로 스프링부트 시작하기

## Gradle

* `ext` : build.gradle에서 사용하는 전역변수 설정
* `repositories` : 각종 의존성(라이브러리)들을 어떤 원격 저장소에서 받을지를 정함
  * `mavenCentral` : 이전부터 많이 사용하는 저장소이지만, 업로드가 힘들어서 공유가 안되는 상황이 발생함
  * `jcenter` : 이런 문제점을 개선하여 라이브러리 업로드를 간단하게 함
* `dependencies` : 프로젝트 개발에 필요한 의존성들을 선언

* 자바와 스프링 부트를 사용하기 위한 필수 플러그인
  * 버전을 명시하지 않아야 `buildscript`에서 작성한 `org.springframework.boot:spring-boot-gradle-plugin:${springBootVersion}`의 버전을 따라감.
  * `java`
  * `eclipse`
  * `org.springframework.boot`
  * `io.spring.dependency-management` : 스프링 부트의 의존성을 관리해주는 플러그인

## Git 연결
