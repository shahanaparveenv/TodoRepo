from django.shortcuts import render, redirect

from todo_app.forms import TodoForm
from todo_app.models import Todo


# Create your views here.
def index(request):
    return render(request,'index1.html')
def dashboard2(request):
    return render(request,'index3.html')
#Create
def todo(request):
    data=TodoForm()
    if request.method == 'POST':
        data1 = TodoForm(request.POST)
        if data1.is_valid():
            data1.save()
            return redirect('todo_list')
    return render(request,'addTodo.html',{'form':data})


#Read
def todo_list(request):
    data=Todo.objects.all()
    return render(request,'list1.html',{'data':data})

def hello(request):
    return render(request,'hello.html')