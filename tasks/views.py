from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Task 
from .forms import TaskForm

@login_required(login_url="/login/")
def task_index (request, *args, **kwargs):
    
    context = {
        'user': request.user,
    }

    return render(request, 'tasks/tasks.html', context)


@login_required(login_url="/login/")
def task_create(request, *args, **kwargs):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        title = form.data.get('task_title')
        description = form.data.get('task_description')
        new_task = Task(title=title, description=description)
        new_task.save()
        request.user.tasks.add(new_task)
        form = TaskForm()
        return HttpResponseRedirect(reverse('tasks:task_index'))

    context = {
        'form': form,
    }

    return render(request, 'tasks/create.html', context)

@login_required()
def task_delete(request, task_id, *args, **kwargs):
    task = get_object_or_404(Task, pk=task_id)
    user_task = get_object_or_404(request.user.tasks, pk=task_id)

    if user_task == task:
        task.delete()
    
    return HttpResponseRedirect(reverse('tasks:task_index'))

@login_required()
def task_check(request, task_id, *args, **kwargs):
    task = get_object_or_404(Task, pk=task_id)
    user_task = get_object_or_404(request.user.tasks, pk=task_id)

    if user_task == task:
        if task.checked:
            task.checked = False
        else:
            task.checked = True
        
        task.save()

    return HttpResponseRedirect(reverse('tasks:task_index'))