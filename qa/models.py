from django.db import models
from django.urls import reverse

# Create your models here.
class Board(models.Model):
    title       = models.CharField(max_length=200, verbose_name="제목")
    author      = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, verbose_name="작성자")
    contents    = models.TextField(verbose_name="내용")
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    updated_at  = models.DateTimeField(auto_now=True, verbose_name="최종수정일")
    
    class Meta:
        db_table            = 'boards'
        verbose_name        = '게시판'
        verbose_name_plural = '게시판'
        ordering            = ['-created_at', '-updated_at']
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('qa:board_detail', args=[str(self.id)])
    

class Author(models.Model):
    first_name  = models.CharField(max_length=100, verbose_name="이름")
    last_name   = models.CharField(max_length=100, verbose_name="성")
    email       = models.EmailField()

    class Meta:
        db_table            = 'authors'
        verbose_name        = '작성자'
        verbose_name_plural = '작성자'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
