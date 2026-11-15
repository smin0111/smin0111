<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=header&text=Seungmin's%20GitHub&fontSize=50" width="100%"/>
</div>

## 이승민 // Backend Developer

<a href="https://charming-floss-d83.notion.site/2c2e4c08601480c096eeca4867278c68"><img src="https://img.shields.io/badge/Notion-000000?style=flat-square&logo=notion&logoColor=white"/></a>
<a href="https://www.youtube.com/@devscene60"><img src="https://img.shields.io/badge/YouTube-FF0000?style=flat-square&logo=youtube&logoColor=white"/></a>
<a href="https://www.instagram.com/devscene60/"><img src="https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white"/></a>
<a href="mailto:seungmin6385@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white"/></a>

## Projects

### [Salus](https://github.com/smin0111/Salus/tree/develop) — 알레르기·건강 정보를 반영해 레시피를 알려주는 로컬 LLM 식생활 서비스

> `2026.01 ~ 현재` | 개인 프로젝트 (5인 팀 프로젝트로 시작해 2026.06부터 혼자 이어서 개발) | 기획 · 백엔드 · 운영

알레르기·건강 정보를 한 번 등록해 두면, 매번 묻지 않아도 먹어도 되는지 판단해 주는 서비스입니다. 지금은 채팅으로 요리를 물으면 미리 넣어 둔 기본 레시피나 웹에서 찾은 실제 레시피를 출처와 함께 보여 주고, 등록한 알레르기 재료가 포함되어 있으면 위험을 알려 줍니다. 최종 목표는 맛을 지키는 대체 재료와 요리까지 알려 주는 것입니다.

**구현한 것**

- 처음 보는 요리는 SearXNG로 웹 레시피를 찾아, 페이지의 JSON-LD를 먼저 읽고 없을 때만 `gemma3:4b`가 본문에서 재료와 단계를 추출
- 버터·치즈처럼 이름에 '우유'가 없어도 우유로 만든 재료까지 잡아내는 알레르기 사전과 판정 로직
- 실제 서비스 판정 코드를 그대로 쓰는 평가 하네스로 로컬 모델 8개를 같은 조건에서 비교해, 대화는 `qwen3:8b`, 추출·요약은 `gemma3:4b`로 역할 분리
- Google·Kakao·Apple·이메일 로그인. 같은 이메일 계정은 기존 계정 재인증 후에만 연결하고, 이미 쓴 Refresh 토큰이 다시 오면 탈취로 보고 그 회원의 토큰을 모두 폐기
- 포트원 V2 결제. 금액은 서버가 정하고 결제 결과는 포트원에 다시 조회해 대조, 앱이 꺼져도 웹훅으로 한 번만 처리
- Redis로 후속 요청용 레시피 작업 세션(TTL) 관리, Redis 장애 시 서버 메모리로 이어 가도록 대비
- Flyway로 스키마 변경 관리, 실제 MySQL 통합 테스트로 동시 가입·스키마 불일치 검증, 맥북 베타 서버 운영과 암호화 백업·복구 확인

**해결한 문제**

- LLM이 검색 결과 요약문만 보고 레시피를 지어냄 → 레시피 페이지를 직접 열어 그대로 꺼내 오는 방식으로 바꿔, 처음 보는 요리 14개 모두 출처를 찾고 본문 추출 시험에서 지어낸 재료 0개
- 같은 코드인데 평가 결과와 알레르기 누출 여부까지 달라짐 → 프롬프트 JSON 형식을 만들던 `Map.of`의 순서가 JVM을 띄울 때마다 달라진 것이 원인. 순서를 고정하자 3회 반복 결과가 같아짐
- 우유 알레르기 사용자에게 버터·탈지분유가 남은 레시피를 "우유 제외"로 안내함 → 제외 판단과 최종 검증이 '우유'라는 글자만 본 것이 원인. 파생 원료까지 포함한 알레르기 사전 기준으로 판정하도록 바꿔, 실전 질문 43개에서 알레르기 위반 1건 → 0건
- 등록 알레르기 '오이'의 끝 글자를 조사로 잘라 '오'로 판정 → 등록된 이름은 자르지 않도록 바꾸고 포도·송이 등 같은 형태를 회귀 테스트로 추가

