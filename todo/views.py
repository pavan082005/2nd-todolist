from django.shortcuts import render
from .models import Todo
# Create your views here.
def index(request):
    todo_items = Todo.objects.order_by('id')
    context = {'todo_items' : todo_items}
    return render(request, 'todo/index.html', context)