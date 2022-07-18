from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def board_list(request):
    board_list = Board.objects.all()
    return render(request, 'qa/board_list.html', {'board_list': board_list})

def board_detail(request, id):
    board_detail = get_object_or_404(Board, id=id)
    return render(request, 'qa/board_detail.html', {'board_detail': board_detail})