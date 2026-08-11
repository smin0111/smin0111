# 안녕하세요, 서비스의 흐름을 끝까지 연결하는 백엔드 개발자 이승민입니다.

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=header&text=Seungmin's%20GitHub&fontSize=50" width="100%"/>
</div>

<br/>

<table>
<tr>
<td width="65%" valign="top">

## About Me

Java와 Spring Boot를 중심으로 백엔드 서비스를 개발하고 있습니다.

기능 하나를 구현하는 데서 끝나기보다 사용자의 요청이 **화면 → API → 데이터 → 외부 서비스 → 배포 환경**을 거쳐 실제 기능으로 동작하는 전체 흐름에 관심이 많습니다.

프로젝트를 진행하며 처음 구현한 구조의 한계를 다시 살펴보고, 다음 구현에서 개선하는 과정을 중요하게 생각합니다.

HulaHoop에서는 여러 서비스와 결제·예약 흐름을 연결했고, Salus에서는 서버 메모리에 의존하던 작업 상태를 Redis로 분리하고 외부 LLM에 의존하던 생성 구조를 로컬 LLM과 검증 파이프라인 중심으로 고도화하고 있습니다.

새로운 기술을 사용하는 것 자체보다 **왜 필요한지, 기존 방식에는 어떤 문제가 있었는지, 적용 이후 어떤 한계가 남는지** 이해하며 개발하는 것을 목표로 하고 있습니다.

</td>
<td width="35%" valign="middle" align="center">

<img src="./assets/profile.jpeg"
     width="180"
     style="border-radius: 50%;" />

<br/><br/>

<a href="mailto:seungmin6385@gmail.com">
<img src="https://img.shields.io/badge/Email-Contact-EA4335?style=flat-square&logo=gmail&logoColor=white"/>
</a>

</td>
</tr>
</table>

<br/>

## Projects

### 🩺 Salus

**건강 상태와 복용약을 고려한 AI 기반 개인 맞춤 식단·레시피 추천 서비스**

기존 팀 프로젝트를 개인 프로젝트로 분리해 백엔드 구조와 AI 생성·검증 흐름을 지속적으로 고도화하고 있습니다.

- Spring Security + JWT 기반 사용자 인증
- 건강 정보·냉장고·식단 기록 API 구현
- Redis 기반 사용자·채팅방별 작업 세션 및 TTL 적용
- Gemini 기반 생성 구조를 Ollama 로컬 LLM으로 전환
- DB에 없는 레시피는 웹 검색 결과를 생성 근거로 활용
- 검색 결과 없음과 검색 장애를 구분하여 오류 상태 관리
- LLM 생성 결과를 바로 노출하지 않고 재료·조리 단계·검색 근거와 비교
- 검증에 실패한 결과는 사용자에게 노출하지 않고 실패 원인 기록
- 알레르기·만성질환·식단 제한·복용약을 추천 흐름에 반영하는 건강 안전 검증 구조 고도화 중

**Tech Stack**

`Java 17` `Spring Boot` `Spring Security` `MyBatis` `MySQL` `Redis` `Ollama` `React Native` `Expo` `Docker`

---

### 🎬 HulaHoop Gateway

**AI 자연어 요청을 영화 예매·자전거 대여 서비스로 연결하는 O2O 플랫폼**

4인 팀에서 PM과 Backend 역할을 맡아 서비스의 주요 흐름과 시스템 간 연동을 구현했습니다.

- AI 요청을 `intent` 단위로 표준화
- Spring Cloud Gateway의 Header·Path 조건을 활용한 서비스 라우팅
- 영화관 조회 → 일정 조회 → 좌석 선택 → 결제 → 예약 → 취소 흐름 구현
- Toss Payments 결제 승인 API 연동
- `bookingGroupId` 기반 다중 좌석 예매 조회·취소 구조 구현
- 영화·자전거 서비스를 독립 서버와 DB로 분리
- 서비스 간 직접 DB 접근 대신 REST API 기반 데이터 전달
- Docker · Nginx 기반 다중 서비스 실행 및 배포 환경 구성
- HTTPS · Mixed Content · 컨테이너 통신 · 시간대 문제 해결

**Tech Stack**

`Java` `Spring Boot` `Spring Cloud Gateway` `MyBatis` `MySQL` `React` `Next.js` `Docker` `Nginx` `AWS EC2`

<br/>

## What I Care About

### Backend

- 요청과 데이터의 흐름
- 트랜잭션과 데이터 일관성
- 인증과 접근 제어
- 서비스 간 명확한 책임과 데이터 경계

### AI Application

- LLM 결과를 그대로 신뢰하지 않는 구조
- 검색 근거를 활용한 생성
- 생성 결과 검증과 실패 처리
- 민감정보와 외부 AI 서비스 간 데이터 경계

### Service & Infra

- API와 외부 서비스 연동
- Docker 기반 실행 환경
- Nginx Reverse Proxy
- 서비스 간 네트워크와 요청 흐름

<br/>

## Skills

### Backend

`Java` `Spring Boot` `Spring Security` `MyBatis` `Spring Cloud Gateway`

### Database & State

`MySQL` `Redis`

### AI

`Ollama` `Gemini API` `Web Search Augmentation` `LLM Validation`

### Frontend

`JavaScript` `TypeScript` `React` `Next.js` `React Native` `Expo`

### Infra & DevOps

`Docker` `Docker Compose` `Nginx` `AWS EC2` `Flyway` `GitHub Actions`

### Collaboration

`Git` `GitHub` `Issue` `Pull Request` `Code Review`

<br/>

## Currently Learning & Improving

- Java · Spring 기반 백엔드 기본기
- 트랜잭션과 데이터 일관성
- 인증·인가 구조
- Redis를 활용한 상태 관리
- 외부 API 연동과 장애 처리
- LLM 기반 서비스의 신뢰성 검증
- 서비스 운영을 고려한 백엔드 구조 설계
