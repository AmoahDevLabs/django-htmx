from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .todo import todos


def index(request):
    return render(request, 'index.html', {'todos': []})


def search(request):
    res_todos = []
    search_query = request.POST['search']
    if len(search_query) == 0:
        return render(request, 'todo.html', {'todos': []})
    for i in todos:
        if search_query in i['title']:
            res_todos.append(i)
    return render(request, 'todo.html', {'todos': res_todos})
