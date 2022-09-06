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
            data = json.loads(request.body)

            title = data['title']
            content = data['content']
            passwd = data['passwd']

            validate_password(passwd)

            hashed_password  = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt())
            
            Board.objects.create(
                title = title,
                content = content,
                passwd = hashed_password.decode('utf-8')
            )

            return JsonResponse({'message' : 'success'}, status = 201)
        except ValidationError as error:
            return JsonResponse({'message' : error.message}, status = 400)