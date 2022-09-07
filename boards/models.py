from django.db import models

# 게시판 모델링 
class Board(models.Model):
    title       = models.CharField(max_length=20)
    context     = models.CharField(max_length=200)
    passwd      = models.CharField(max_length=100)
    created_at  = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "boards"
