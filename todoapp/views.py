from django.shortcuts import render, redirect
from todoapp.forms import TodoForm, TodoUpdateForm
from todoapp.models import ToDo
from django.contrib import messages


# Create your views here.
def todoapp(request):
    context = {}
    todolist = ToDo.objects.all().order_by('-date_posted')
    context['todolist'] = todolist
    if request.method == 'POST':
        forms = TodoForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, ' Your Item has been  Added Successfully')
            return redirect('todoapp:todoapp')
    else:
        forms = TodoForm()
        context['forms'] = forms

    return render(request, 'todoapp/todoapp.html', context)


def delete(request, pk):

    items = ToDo.objects.get(pk=pk)
    items.delete()
    messages.info(request, 'Your message has been deleted succesfully')
    return redirect('todoapp:todoapp')


def edit_list(request, pk):
    context = {}
    items = ToDo.objects.get(pk=pk)
    if request.POST:
        todo_forms = TodoUpdateForm(request.POST, instance=items)
        if todo_forms.is_valid():
            obj = todo_forms.save()
            obj.save()
            context['success_message'] = 'Your List Has Been Updated.'
            items = obj

    todo_forms = TodoUpdateForm(
        initial={
            'content': items.content,
        }
    )
    context['todo_form'] = todo_forms

    return render(request, 'todoapp/edit_list.html', context)