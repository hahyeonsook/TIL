# HTTP

## SSL vs TLS

### SSL은 무엇인가?
* 네트워크 상에서 인증되고 암호화된 연결을 위해 사용되는 프로토콜
* SSL은 1995년 처음 개발되었고, v1, v2를 거쳐 현재는 TLS로 대체되었음

### TLS란 무엇인가?
* SSL을 대체하는 상위 버전의 암호화 프로토콜
* 현재의 HTTPS는 TLS를 사용하지만 여전히 SSL/TLS라고 사용

### SSL 인증서란?
* 도메인 이름, 옵션들, 사이트 주인 등의 웹 사이트 정보를 포함하고 있음
* SSL 인증서가 신뢰할 수 있는 인증 기관 CA에 의해 서명된 경우, 해당 인증서를 사용하여 사인된 컨텐츠틑 신뢰할 수 있음을 의미함
* 웹 사이트의 ID를 비대칭 알고리즘으로 암호화한 디지털 문서
  * 공개키
    * 인증서에 포함되어 있음
    * 웹 브라우저가 HTTPS 프로토콜을 통해 암호화된 통신을 시작할 때 사용
  * 개인키
    * 서버에 보관되어 있음
    * 웹 페이지, 이미지, JavaScript 등의 파일에 서명할 때 사용


### SSL/TLS를 사용하려면 전용 IP를 가지고 있어야 하는가?
* 지금은 SNI(Server Name Indication)이라는 기술로 인해 꼭 필요하진 않음
* 단, 전용 IP가 아닌 SNI를 사용하려면 호스팅 플랫폼에서 SNI를 지원해야 함

### 이전 버전의 TLS의 보안 이슈는 무엇인가?
* TLS 1.0, 1.1
  * ROBOT 공격이 RSA 키 교환 알고리즘에 영향을 줄 수 있었음
  * TLS 서버가 키를 교환할 때 잘못된 매개변수를 사용하도록 속일 수 있었음
  * 키 교환시 키를 손상시키면, 공격자는 보안을 완전히 손상시키고 대화를 해독할 수 있었음 (<- 이거 해보고 싶음)
* TLS 1.2

## SSL/TLS Handshake
* 사용할 TLS 버전을 지정
* 사용할 암호 알고리즘 결정
* 서버의 TLS 인증서를 사용하여 서버의 신원 인증
* handshake가 완료된 후 키 간의 메시지를 암호화하기 위한 세션 키 생성

[](https://images.ctfassets.net/slt3lc6tev37/3wZIhjRIjfVSmCbVqkBKzb/4a7aa34324108c725dc25fc9e7c4ea4a/tls-ssl-handshake.png)

---
* [https://blog.naver.com/alice_k106/221468341565](https://blog.naver.com/alice_k106/221468341565)
* [https://www.ssl.com/faqs/faq-what-is-ssl/](https://www.ssl.com/faqs/faq-what-is-ssl/)
* [https://www.cloudflare.com/ko-kr/learning/ssl/what-is-ssl/](https://www.cloudflare.com/ko-kr/learning/ssl/what-is-ssl/)
* [https://www.ssls.com/blog/whats-the-difference-between-tls-and-ssl-certificates/](https://www.ssls.com/blog/whats-the-difference-between-tls-and-ssl-certificates/)