`Java 17` `Spring Boot` `Spring Security` `JPA` `Flyway` `MySQL` `Redis` `Ollama` `SearXNG` `React Native(Expo)` `Docker` `Nginx` `GitHub Actions`

---

### [HulaHoop Gateway](https://github.com/HulaHoop-Gateway) — AI 채팅으로 영화 예매·공유 전기자전거 대여의 실제 예약·결제·취소로 잇는 O2O 플랫폼

> `2025.10 ~ 2025.12` | KD아카데미 팀 프로젝트 (4인) | PM · 백엔드 | 팀 병합 PR 139건 중 78건(56%) 작성

앞으로 AI가 배달 주문, 쇼핑, 미용실 예약, 항공권 구매처럼 오프라인 서비스까지 대신 처리하게 될 거라고 봤습니다. 그러면 수많은 AI 서비스와 플랫폼이 서로 하나하나 연결되어야 하는데, N×N 연결은 비효율적입니다. HulaHoop Gateway는 그 사이에서 AI의 요청을 받아 알맞은 플랫폼으로 이어 주는 하나의 연결 지점을 목표로 했습니다. 그중 **예약**에 초점을 맞춰, 영화 예매와 공유 전기자전거 대여를 예로 예약·결제·취소까지 실제로 이어지는 프로토타입을 만들었습니다.

**구현한 것**

- AI 서버는 게이트웨이 주소 하나로만 요청하고, Spring Cloud Gateway가 요청의 `intent`(movie·bike)를 보고 영화·전기자전거 서버로 전달하도록 라우팅 구성
- AI 대화로 영화관 조회부터 상영 일정·좌석 선택·결제·예약 확정·취소까지 이어지는 영화 예매 흐름
- 여러 좌석을 `bookingGroupId`로 묶어 그룹 단위 조회·취소·환불 금액 계산
- 영화관·전기자전거 서버의 결제·환불 결과를 관리자 서버 한곳에 모아, 가맹점별·일/월별 거래 건수·비중·매출·환불액·순매출 통계 제공
- Docker Compose로 컨테이너 10개를 AWS EC2·RDS에 배포, 서브도메인 4개 HTTPS (배포 저장소 커밋 60개 모두 작성)

**해결한 문제**

- 좌석을 고르는 순간 예약을 저장해 결제에 실패하면 좌석만 묶임 → Toss Payments 승인 뒤에 예약을 확정하도록 순서를 바꿈
- 모든 사용자가 하나의 대화 상태를 공유 → 인증된 사용자 ID 기준으로 대화 이력과 예매 단계를 분리
- 컨테이너 시간대가 UTC라 예약 날짜가 하루 밀림 → JVM 시간대를 Asia/Seoul로 맞춤

`Java` `Spring Boot` `Spring Cloud Gateway` `MyBatis` `MySQL` `Toss Payments` `Next.js` `Docker` `Nginx` `AWS EC2·RDS`

---

## Skills

