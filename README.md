# ๐ ๋ชฉ์ฐจ

1. [Posting Service](#-posting-service)
2. [๊ฐ๋ฐ ๊ธฐ๊ฐ](#-๊ฐ๋ฐ-๊ธฐ๊ฐ)
3. [๊ฐ๋ฐ ์ธ์](#-๊ฐ๋ฐ-์ธ์)
4. [์๊ตฌ์ฌํญ ๋ฐ ๋ถ์](#-์๊ตฌ์ฌํญ-๋ฐ-๋ถ์)
5. [๊ธฐ์  ์คํ](#-๊ธฐ์ -์คํ)
6. [API Endpoints](#api-endpoints)
7. [ERD](#-erd)
8. [API ๋ช์ธ์](#-api-๋ช์ธ์)


# ๐Posting Service
- ๋น๋ฐ๋ฒํธ ์ค์ ์ด ๊ฐ๋ฅํ ๊ฒ์๋ฌผ์ ์์ ๋กญ๊ฒ ์์ฑ/์ญ์ /์์ ์ด ๊ฐ๋ฅํ ์๋น์ค

# ๐ ๊ฐ๋ฐ ๊ธฐ๊ฐ
- 2022.09.06 ~ 2022.09.07(2์ผ)

## ๐ง๐ปโ๐ป ๊ฐ๋ฐ ์ธ์(1๋ช)
- ๋ฐ๋ฏผํ

## ๐ ์๊ตฌ์ฌํญ ๋ฐ ๋ถ์
1. ๊ฒ์๋ฌผ ์์ฑ
    - ์ ๋ชฉ๊ณผ ๋ณธ๋ฌธ์ผ๋ก ๊ตฌ์ฑ
    - ์ ๋ชฉ์ ์ต๋ 20์, ๋ณธ๋ฌธ์ 200์๋ก ์ ํ
    - ์ ๋ชฉ๊ณผ ๋ณธ๋ฌธ ๋ชจ๋ ์ด๋ชจ์ง ํฌํจ ๊ฐ๋ฅ

2. ๊ฒ์๋ฌผ ์ฌ๋ฆด ๋ ๋น๋ฐ๋ฒํธ ์ค์  ๊ฐ๋ฅ
    - ์ถํ ๋ณธ์ธ์ด ์์ฑํ ๊ฒ์๋ฌผ์ ๋น๋ฐ๋ฒํธ ์๋ ฅ ํ ์์ , ์ญ์  ๊ฐ๋ฅ
    - ํ์๊ฐ์, ๋ก๊ทธ์ธ ์์ด ๋น๋ฐ๋ฒํธ๋ง ์ผ์นํ๋ฉด ์์ , ์ญ์  ๊ฐ๋ฅ
    - ๋น๋ฐ๋ฒํธ๋ ๋ฐ์ดํฐ๋ฒ ์ด์ค์ ์ํธํ๋ ํํ๋ก ์ ์ฅ
    - ๋น๋ฐ๋ฒํธ๋ 6์ ์ด์, ์ซ์ 1๊ฐ ์ด์ ๋ฐ๋์ ํฌํจ

3. ๊ฒ์๋ฌผ ์ ๋ ฌ
    - ๋ชจ๋  ์ฌ์ฉ์๋ ํ ํ์ด์ง ๋ด์์ ๋ชจ๋  ๊ฒ์๋ฌผ์ ์ต์  ๊ธ ์์๋ก ํ์ธ ๊ฐ๋ฅ
    - 20๊ฐ ๋จ์๋ก ๋ก๋

## ๐  ๊ธฐ์  ์คํ
Language | Framework | Database | HTTP | Tools
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> |  <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"> 

## ๐ฏ API Endpoints
| endpoint | HTTP Method | ๊ธฐ๋ฅ | require parameter | response data |
|----------|-------------|------|-------------------|---------------| 
|/boards | GET  | ๊ฒ์๋ฌผ ๋ฆฌ์คํธ ์กฐํ | | 200 OK 
| /boards/post|  POST | ๊ฒ์๋ฌผ ์์ฑ  |title: string </br> context: string  </br> passwd: string| 201 Created </br> 400 Bad Request |
| /boards/delete/:id | DELETE  | ๊ฒ์๋ฌผ ์ญ์  |   passwd: string  | 200 OK </br> 401 Unauthorized |
| /boards/update/:id | PATCH | ๊ฒ์๋ฌผ ์์  | title: string </br> context: string  </br> passwd: string | 200 OK </br> 401 Unauthorized

## ๐ ERD
![](https://velog.velcdn.com/images/miracle-21/post/c5922cbf-f5ad-43fb-8cc1-418cf6c6c7a8/image.png)

## ๐ API ๋ช์ธ์
- [postman API ๋งํฌ](https://documenter.getpostman.com/view/18832289/VVBQYVMs)

![](https://velog.velcdn.com/images/miracle-21/post/dc414f01-1ab9-4a2a-950e-d4e186348592/image.gif)


