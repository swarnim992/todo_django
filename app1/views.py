from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    return render(request, 'app1/home.html')

@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def calculate(request):
    # num1 = request.query_params.get('num1')
    # operator = request.query_params.get('operator')
    # num2 = request.query_params.get('num2')
    if request.method == 'GET':
        return Response({"message": "Send POST request with student data"})

    if request.method == 'POST':
        name = request.data.get("name")
        age = request.data.get("age")

        if not name or not age:
            return Response(
                {"error": "name and age are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {
                "message": "Student created successfully",
                "data": {
                    "name": name,
                    "age": age
                }
            },
            status=status.HTTP_201_CREATED
        )

    result = 0
    # if(operator == '+'):
    #     result = num1+num2

    return Response({"result": result}, safe=False)

@login_required
def todo_list(request):
    todos = Todo.objects.all().order_by('-created_at')
    return render(request, 'app1/todo_list.html', {'todos': todos})

@login_required
def todo_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title:
            Todo.objects.create(title=title, description=description)
        return redirect('todo_list')
    return render(request, 'app1/todo_form.html', {'action': 'Create'})

@login_required
def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.completed = 'completed' in request.POST
        todo.save()
        return redirect('todo_list')
    return render(request, 'app1/todo_form.html', {'todo': todo, 'action': 'Update'})

@login_required
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'app1/todo_confirm_delete.html', {'todo': todo})

@login_required
def demo_json(request):
    data = {
        'name': 'App1',
        'version': '1.0',
        'features': ['feature1', 'feature2', 'feature3']
    }
    return JsonResponse(data)