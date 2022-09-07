from contextvars import Context
import json
import bcrypt

from django.views import View
from django.http import JsonResponse
from django.core.exceptions import ValidationError

from core.validation import validate_password
from boards.models import Board

class CreateView(View):
    def post(self, request):
        try:
            data    = json.loads(request.body)

            title   = data['title']
            context = data['context']
            passwd  = data['passwd']

            validate_password(passwd)

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
    def delete(self, request, id):
        data = json.loads(request.body)

        board = Board.objects.get(id=id)

        if not bcrypt.checkpw(data['passwd'].encode('utf-8'), board.passwd.encode('utf-8')):
            return JsonResponse({'message' : 'invalid password'}, status = 401)
        else:
            board.delete()
            return JsonResponse({'message' : 'success'}, status = 200)


class UpdateView(View):
    def patch(self, request, id):
        data = json.loads(request.body)
        board = Board.objects.get(id=id)

        if not bcrypt.checkpw(data['passwd'].encode('utf-8'), board.passwd.encode('utf-8')):
            return JsonResponse({'message' : 'invalid password'}, status = 401)
        else:
            data = json.loads(request.body)
            
            board = Board.objects.get(id=id)

            if 'title' in data.keys():
                board.title = data['title']
            if 'context' in data.keys():
                board.context = data['context']
            
            board.save()

            return JsonResponse({'message' : 'success'}, status = 200)
