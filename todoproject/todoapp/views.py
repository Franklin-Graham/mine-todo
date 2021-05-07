from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import  DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .forms import UpdateForm
from .models import Task
from django.contrib import messages
# Create your views here.
class TaskList(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'T'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'F'
    fields = ('task','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')





def fun1(request):
    task1 = Task.objects.all()
    if request.method=="POST":
        task= request.POST.get('task','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        task = Task(task=task,priority=priority,date=date)
        task.save()

    return render(request,'home.html',{'T':task1})

#delete
def delete(request,id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

#edit/update
def update(request,id):
    task =Task.objects.get(id=id)
    f = UpdateForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'T':task,'F':f})
#
# def detail(request,id):
#     task = Task.objects.get(id=id)
#     return render(request,'detail.html',{'task':task})