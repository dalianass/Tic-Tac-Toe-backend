from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import funkcije
from urllib.parse import unquote
import json

brd = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
  ]
  
# Create your views here.
def minimax(request):
    return HttpResponse("minimax radi")

@api_view(['GET'])
def getData(request, board):
    person = {'name': 'dalila', 'godine': 25, 'board': board}
    return Response(person)

@api_view(['GET'])
def getBoard(request):
    board = request.GET.get('board', None)
    if board:
        # decoded_board = unquote(board)
        decoded_data = json.loads(board)


        result = funkcije.minimax(decoded_data, 0, True, float('-inf'), float('inf'))
        return Response(result)
    else:
        return Response({'success': False})
    