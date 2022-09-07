import json
import bcrypt

from django.views import View
from django.http import JsonResponse
from django.core.exceptions import ValidationError

from core.validation import validate_password
from boards.models import Board

class CreateView(View):
    """
    * 게시물 생성: 제목, 내용, 비밀번호 필요
    * @POST ("/boards")
    * @returns json
    """
    def post(self, request):
        try:
            data    = json.loads(request.body)

            title   = data['title']
            context = data['context']
            passwd  = data['passwd']

            # 비밀번호 유효성 검사
            validate_password(passwd)

            # 비밀번호 암호화
            hashed_password  = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt())
            
            Board.objects.create(
                title   = title,
                context = context,
                passwd  = hashed_password.decode('utf-8')
            )

            return JsonResponse({'message' : 'success'}, status = 201)
        except ValidationError as error:
            return JsonResponse({'message' : error.message}, status = 400)

class DeleteView(View):
    """
    * 게시물 삭제: 비밀번호 필요
    * @DELETE ("/boards/delete/:id")
    * @returns json
    """
    def delete(self, request, id):
        data  = json.loads(request.body)
        board = Board.objects.get(id=id)

        # 비밀번호 비교, 일지하지 않으면 에러 메세지 반환.
        if not bcrypt.checkpw(data['passwd'].encode('utf-8'), board.passwd.encode('utf-8')):
            return JsonResponse({'message' : 'invalid password'}, status = 401)
        else:
            board.delete()
            return JsonResponse({'message' : 'success'}, status = 200)


class UpdateView(View):
    """
    * 게시물 수정: 비밀번호 필요
    * @PATCH ("/boards/update/:id")
    * @returns json
    """
    def patch(self, request, id):
        data  = json.loads(request.body)
        board = Board.objects.get(id=id)

        # 비밀번호 비교, 일지하지 않으면 에러 메세지 반환.
        if not bcrypt.checkpw(data['passwd'].encode('utf-8'), board.passwd.encode('utf-8')):
            return JsonResponse({'message' : 'invalid password'}, status = 401)
        else:
            data  = json.loads(request.body)
            board = Board.objects.get(id=id)

            if 'title' in data.keys():
                board.title   = data['title']
            if 'context' in data.keys():
                board.context = data['context']
            
            board.save()

            return JsonResponse({'message' : 'success'}, status = 200)