<table>
<tr>
<td width="50%" align="center" valign="top">
<h4>Language</h4>
<img src="https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white"/>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=white"/>
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white"/>
</td>
<td width="50%" align="center" valign="top">
<h4>Backend</h4>
<img src="https://img.shields.io/badge/Spring%20Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white"/>
<img src="https://img.shields.io/badge/Spring%20Security-6DB33F?style=flat-square&logo=springsecurity&logoColor=white"/>
<img src="https://img.shields.io/badge/Spring%20Cloud%20Gateway-6DB33F?style=flat-square&logo=spring&logoColor=white"/>
<img src="https://img.shields.io/badge/JPA%C2%B7Hibernate-59666C?style=flat-square&logo=hibernate&logoColor=white"/>
<img src="https://img.shields.io/badge/MyBatis-B7292E?style=flat-square"/>
<img src="https://img.shields.io/badge/JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white"/>
<img src="https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white"/>
</td>
</tr>
<tr>
<td width="50%" align="center" valign="top">
<h4>Data & AI</h4>
<img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white"/>
<img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white"/>
<img src="https://img.shields.io/badge/Flyway-CC0200?style=flat-square&logo=flyway&logoColor=white"/>
<img src="https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white"/>
<img src="https://img.shields.io/badge/SearXNG-3050FF?style=flat-square"/>
</td>
<td width="50%" align="center" valign="top">
<h4>Frontend & app</h4>
<img src="https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=white"/>
<img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white"/>
<img src="https://img.shields.io/badge/React%20Native-61DAFB?style=flat-square&logo=react&logoColor=white"/>
<img src="https://img.shields.io/badge/Expo-000020?style=flat-square&logo=expo&logoColor=white"/>
</td>
</tr>
<tr>
<td width="50%" align="center" valign="top">
<h4>Infra & DevOps</h4>
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white"/>
<img src="https://img.shields.io/badge/AWS%20EC2-FF9900?style=flat-square&logo=amazonec2&logoColor=white"/>
<img src="https://img.shields.io/badge/AWS%20RDS-527FFF?style=flat-square&logo=amazonrds&logoColor=white"/>
<img src="https://img.shields.io/badge/Tailscale-242424?style=flat-square&logo=tailscale&logoColor=white"/>
</td>
<td width="50%" align="center" valign="top">
<h4>Payments & tools</h4>
<img src="https://img.shields.io/badge/PortOne%20V2-1D2CFF?style=flat-square"/>
<img src="https://img.shields.io/badge/Toss%20Payments-0064FF?style=flat-square"/>
<img src="https://img.shields.io/badge/JUnit%205-25A162?style=flat-square&logo=junit5&logoColor=white"/>
<img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white"/>
<img src="https://img.shields.io/badge/Claude%20Code-D97757?style=flat-square&logo=claude&logoColor=white"/>
<img src="https://img.shields.io/badge/Codex-412991?style=flat-square&logo=openai&logoColor=white"/>
</td>
</tr>
</table>

## What I've Done

| 분야 | 경험 |
| --- | --- |
| Backend | Spring Boot로 REST API, Spring Security·JWT 소셜·이메일 인증, 결제 연동(포트원 V2, Toss Payments)을 만들었습니다. 외부 결제사 호출은 트랜잭션 밖에 두고 DB 쓰기만 묶어 트랜잭션 경계를 나눴습니다 |
| Data | JPA(Salus)와 MyBatis(HulaHoop)를 모두 써 봤습니다. 스키마는 Flyway로 관리하고 실제 MySQL로 통합 테스트합니다. Redis는 TTL이 있는 짧은 상태에 씁니다 |
| AI | Ollama로 로컬 LLM을 붙이고, 외부 근거를 찾아 답에 쓰되 근거가 없으면 답하지 않고 원문과 맞는지 검증하는 구조를 만들었습니다. 모델은 평가 하네스로 같은 조건에서 비교해 골랐습니다 |
| Infra | Docker Compose와 Nginx로 직접 배포했고, AWS EC2·RDS와 맥북 베타 서버에서 운영하며 암호화 백업과 복구를 확인합니다 |
| Frontend | React, Next.js, React Native(Expo)로 화면을 붙일 수 있습니다 |
| Tools | Git과 GitHub Issue·PR로 협업합니다. Claude Code로 구현하고 Codex로 따로 검토받으며, 두 도구가 같은 규칙을 따르도록 `AGENTS.md`를 만들어 씁니다 |

## GitHub

<p align="center">
<img src="./assets/github-langs.svg" width="60%"/>
</p>

## Education & Certification

- KD아카데미 풀스택 개발자 과정 수료 `2025.06 ~ 2025.12` (팀 프로젝트 2회 팀장·PM)
- 정보처리산업기사 `2025.06`
