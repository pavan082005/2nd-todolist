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

def completedTodo(request, todo_id):
    todo = Todo.objects.get(pk = todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(completed__exact = True).delete()
    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('index')