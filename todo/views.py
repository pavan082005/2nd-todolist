from django.shortcuts import render, redirect
from .models import Todo
from .forms import Todoform
from django.views.decorators.http import require_POST
# Create your views here.
def index(request):
    todo_items = Todo.objects.order_by('id')
    form = Todoform()
    context = {'todo_items' : todo_items, 'form' : form}
    return render(request, 'todo/index.html', context)

@require_POST
def addTodo(request):
    form = Todoform(request.POST)
    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()
    return redirect('index')