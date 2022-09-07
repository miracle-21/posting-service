import json
import bcrypt

from django.test import TestCase, Client

from boards.models import Board

class BoardTest(TestCase):
    # 게시물 5개 생성
    def setUp(self):
        Board.objects.bulk_create([
            Board(id = 1, title = '제목1', context = '내용1', passwd=bcrypt.hashpw('wpahr1'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')),
            Board(id = 2, title = '제목2', context = '내용2', passwd=bcrypt.hashpw('wpahr2'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')),
            Board(id = 3, title = '제목3', context = '내용3', passwd=bcrypt.hashpw('wpahr3'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'))
        ])

    def tearDown(self):
        Board.objects.all().delete

    # 게시물 리스트 조회 성공
    def test_success_board_descending_get(self):
        client = Client()
        response = client.get('/boards?offset=0&limit=2')
        self.assertEqual(response.json(),
        {
            "results": [
                {
                    "id": 3,
                    "title": "제목3",
                    "context": "내용3"
                },
                {
                    "id": 2,
                    "title": "제목2",
                    "context": "내용2"
                },
            ]
        })
        self.assertEqual(response.status_code, 200)

    # 게시물 생성 성공
    def test_success_board_post(self):
        client   = Client()

        body = {"title":"제목6", "context":"내용6", "passwd":"wpahr6"}
        response = client.post('/boards/post', content_type='application/json', data=json.dumps(body))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'message' : 'success'})

    # 게시물 생성 실패
    def test_fail_board_post(self):
        client   = Client()

        body = {"title":"제목6", "context":"내용6", "passwd":"wpahr"}
        response = client.post('/boards/post', content_type='application/json', data=json.dumps(body))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message" : "invalid password"})

    # 게시물 삭제 성공
    def test_success_board_delete(self):
        client   = Client()

        body = {"passwd":"wpahr1"}
        response = client.delete('/boards/delete/1', content_type='application/json', data=json.dumps(body))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message' : 'success'})

    # 게시물 삭제 실패
    def test_fail_board_delete(self):
        client   = Client()

        body = {"passwd":"wpahr"}
        response = client.delete('/boards/delete/1', content_type='application/json', data=json.dumps(body))

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"message" : "invalid password"})

    # 게시물 수정 성공
    def test_success_board_update(self):
        client   = Client()

        body = {"context" : "내용 수정🌟", "passwd":"wpahr1"}
        response = client.patch('/boards/update/1', content_type='application/json', data=json.dumps(body))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message' : 'success'})

    # 게시물 수정 실패
    def test_fail_board_update(self):
        client   = Client()

        body = {"context" : "내용 수정🌟", "passwd":"wpahr"}
        response = client.patch('/boards/update/1', content_type='application/json', data=json.dumps(body))

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"message" : "invalid password"})