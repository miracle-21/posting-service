# 📎 목차

1. [Posting Service](#-posting-service)
2. [개발 기간](#-개발-기간)
3. [개발 인원](#-개발-인원)
4. [요구사항 및 분석](#-요구사항-및-분석)
5. [기술 스택](#-기술-스택)
6. [API Endpoints](#api-endpoints)
7. [ERD](#-erd)
8. [API 명세서](#-api-명세서)


# 🚀Posting Service
- 비밀번호 설정이 가능한 게시물을 자유롭게 생성/삭제/수정이 가능한 서비스

# 📆 개발 기간
- 2022.09.06 ~ 2022.09.07(2일)

## 🧑🏻‍💻 개발 인원(1명)
- 박민하

## 📝 요구사항 및 분석
1. 게시물 생성
    - 제목과 본문으로 구성
    - 제목은 최대 20자, 본문은 200자로 제한
    - 제목과 본문 모두 이모지 포함 가능

2. 게시물 올릴 때 비밀번호 설정 가능
    - 추후 본인이 작성한 게시물에 비밀번호 입력 후 수정, 삭제 가능
    - 회원가입, 로그인 없이 비밀번호만 일치하면 수정, 삭제 가능
    - 비밀번호는 데이터베이스에 암호화된 형태로 저장
    - 비밀번호는 6자 이상, 숫자 1개 이상 반드시 포함

3. 게시물 정렬
    - 모든 사용자는 한 페이지 내에서 모든 게시물을 최신 글 순서로 확인 가능

## 🛠 기술 스택
Language | Framwork | Database | HTTP | Tools
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> |  <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"> 

## 🎯 API Endpoints
| endpoint | HTTP Method | 기능 | require parameter | response data |
|----------|-------------|------|-------------------|---------------|
|          |             |      |                   |               |
|          |             |      |                   |               |
|          |             |      |                   |               |

## 📚 ERD
![](https://velog.velcdn.com/images/miracle-21/post/c5922cbf-f5ad-43fb-8cc1-418cf6c6c7a8/image.png)

## 🔖 API 명세서
- postman API